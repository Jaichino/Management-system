##############################################################################
# Importaciones
##############################################################################

from datetime import date, time
from model.database import engine, Turno, Cliente, Servicio
from sqlmodel import select, Session, join, distinct


##############################################################################
# Modelo Servicio
##############################################################################

class ModeloTurno:

    @staticmethod
    def nuevo_turno(
        cliente: int, 
        servicio: int, 
        fecha: date, 
        hora: time, 
        obs: str = None,
        estado: str = 'confirmado'
    ):
        ''' Método para agendar un nuevo turno

            :param int cliente: ID del cliente
            :param int servicio: ID del servicio a realizar
            :param date fecha: Fecha del servicio
            :param time hora: Hora del servicio
            :param str obs: Observaciones sobre el turno
            :param str estado: Estado del turno
        '''
        with Session(engine) as sesion:
            turno = Turno(
                cliente_id=cliente,
                servicio_id=servicio,
                fecha=fecha,
                hora=hora,
                observacion=obs,
                estado=estado
            )
            sesion.add(turno)
            sesion.commit()


    @staticmethod
    def turnos_fecha(fecha: date):
        ''' Método que devuelve una lista con todos los turnos agendados para
            una fecha determinada

            :param date fecha: Fecha de búsqueda
            :return: Lista con turnos para fecha elegida
            :rtype: list
        '''
        with Session(engine) as sesion:
            turnos_fecha = sesion.exec(
                select(
                    Turno.fecha,
                    Turno.hora,
                    Cliente.nombre, 
                    Servicio.nombre, 
                    Turno.observacion, 
                    Servicio.precio,
                    Servicio.duracion,
                    Turno.id
                )
                .join(Cliente, Cliente.id == Turno.cliente_id)
                .join(Servicio, Servicio.id == Turno.servicio_id)
                .where(Turno.fecha == fecha)
                .order_by(Turno.hora)
            ).all()

            return turnos_fecha


    @staticmethod
    def eliminar_turno(id: int):
        ''' Método para eliminar un determinado turno

            :param int id: ID del turno a eliminar
        '''
        with Session(engine) as sesion:
            turno_eliminar = sesion.exec(
                select(Turno).where(Turno.id == id)
            ).one()
            sesion.delete(turno_eliminar)
            sesion.commit()
    

    @staticmethod
    def historial_turnos(cliente: int, fecha: date, servicio: int = None):
        ''' Método para devolver un listado del historial de turnos que ha
            tenido un cliente determinado. Se podrá filtrar por cliente y
            por servicio, siendo el filtrado por servicio opcional. Si no se
            filtra por servicio, se muestran todos los tratamientos realizados
            al cliente buscado. El parámetro fecha es para que se muestren los
            turnos que ya fueron realizados (antes del día actual).
        
            :param int cliente: ID del cliente que se quiere revisar
            :param int servicio: ID del servicio que se quiere buscar
            :param date fecha: Será la fecha actual
            :return: Lista de turnos realizados para un cliente
            :rtype: list
        '''
        with Session(engine) as sesion:
            if servicio is None:
                query = (
                    select(
                        Turno.fecha,
                        Cliente.nombre,
                        Servicio.nombre,
                        Turno.observacion
                    )
                    .join(Cliente, Cliente.id == Turno.cliente_id)
                    .join(Servicio, Servicio.id == Turno.servicio_id)
                    .where(Cliente.id == cliente, Turno.fecha <= fecha)
                    .order_by(Turno.fecha)
                )
            else:
                query = (
                    select(
                        Turno.fecha,
                        Cliente.nombre,
                        Servicio.nombre,
                        Turno.observacion
                    )
                    .join(Cliente, Cliente.id == Turno.cliente_id)
                    .join(Servicio, Servicio.id == Turno.servicio_id)
                    .where(
                        Cliente.id == cliente,
                        Servicio.id == servicio,
                        Turno.fecha <= fecha
                    )
                    .order_by(Turno.fecha)
                )

            historial = sesion.exec(query).all()

            return historial
    

    @staticmethod
    def clientes_con_turnos():
        ''' Método para obtener un listado de todos los clientes que alguna
            vez se realizaron algún tratamiento.

            :return: Lista de objetos Cliente distintos que sacaron turno
        '''
        with Session(engine) as sesion:
            clientes = sesion.exec(
                select(Cliente)
                .distinct(Cliente.id)
                .join(Turno, Turno.cliente_id == Cliente.id)
                .order_by(Cliente.nombre)
            ).all()

            return clientes