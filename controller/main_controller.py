##############################################################################
# Importaciones
##############################################################################

from view.interfaces.ventana_principal import VentanaPrincipal
from view.interfaces.ventana_clientes import VentanaCliente
from view.interfaces.ventana_servicios import VentanaServicio
from view.interfaces.ventana_turnos import VentanaTurno
from view.interfaces.widget_tarjetaservicio import WidgetTarjetaServicio
from view.interfaces.widget_tarjetaturno import WidgetTarjetaTurno
from model.modelo_clientes import ModeloCliente
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QMessageBox)
from PySide6.QtGui import QStandardItemModel, QStandardItem


##############################################################################
# Controlador Widget - Tarjetas de Servicios
##############################################################################

class TarjetaTurnosController(QWidget):
    def __init__(self):
        super().__init__()
        self.widget_tarjetaturno = WidgetTarjetaTurno()
        self.widget_tarjetaturno.setupUi(self)

##############################################################################
# Controlador Widget - Tarjetas de Servicios
##############################################################################

class TarjetaServiciosController(QWidget):
    def __init__(self):
        super().__init__()
        self.widget_tarjetaservicio = WidgetTarjetaServicio()
        self.widget_tarjetaservicio.setupUi(self)

##############################################################################
# Controlador ventana nuevos clientes
##############################################################################

class ClienteController(QMainWindow):
    
    def __init__(self, main_controller):
        super().__init__()
        self.ui_cliente = VentanaCliente()
        self.ui_cliente.setupUi(self)
        self.main_controller = main_controller
        self.modelo_cliente = ModeloCliente()

        self.ui_cliente.btnAgregarCliente.clicked.connect(self.nuevo_cliente)


    def nuevo_cliente(self):
        try:
            # Recuperación de valores de campo
            nombre = self.ui_cliente.txtNombre.text().upper() 
            cel = int(self.ui_cliente.txtCelular.text())
            email = self.ui_cliente.txtEmail.text().lower()

            # Comprobación de que se llenan campos obligatorios
            if nombre == '':
                QMessageBox.critical(
                    self,
                    "Nuevo Cliente",
                    "El campo de nombre es obligatorio"
                )
                return

            # Carga de cliente
            self.modelo_cliente.nuevo_cliente(nombre, cel, email)

            # Limpieza de campos
            nombre = self.ui_cliente.txtNombre.setText("")
            cel = self.ui_cliente.txtCelular.setText("")
            email = self.ui_cliente.txtEmail.setText("")

            # Actualización de tabla
            self.main_controller.cargar_clientes()
            
            # Mensaje de confirmación
            QMessageBox.information(self, "Nuevo Cliente", "Cliente Creado!")

        except ValueError:
            QMessageBox.critical(
                self,
                "Nuevo Cliente",
                "Revisar campos"
            )

        except Exception as e:
            QMessageBox.critical(
                self,
                "Nuevo Cliente",
                f"Error - {e}"
            )

##############################################################################
# Controlador ventana nuevos servicios
##############################################################################

