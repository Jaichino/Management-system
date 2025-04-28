##############################################################################
# Importaciones
##############################################################################

from model.database import engine, Cliente
from sqlmodel import select, Session

##############################################################################
# Modelo Clientes
##############################################################################

class ModeloCliente():

    @staticmethod
    def nuevo_cliente(
        nombre: str,  
        cel: int = None, 
        email: str = None
    ):
        ''' Método para insertar nuevos clientes a la base de datos
            :param str nombre: Nombre del cliente
            :param int cel: Teléfono del cliente
            :param str email: Email del cliente
        '''
        with Session(engine) as sesion:
            cliente = Cliente(
                nombre=nombre,
                telefono=cel,
                email=email
            )
            sesion.add(cliente)
            sesion.commit()


    @staticmethod
    def lista_clientes():
        ''' Metodo para obtener todos los clientes registrados
            :return: Lista de clientes
            :rtype: list
        '''
        with Session(engine) as sesion:
            clientes = sesion.exec(
                select(Cliente)
            ).all()
            return clientes
    

    @staticmethod
    def filtrar_cliente(coinc_nombre: str):
        ''' Método para obtener lista filtrada de clientes segun coincidencia
            de nombre
            :param str coinc_nombre: Coincidencia con nombre
            :return: Lista de clientes filtrados por nombre
            :rtype: list
        '''
        with Session(engine) as sesion:
            clientes_filtrados = sesion.exec(
                select(Cliente)
                .where(Cliente.nombre.like(f"%{coinc_nombre}%"))
            ).all()

            return clientes_filtrados


    @staticmethod
    def editar_cliente(
        id: int, 
        nombre: str, 
        cel: int = None, 
        email: str = None
    ):
        ''' Método para editar un cliente segun su ID
            :param int id: ID del cliente a editar
            :param str nombre: Nombre del cliente
            :param int cel: Telefono del cliente
            :param str email: Email del cliente
        '''
        with Session(engine) as sesion:
            cliente_editar = sesion.exec(
                select(Cliente).where(Cliente.id == id)
            ).one()

            cliente_editar.nombre = nombre
            cliente_editar.telefono = cel
            cliente_editar.email = email
            sesion.add(cliente_editar)
            sesion.commit()


    @staticmethod
    def info_cliente(id: int):
        ''' Método para obtener la información de un cliente en particular
            según su ID.
            :param int id: ID del cliente
            :return: Lista con objeto Cliente
        '''
        with Session(engine) as sesion:
            cliente = sesion.exec(
                select(Cliente).where(Cliente.id == id)
            ).one()

            return cliente
        
    
    @staticmethod
    def eliminar_cliente(id: int):
        ''' Método utilizado para eliminar un cliente determinado
            :param int id: ID del cliente a eliminar
        '''
        with Session(engine) as sesion:
            cliente_eliminar = sesion.exec(
                select(Cliente).where(Cliente.id == id)
            ).one()

            sesion.delete(cliente_eliminar)
            sesion.commit()
