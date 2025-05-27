##############################################################################
# Importaciones
##############################################################################

from datetime import date, time
from enum import Enum
from sqlmodel import SQLModel, Relationship, create_engine, Field, text
from sqlalchemy import event

##############################################################################
# Modelado de base de datos
##############################################################################

##############################################################################
# Creación tabla Cliente
##############################################################################
class Cliente(SQLModel, table=True):

    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    telefono: int | None = None
    email: str | None = None

    turnos_cliente: list["Turno"] = Relationship(
        back_populates="cliente", cascade_delete=True
    )

    ventas: list["Venta"] = Relationship(
        back_populates='cliente'
    )

    ccorrientes: list["CuentaCorriente"] = Relationship(
        back_populates='cliente', cascade_delete=True
    )

    fichas: list["FichaCosmetologica"] = Relationship(
        back_populates="cliente", cascade_delete=True
    )

##############################################################################
# Creación tabla Servicio
##############################################################################
class Servicio(SQLModel, table=True):

    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    duracion: int
    precio: float

    turnos_servicio: list["Turno"] = Relationship(
        back_populates="servicio", cascade_delete=True
    )

##############################################################################
# Creación tabla Turno
##############################################################################

class EstadoTurno(str, Enum):
    pendiente = "Pendiente"
    realizado = "Realizado"
    confirmado = "Confirmado"
    cancelado = "Cancelado"

class Turno(SQLModel, table=True):

    id: int | None = Field(default=None, primary_key=True)
    cliente_id: int = Field(foreign_key="cliente.id", ondelete="CASCADE")
    servicio_id: int = Field(foreign_key="servicio.id", ondelete="CASCADE")
    fecha: date
    hora: time
    observacion: str | None = None
    estado: EstadoTurno
    senia: float

    cliente: Cliente = Relationship(back_populates="turnos_cliente")
    servicio: Servicio = Relationship(back_populates="turnos_servicio")


##############################################################################
# Creación tabla Producto
##############################################################################
class Producto(SQLModel, table=True):
    
    nro_producto: int | None = Field(default=None, primary_key=True)
    codigo_producto: str = Field(index=True)
    descripcion: str = Field(index=True)
    precio_unitario: float
    stock: int
    vencimiento: date
    estado: bool

    detalles_productos: list['DetalleVenta'] = Relationship(
        back_populates='producto'
    )

##############################################################################
# Creación tabla Venta
##############################################################################

class Venta(SQLModel, table=True):

    nro_venta: int | None = Field(default=None, primary_key=True)
    fecha_venta: date = Field(default=date.today())
    cliente_id: int | None =  Field(foreign_key="cliente.id", ondelete="SET NULL")
    monto_total: float
    modo_pago: str
    interes: float | None = None

    cliente: Cliente = Relationship(back_populates='ventas')

    detalles_ventas: list['DetalleVenta'] = Relationship(
        back_populates='venta', cascade_delete=True
    )

##############################################################################
# Creación tabla DetalleVenta
##############################################################################

class DetalleVenta(SQLModel, table=True):
    
    nro_venta: int = Field(
        foreign_key='venta.nro_venta', primary_key=True, ondelete="CASCADE"
    )
    nro_producto: int = Field(
                                foreign_key='producto.nro_producto',
                                primary_key=True
                            )
    precio_unitario: float
    cantidad: int

    venta: Venta = Relationship(back_populates='detalles_ventas')
    producto: Producto = Relationship(back_populates='detalles_productos')

##############################################################################
# Creación tabla CuentaCorriente
##############################################################################

class CuentaCorriente(SQLModel, table=True):
    
    nro_operacion: int | None = Field(default=None, primary_key=True)
    cliente_id: int = Field(foreign_key='cliente.id', ondelete="CASCADE")
    fecha_operacion: date
    tipo_operacion: str
    monto_operacion: float
    monto_pendiente: float

    cliente: Cliente = Relationship(back_populates='ccorrientes')


##############################################################################
# Creación tabla FichaCosmetologica
##############################################################################

class FichaCosmetologica(SQLModel, table=True):

    id_ficha: int | None = Field(default=None, primary_key=True)
    id_cliente: int = Field(foreign_key="cliente.id", ondelete="CASCADE")
    ficha: str

    cliente: Cliente = Relationship(back_populates='fichas')
##############################################################################
# Creacion de engine y seleccion de base de datos
##############################################################################

bd_name = "bla_estetica.db"
bd_url = f"sqlite:///{bd_name}"
engine = create_engine(bd_url, echo=True)

# SOLO PARA SQLite, PARA ACTIVAR LAS FOREIGN KEYS EN TODAS LAS SESIONES
@event.listens_for(engine, "connect")
def enable_foreign_keys(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

def create_bd():
    SQLModel.metadata.create_all(engine)
    with engine.connect() as connection:
        connection.execute(text("PRAGMA foreign_keys=ON"))

##############################################################################
# Ejecución solo para crear la base de datos
##############################################################################


if __name__ == "__main__":
   create_bd()

