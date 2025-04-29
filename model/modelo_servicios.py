##############################################################################
# Importaciones
##############################################################################

from model.database import engine, Servicio
from sqlmodel import select, Session

##############################################################################
# Modelo Servicio
##############################################################################

class ModeloServicio:

    @staticmethod
    def nuevo_servicio(nombre: str, duracion: int, precio: float):
        ''' Método para agregar nuevos servicios a la base de datos.
            :param str nombre: Nombre del servicio
            :param int duracion: Duración del servicio en minutos
            :param float precio: Precio del servicio
        '''
        with Session(engine) as sesion:
            servicio = Servicio(
                nombre=nombre,
                duracion=duracion,
                precio=precio
            )
            sesion.add(servicio)
            sesion.commit()


    @staticmethod
    def lista_servicios():
        ''' Método para obtener los servicios disponibles.
            :return: Lista de servicios disponibles
            :rtype: list
        '''
        with Session(engine) as sesion:
            servicios = sesion.exec(
                select(Servicio)
                .order_by(Servicio.nombre)
            ).all()

            return servicios


    @staticmethod
    def eliminar_servicio(id_servicio: int):
        ''' Método para eliminar un servicio determinado
            :param int id_servicio: ID del servicio a eliminar
        '''
        with Session(engine) as sesion:
            servicio_eliminar = sesion.exec(
                select(Servicio).where(Servicio.id == id_servicio)
            ).one()

            sesion.delete(servicio_eliminar)
            sesion.commit()


    @staticmethod
    def editar_servicio(id: int, nombre: str, duracion: int, precio: float):
        ''' Método para modificar un determinado servicio
            :param int id: ID del servicio a modificar
            :param str nombre: Nuevo nombre del servicio
            :param int duracion: Nueva duracion del servicio en minutos
            :param float precio: Nuevo precio del servicio
        '''
        with Session(engine) as sesion:
            servicio_editar = sesion.exec(
                select(Servicio).where(Servicio.id == id)
            ).one()

            servicio_editar.nombre = nombre
            servicio_editar.duracion = duracion
            servicio_editar.precio = precio
            sesion.add(servicio_editar)
            sesion.commit()

    
    @staticmethod
    def info_servicio(id: int):
        ''' Método para devolver la información de un servicio determinado
            :param int id: ID del servicio a obtener
        '''
        with Session(engine) as sesion:
            info = sesion.exec(
                select(Servicio).where(Servicio.id == id)
            ).one()

            return info