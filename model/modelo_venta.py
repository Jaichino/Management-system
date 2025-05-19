##############################################################################
# Importaciones
##############################################################################

from datetime import date
from sqlmodel import select, Session, between
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import IntegrityError
from model.database import (
    engine, Venta, DetalleVenta, Producto, CuentaCorriente
)

##############################################################################
# Modelo Ventas
##############################################################################

class ModeloVentas:

    @staticmethod
    def nueva_venta(
        fecha: date,
        cliente: int,
        monto_total: float,
        modo_pago: str,
        interes: float,
        productos: list
    ):
        ''' Método para generar una nueva venta

            :param date fecha: Fecha de venta
            :param int cliente: ID de cliente
            :param float monto_total: Monto total de venta
            :param str modo_pago: Modo de pago utilizado
            :param float interes: Interes de la venta
            :param list productos: Listado de productos vendidos
        '''
        with Session(engine) as sesion:
            try:
                # Agregado de venta
                venta = Venta(
                    fecha_venta=fecha,
                    cliente_id=cliente,
                    monto_total=monto_total,
                    modo_pago=modo_pago,
                    interes=interes
                )
                sesion.add(venta)
                sesion.flush()

                # Agregado de detalles de venta
                for producto in productos:
                    detalle = DetalleVenta(
                        nro_venta=venta.nro_venta,
                        nro_producto=producto['nro_producto'],
                        precio_unitario=producto['precio_unitario'],
                        cantidad=producto['cantidad']
                    )
                    sesion.add(detalle)

                    # Descuento de unidades vendidas del producto
                    producto_vendido = sesion.get(
                        Producto, producto['nro_producto']
                    )
                    producto_vendido.stock -= producto['cantidad']
                    sesion.add(producto_vendido)

                sesion.commit()

            except Exception as e:
                sesion.rollback()
                raise e


    @staticmethod
    def eliminar_venta(nro_venta: int, dev_stock: bool = False):
        ''' Método para eliminar una venta determinada por su nro_venta y
            devolver a stock los productos vendidos en caso de que dev_stock
            sea True

            :param int nro_venta: Número de venta a eliminar
            :param bool dev_stock: Indica si se devuelven productos a stock
        '''
        with Session(engine) as sesion:
            # Obtención de venta a eliminar
            venta_a_eliminar = sesion.exec(
                select(Venta).where(Venta.nro_venta == nro_venta)
            ).one()

            # Obtención del detalle de venta
            detalle_venta = sesion.exec(
                select(DetalleVenta)
                .options(selectinload(DetalleVenta.producto))
                .where(DetalleVenta.nro_venta == nro_venta)
            ).all()

            # Si dev_stock == True, se devuelven productos a stock
            if dev_stock:
                for det in detalle_venta:
                    producto = det.producto
                    cantidad_vendida = det.cantidad

                    producto.stock += cantidad_vendida 
                    sesion.add(producto)
            
            # Eliminación de venta
            sesion.delete(venta_a_eliminar)
            sesion.commit()


    @staticmethod
    def listado_ventas(desde: date, hasta: date, cliente: int = None):
        ''' Método para obtener el listado de ventas realizadas entre dos
            fechas o filtrando por cliente.

            :param date desde: Fecha inicial de busqueda
            :param date hasta: Fecha final de busqueda
            :param int cliente: ID de cliente
            :return: Lista de objetos Venta
        '''
        with Session(engine) as sesion:
            if cliente is not None:
                query = (
                    select(Venta)
                    .options(selectinload(Venta.cliente))
                    .where(
                        between(Venta.fecha_venta, desde, hasta),
                        Venta.cliente_id == cliente
                    )
                )

            else:
                query = (
                    select(Venta)
                    .options(selectinload(Venta.cliente))
                    .where(between(Venta.fecha_venta, desde, hasta))
                )
            
            listado_ventas = sesion.exec(query).all()
            return listado_ventas


    @staticmethod
    def consulta_detalleventa(nro_venta: int):
        ''' Método para obtener el detalle de una determinada venta

            :param int nro_venta: Número de venta a consultar detalle
            :return: Objeto DetalleVenta
        '''
        with Session(engine) as sesion:
            detalle_venta = sesion.exec(
                select(DetalleVenta)
                .options(selectinload(DetalleVenta.producto))
                .options(selectinload(DetalleVenta.venta))
                .where(DetalleVenta.nro_venta == nro_venta)
            ).all()
            
            return detalle_venta


    @staticmethod
    def obtener_venta(nro_venta: int):
        ''' Método para obtener una venta determinada por su nro_venta

            :param int nro_venta: ID de venta a consultar
            :return: Object Venta
            :rtype: object
        '''
        with Session(engine) as sesion:
            venta = sesion.exec(
                select(Venta)
                .options(selectinload(Venta.cliente))
                .where(Venta.nro_venta == nro_venta)
            ).first()

            return venta

# if __name__ == '__main__':