##############################################################################
# Importaciones
##############################################################################

from datetime import date
from sqlmodel import select, Session, between
from model.database import engine, Producto

##############################################################################
# Modelo Producto
##############################################################################
class ModeloProducto:

    @staticmethod
    def nuevo_producto(
        codigo: str,
        descripcion: str,
        precio: float,
        stock: int,
        vencimiento: date,
        estado: bool
    ):
        ''' Método para cargar nuevos productos

            :param str codigo: codigo del producto
            :param str descripcion: descripcion
            :param float precio: precio del producto
            :param int stock: stock del producto
            :param date vencimiento: vencimiento del producto
            :param bool estado: estado producto (1 activo, 0 eliminado)
        '''
        with Session(engine) as sesion:
            producto = Producto(
                codigo_producto=codigo,
                descripcion=descripcion,
                precio_unitario=precio,
                stock=stock,
                vencimiento=vencimiento,
                estado=estado
            )
            sesion.add(producto)
            sesion.commit()


    @staticmethod
    def listado_productos(
        codigo: str = None, descripcion: str = None, stock: int = None
    ):
        ''' Método para devolver el listado de productos existentes, se puede
            pasar codigo, descripcion o stock (para el caso que se quiera ver
            productos con stock = 0)

            :param str codigo: codigo del producto buscado
            :param str descripcion: descripcion del producto
            :param int stock: Stock de producto
            :return: lista de objetos Producto
        '''
        with Session(engine) as sesion:

            if codigo == None and descripcion == None and stock == None:
                query = (
                    select(Producto)
                    .where(Producto.estado == True)
                    .order_by(Producto.vencimiento)
                )
            
            elif codigo is not None:
                query = (select(Producto)
                        .where( Producto.codigo_producto == codigo, 
                                Producto.estado == True)
                        .order_by(Producto.vencimiento)
                        )
                
        
            elif descripcion is not None:
                query= (select(Producto)
                        .where( Producto.descripcion.like(f"%{descripcion}%"),
                                Producto.estado == True)
                        .order_by(Producto.vencimiento)
                        )
            
            elif stock is not None:
                query= (select(Producto)
                        .where( Producto.stock == stock,
                                Producto.estado == True)
                        .order_by(Producto.vencimiento)
                        )
            
            productos = sesion.exec(query).all()
            return(productos)


    @staticmethod
    def actualizar_producto(
        nro_producto: int,
        descripcion: str | None = None,
        precio: float | None = None,
        stock: int | None = None,
        vencimiento: date | None = None
    ):
        ''' Método para actualizar un producto determinado según nro_producto

            :param int nro_producto: Nro de producto a actualizar
            :param str descripcion: Descripcion del producto
            :param float precio: Precio del producto
            :param int stock: Stock del producto
            :param date stock: Fecha de vencimiento del producto
        '''
        with Session(engine) as sesion:
            producto_a_editar = sesion.exec(
                select(Producto).where(Producto.nro_producto == nro_producto)
            ).one()

            if descripcion is not None:
                producto_a_editar.descripcion  = descripcion
            if precio is not None:
                producto_a_editar.precio_unitario = precio
            if stock is not None:
                producto_a_editar.stock = stock
            if vencimiento is not None:
                producto_a_editar.vencimiento = vencimiento
            
            sesion.add(producto_a_editar)
            sesion.commit()


    @staticmethod
    def eliminar_producto(nro_producto: int, estado: bool = False):
        ''' Método para cambiar estado de producto a False indicando que el
            mismo ya no se encuentra disponible en el stock de productos.
            Sigue existiendo para no perder referencias de ventas.

            :param int nro_producto: Nro de producto a eliminar
        '''
        with Session(engine) as sesion:
            producto_a_eliminar = sesion.exec(
                select(Producto).where(Producto.nro_producto == nro_producto)
            ).one()
            
            producto_a_eliminar.estado = estado
            sesion.add(producto_a_eliminar)
            sesion.commit()


    @staticmethod
    def productos_entre_fechas(
        desde: date = None, hasta: date = None, codigo: str = None
    ):
        ''' Método para devolver lista de productos que se encuentran entre
            dos fechas determinadas o según su código
            
            :param date desde: Fecha inicial de busqueda
            :param date hasta: Fecha final de busqueda
            :param str codigo: Codigo del producto a buscar
            :return: Lista de objetos Producto
        '''
    
        with Session(engine) as sesion:

            if codigo is not None:
                query = (
                        select(Producto)
                        .where(
                            Producto.codigo_producto == codigo, 
                            Producto.estado == True)
                )
            
            else:
                query = (
                        select(Producto)
                        .where(
                            between(Producto.vencimiento, desde, hasta),
                            Producto.estado == True)
                )

            vencimientos = sesion.exec(query).all()
            return vencimientos


    @staticmethod
    def obtener_nro_producto(codigo: str, vencimiento: date):
        ''' Método para obtener el nro_producto a partir de un codigo y
            vencimiento

            :param str codigo: Codigo del producto
            :param date vencimiento: Vencimiento del producto
            :return: Numero de producto
            :rtype: int
        '''
        with Session(engine) as sesion:
            nro_producto = sesion.exec(
                select(Producto.nro_producto)
                .where(
                    Producto.codigo_producto == codigo, 
                    Producto.vencimiento == vencimiento,
                    Producto.estado == True
                )
            ).first()

            return nro_producto

#if __name__ == '__main__':