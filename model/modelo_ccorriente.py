##############################################################################
# Importaciones
##############################################################################

from datetime import date

from sqlmodel import select, Session, join, distinct, func
from sqlalchemy.orm import selectinload, joinedload
from sqlalchemy.orm import aliased

from model.database import engine, CuentaCorriente, Cliente

##############################################################################
# Modelo Cuenta Corriente
##############################################################################

class ModeloCuentaCorriente:

    @staticmethod
    def nueva_cuentacorriente(
        cliente: int,
        fecha: date,
        tipo_operacion: str,
        monto_operacion: float,
        monto_pendiente: float
    ):
        ''' Método para ingresar una nueva cuenta corriente

        :param int cliente: ID del cliente al que corresponde la cuenta
        :param date fecha: Fecha de operacion
        :param str tipo_operacion: Tipo de operacion (Adeuda, Paga)
        :param float monto_operacion: Monto de la operacion
        :param float monto_pendiente: Monto de deuda restante
        '''
        with Session(engine) as sesion:
            cuenta_corriente = CuentaCorriente(
                cliente_id=cliente,
                fecha_operacion=fecha,
                tipo_operacion=tipo_operacion,
                monto_operacion=monto_operacion,
                monto_pendiente=monto_pendiente
            )

            sesion.add(cuenta_corriente)
            sesion.commit()


    @staticmethod
    def lista_cuentacorriente(cliente: int):
        ''' Método para obtener las cuentas corrientes de un cliente
            determinado

            :param int cliente: ID del cliente a consultar cuenta corriente
            :return: Lista de objetos CuentaCorriente
        '''
        with Session(engine) as sesion:
            detalle_cc = sesion.exec(
                select(CuentaCorriente)
                .options(selectinload(CuentaCorriente.cliente))
                .where(CuentaCorriente.cliente_id == cliente)
            ).all()

            return detalle_cc


    @staticmethod
    def eliminar_cuentacorriente(cliente: int):
        ''' Método para eliminar la cuenta corriente de un determinado cliente
            cuando salda su deuda

            :param int cliente: ID del cliente a eliminar cuenta corriente
        '''
        with Session(engine) as sesion:
            registros_cc = sesion.exec(
                select(CuentaCorriente)
                .where(CuentaCorriente.cliente_id == cliente)
            ).all()

            for registro in registros_cc:
                sesion.delete(registro)
            
            sesion.commit()


    @staticmethod
    def eliminar_operacion(nro_operacion: int):
        ''' Método para eliminar un registro de operación de cuenta corriente

        :param int nro_operacion: Numero de operacion a eliminar
        '''
        with Session(engine) as sesion:
            operacion = sesion.exec(
                select(CuentaCorriente)
                .where(CuentaCorriente.nro_operacion == nro_operacion)
            ).one()

            sesion.delete(operacion)
            sesion.commit()


    @staticmethod
    def clientes_cuentacorriente():
        ''' Método para obtener los clientes que tienen cuentas corrientes
            abiertas

            :return: Lista de clientes con cuenta corriente
        '''
        with Session(engine) as sesion:
            clientes = sesion.exec(
                select(distinct(Cliente.id), Cliente.nombre)
                .join(
                    CuentaCorriente, CuentaCorriente.cliente_id == Cliente.id
                )
                .order_by(Cliente.nombre)
            ).all()

            return clientes
    

    @staticmethod
    def deuda_total_cuentacorrientes() -> float:
        ''' Método para obtener la deuda total en cuentas corrientes de todos
            los clientes.
        '''
        with Session(engine) as sesion:
            subquery = (
                select(
                    func.max(CuentaCorriente.nro_operacion).label("nro_operacion"),
                    CuentaCorriente.monto_pendiente
                )
                .group_by(CuentaCorriente.cliente_id)
                .subquery()
            )
            
            cc_alias = aliased(CuentaCorriente)

            query = (
                select(func.sum(cc_alias.monto_pendiente))
                .join(subquery, cc_alias.nro_operacion == subquery.c.nro_operacion)
            )
            results = sesion.exec(query).one()

            return results or 0.0