class ServicioController(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.ui_servicio = VentanaServicio()
        self.ui_servicio.setupUi(self)

##############################################################################
# Controlador ventana nuevos turnos
##############################################################################

class TurnoController(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.ui_turno = VentanaTurno()
        self.ui_turno.setupUi(self)


##############################################################################
# Controlador Principal
##############################################################################

class MainController(QMainWindow):

    def __init__(self):
        super().__init__()
        self.main_ui = VentanaPrincipal()
        self.main_ui.setupUi(self)

        # Seteo de la página principal StackedWidget
        self.main_ui.StackedWidget.setCurrentIndex(2)

        # Seteo de botones para recorrer menú
        self.main_ui.btn_clientes.clicked.connect(self.abrir_menu_clientes)
        self.main_ui.btn_servicios.clicked.connect(self.abrir_menu_servicios)
        self.main_ui.btn_turnos.clicked.connect(self.abrir_menu_turnos)

        # Abrir ventana para agendar nuevo cliente
        self.main_ui.btnNuevoCliente.clicked.connect(
            self.ventana_nuevo_cliente
        )

        # Abrir ventana para agregar nuevo servicio
        self.main_ui.btnNuevoServicio.clicked.connect(
            self.ventana_nuevo_servicio
        )

        # Abrir ventana para agregar nuevo turno
        self.main_ui.btnNuevoTurno.clicked.connect(
            self.ventana_nuevo_turno
        )
        
        # Llamadas para agregar tarjetas de servicios y turnos
        self.agregar_servicios()
        self.agregar_turnos()

        # Visualización de clientes en tabla
        self.cargar_clientes()


    # Movimiento entre menú principal
    def abrir_menu_clientes(self):
        self.main_ui.StackedWidget.setCurrentIndex(3)
    
    def abrir_menu_servicios(self):
        self.main_ui.StackedWidget.setCurrentIndex(0)
    
    def abrir_menu_turnos(self):
        self.main_ui.StackedWidget.setCurrentIndex(1)

    # Apertura ventana nuevo cliente
    def ventana_nuevo_cliente(self):
        self.abrir_nuevo_cliente = ClienteController(self)
        self.abrir_nuevo_cliente.show()
    
    # Apertura ventana nuevo servicio
    def ventana_nuevo_servicio(self):
        self.abrir_nuevo_servicio = ServicioController()
        self.abrir_nuevo_servicio.show()

    # Apertura ventana nuevo turno
    def ventana_nuevo_turno(self):
        self.abrir_nuevo_turno = TurnoController()
        self.abrir_nuevo_turno.show()

    ##############################################################################
    # Método para carga de clientes en QTableView
    ##############################################################################

    def cargar_clientes(self):
        
        # Se establece modelo y headers del modelo
        self.modelo = QStandardItemModel()
        self.modelo.setHorizontalHeaderLabels(["Nombre", "Telefono", "Email"])

        # Se limpia el modelo antes de cargar clientes
        self.modelo.removeRows(0, self.modelo.rowCount())
    
        # Se recuperan clientes de la base de datos
        clientes = ModeloCliente.lista_clientes()

        for cliente in clientes:
            fila = [
                QStandardItem(cliente.nombre),
                QStandardItem(str(cliente.telefono)),
                QStandardItem(cliente.email)
            ]
            self.modelo.appendRow(fila)
        
    
        self.main_ui.tablaClientes.setModel(self.modelo)

        self.main_ui.tablaClientes.setColumnWidth(0,200)
        self.main_ui.tablaClientes.setColumnWidth(1,300)
        self.main_ui.tablaClientes.setColumnWidth(2,360)

    ##############################################################################
    # Posicionamiento de tarjetas de Servicios y Turnos
    ##############################################################################

    def agregar_servicios(self):

        servicios = [
            {"nombre": "Limpieza Facial", "duracion": 60, "precio": 2500},
            {"nombre": "Limpieza Facial", "duracion": 60, "precio": 2500},
            {"nombre": "Limpieza Facial", "duracion": 60, "precio": 2500},
            {"nombre": "Limpieza Facial", "duracion": 60, "precio": 2500},
            {"nombre": "Limpieza Facial", "duracion": 60, "precio": 2500},
            {"nombre": "Limpieza Facial", "duracion": 60, "precio": 2500},
            {"nombre": "Limpieza Facial", "duracion": 60, "precio": 2500},
            
            
        ]

        contenedor = self.main_ui.contenedorServicios.layout()
        
        if contenedor is None:
            contenedor = QVBoxLayout(self.main_ui.contenedorServicios)
            contenedor.setContentsMargins(0,0,0,0)
            contenedor.setSpacing(10)
            self.main_ui.contenedorServicios.setLayout(contenedor)
            
        
        for servicio in servicios:
            tarjeta = TarjetaServiciosController()
            tarjeta.widget_tarjetaservicio.lblServicio.setText(servicio["nombre"])
            tarjeta.widget_tarjetaservicio.lblDuracion.setText(f'{servicio["duracion"]} minutos')
            tarjeta.widget_tarjetaservicio.lblPrecio.setText(f'$ {servicio["precio"]}')
            contenedor.addWidget(tarjeta)
        
        contenedor.addSpacerItem(
            QSpacerItem(20,40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )
    

    def agregar_turnos(self):

        turnos = [
            {'id': 1,'cliente':'Juan', 'servicio':'Limpieza Facial', 'obs':'Todo OK', 'precio':10000, 'hora': '12:00'},
            {'id':2,'cliente':'Juan', 'servicio':'Limpieza Facial', 'obs':'Todo OK', 'precio':10000, 'hora': '12:00'},
        ]
        # Se define el contenedor donde irán las tarjetas
        contenedor = self.main_ui.contenedorTurnos.layout()

        for turno in turnos:
            tarjeta = TarjetaTurnosController()
            tarjeta.widget_tarjetaturno.lblCliente.setText(turno["cliente"])
            tarjeta.widget_tarjetaturno.lblServicio.setText(turno["servicio"])
            tarjeta.widget_tarjetaturno.lblObservacion.setText(turno["obs"])
            tarjeta.widget_tarjetaturno.lblHoraTurno.setText(turno["hora"])
            tarjeta.widget_tarjetaturno.lblPrecio.setText(f'$ {turno["precio"]}')
            #################################
            # Ejemplo de como capturar el id en los botones
            tarjeta.widget_tarjetaturno.btnCancelarTurno.clicked.connect(
                lambda _, turno_id=turno['id']: self.imprimir_turno(turno_id))
            #################################

            contenedor.addWidget(tarjeta)

        contenedor.addSpacerItem(
            QSpacerItem(20,40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )
    
    # Ejemplo para imprimir el id capturado en cada boton
    def imprimir_turno(self, turno_id):
        print(turno_id)