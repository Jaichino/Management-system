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

class Cliente(SQLModel, table=True):

    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    apellido: str
    telefono: int | None = None
    email: str | None = None

    turnos_cliente: list["Turno"] = Relationship(
        back_populates="cliente", cascade_delete=True
    )

class Servicio(SQLModel, table=True):

    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    duracion: int
    precio: float

    turnos_servicio: list["Turno"] = Relationship(
        back_populates="servicio", cascade_delete=True
    )


class EstadoTurno(str, Enum):
    pendiente = "pendiente"
    realizado = "realizado"
    confirmado = "confirmado"
    cancelado = "cancelado"


class Turno(SQLModel, table=True):

    id: int | None = Field(default=None, primary_key=True)
    cliente_id: int = Field(foreign_key="cliente.id", ondelete="CASCADE")
    servicio_id: int = Field(foreign_key="servicio.id", ondelete="CASCADE")
    fecha: date
    hora: time
    observacion: str | None = None
    estado: EstadoTurno

    cliente: Cliente = Relationship(back_populates="turnos_cliente")
    servicio: Servicio = Relationship(back_populates="turnos_servicio")


##############################################################################
# Creacion de engine y seleccion de base de datos
##############################################################################

bd_name = "turnero_bla.db"
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

#if __name__ == "__main__":
#    create_bd()
#
#