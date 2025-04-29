##############################################################################
# Importaciones
##############################################################################

from datetime import date, time
from model.database import engine, Turno, Cliente, Servicio
from sqlmodel import select, Session, join

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