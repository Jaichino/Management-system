##############################################################################
# Importaciones
##############################################################################

from datetime import date
from sqlmodel import select, Session, between
from sqlalchemy.orm import selectinload
from model.database import engine, Venta, DetalleVenta

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
        interes: float
    ):
        ''' Método para generar una nueva venta

            :param date fecha: Fecha de venta
            :param int cliente: ID de cliente
            :param float monto_total: Monto total de venta
            :param str modo_pago: Modo de pago utilizado
            :param float interes: Interes de la venta
        '''
        with Session(engine) as sesion:
            venta = Venta(
                fecha_venta=fecha,
                cliente_id=cliente,
                monto_total=monto_total,
                modo_pago=modo_pago,
                interes=interes
            )
            
            sesion.add(venta)
            sesion.commit()


    @staticmethod
    def nuevo_detalle_venta(
        nro_venta: int,
        nro_producto: int,
        precio: float,
        cantidad: int
    ):
        ''' Método para ingresar un nuevo detalle de venta

            :param int nro_venta: Número de venta
            :param int nro_producto: Número de producto vendido
            :param float precio: Precio unitario del producto
            :param int cantidad: Cantidad vendida del producto nro_producto
        '''
        with Session(engine) as sesion:
            detalle_venta = DetalleVenta(
                nro_venta=nro_venta,
                nro_producto=nro_producto,
                precio_unitario=precio,
                cantidad=cantidad
            )
            sesion.add(detalle_venta)
            sesion.commit()
    

    @staticmethod
    def eliminar_venta(nro_venta: int):
        ''' Método para eliminar una venta determinada por su nro_venta

            :param int nro_venta: Número de venta a eliminar
        '''
        with Session(engine) as sesion:
            venta_a_eliminar = sesion.exec(
                select(Venta).where(Venta.nro_venta == nro_venta)
            ).one()

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
                .where(DetalleVenta.nro_venta == nro_venta)
            ).all()
            
            return detalle_venta


# if __name__ == '__main__':