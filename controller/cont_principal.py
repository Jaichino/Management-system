##############################################################################
# Importaciones
##############################################################################

from PySide6.QtWidgets import QMainWindow

from view.interfaces.ventana_principal import VentanaPrincipal
from controller.cont_clientes import ClienteController, NuevoClienteController
from controller.cont_servicios import (
    NuevoServicioController, ServiciosController
)
from controller.cont_turnos import (
    NuevoTurnoController, TurnoController, VentanaObservacionController
)
from controller.cont_producto import (
    ProductoController, NuevoProductoController
)
from controller.cont_venta import DetalleVentaController, VentasController
from controller.cont_ccorriente import CuentaCorrienteController

##############################################################################
##############################################################################
#                CONTROLADOR PRINCIPAL DE LA APLICACIÓN                      #
##############################################################################
##############################################################################

class MainController(QMainWindow):

    def __init__(self):
        super().__init__()
        self.main_ui = VentanaPrincipal()
        self.main_ui.setupUi(self)

        # Referencia a controladores
        self.producto_controller = ProductoController(self)
        self.cliente_controller = ClienteController(self)
        self.servicio_controller = ServiciosController(self)
        self.turno_controller = TurnoController(self)
        self.venta_controller = VentasController(self)
        self.cc_controller = CuentaCorrienteController(self)

        ######################################################################
        # Llamada widgets necesarios
        ######################################################################
        # Stacked widgets
        self.stacked_principal = self.main_ui.StackedWidget
        self.stacked_ventas = self.main_ui.stackedVentas
        
        # Buttons Principales
        self.btn_menu_principal = self.main_ui.btnMenu
        self.btn_menu_cliente = self.main_ui.btnMenuClientes
        self.btn_menu_servicios = self.main_ui.btnMenuServicios
        self.btn_menu_turnos = self.main_ui.btnMenuTurnos
        self.btn_menu_historial = self.main_ui.btnMenuHistorial
        self.btn_menu_productos = self.main_ui.btnMenuProductos
        self.btn_menu_ventas = self.main_ui.btnMenuVentas
        self.btn_menu_ccorriente = self.main_ui.btnMenuCCorriente

        self.btn_volver_venta = self.main_ui.btnVolverAVenta
        self.btn_consulta_venta = self.main_ui.btnConsultaVentas

        self.btn_nuevo_servicio = self.main_ui.btnNuevoServicio
        self.btn_nuevo_turno = self.main_ui.btnNuevoTurno
        self.btn_nuevo_producto = self.main_ui.btnNuevoProducto
        self.btn_nuevo_cliente = self.main_ui.btnNuevoCliente

        # Txts
        self.txt_cliente = self.main_ui.lineEditCliente
        self.txt_codigo_producto = self.main_ui.txtCodigoProd
        self.txt_codigo_prodventa = self.main_ui.txtCodigoProdVenta

        ######################################################################
        # Seteo de botones para recorrer menú
        ######################################################################

        # Seteo de la página principal StackedWidget
        self.stacked_principal.setCurrentIndex(6)
        # Seteo de la pagina principal del stacked de ventas
        self.stacked_ventas.setCurrentIndex(1)

        # Botón para ir a menú principal
        self.btn_menu_principal.clicked.connect(self.ir_menu_principal)
        # Botón para abrir menú de clientes
        self.btn_menu_cliente.clicked.connect(self.abrir_menu_clientes)
        # Botón para abrir menú de servicios
        self.btn_menu_servicios.clicked.connect(self.abrir_menu_servicios)
        # Botón para abrir menú de turnos
        self.btn_menu_turnos.clicked.connect(self.abrir_menu_turnos)
        # Botón para abrir menú de historial de tratamientos
        self.btn_menu_historial.clicked.connect(self.abrir_menu_historial)
        # Botón para abrir menú de productos
        self.btn_menu_productos.clicked.connect(self.abrir_menu_productos)
        # Bóton para abrir menú de ventas
        self.btn_menu_ventas.clicked.connect(self.abrir_menu_ventas)
        # Botón para abrir menú de cuenta corriente
        self.btn_menu_ccorriente.clicked.connect(self.abrir_menu_ccorriente)

        ######################################################################
        # Movimiento en stacked de ventas

        # Ir a pantalla de nueva venta
        self.btn_volver_venta.clicked.connect(self.ir_nueva_venta)
        # Ir a pantalla de consulta de ventas
        self.btn_consulta_venta.clicked.connect(self.ir_consulta_ventas)


        ######################################################################
        # Apertura ventanas secundarias
        ######################################################################
        
        # Abrir ventana para nuevo servicio
        self.btn_nuevo_servicio.clicked.connect(self.ventana_nuevo_servicio)
        # Abrir ventana para agendar nuevo cliente
        self.btn_nuevo_cliente.clicked.connect(self.ventana_nuevo_cliente)
        # Abrir ventana para nuevo producto
        self.btn_nuevo_producto.clicked.connect(self.ventana_nuevoproducto)
        # Abrir ventana para nuevo turno
        self.btn_nuevo_turno.clicked.connect(self.ventana_nuevo_turno)


    ##########################################################################
    # Movimiento entre menú principal
    ##########################################################################

    # Método para llevar stacked a menú principal
    def ir_menu_principal(self):
        self.stacked_principal.setCurrentIndex(6)

    # Método para llevar stacked a menú clientes
    def abrir_menu_clientes(self):
        self.stacked_principal.setCurrentIndex(7)
        self.txt_cliente.setFocus()

    # Método para llevar stacked a menú servicios
    def abrir_menu_servicios(self):
        self.stacked_principal.setCurrentIndex(0)

    # Método para llevar stacked a menú turnos
    def abrir_menu_turnos(self):
        self.stacked_principal.setCurrentIndex(1)

    # Método para llevar stacked a menú historial de tratamientos
    def abrir_menu_historial(self):
        self.stacked_principal.setCurrentIndex(5)

    # Método para llevar stacked a menú productos
    def abrir_menu_productos(self):
        self.stacked_principal.setCurrentIndex(4)
        self.txt_codigo_producto.setFocus()

    # Método para llevar stacked a menú ventas
    def abrir_menu_ventas(self):
        self.stacked_principal.setCurrentIndex(2)
        self.txt_codigo_prodventa.setFocus()

    # Método para llevar stacked a menú cuenta corriente
    def abrir_menu_ccorriente(self):
        self.stacked_principal.setCurrentIndex(3)

    # Método para llevar stacked ventas a ventana consulta ventas
    def ir_consulta_ventas(self):
        self.stacked_ventas.setCurrentIndex(0)
        
    # Método para llevar stacked ventas a ventana nueva venta
    def ir_nueva_venta(self):
        self.stacked_ventas.setCurrentIndex(1)


    ##########################################################################
    # Apertura de ventanas secundarias
    ##########################################################################
    # Apertura ventana nuevo cliente
    def ventana_nuevo_cliente(self):
        self.abrir_nuevo_cliente = NuevoClienteController(self)
        self.abrir_nuevo_cliente.show()
    
    # Apertura ventana nuevo servicio
    def ventana_nuevo_servicio(self):
        self.abrir_nuevo_servicio = NuevoServicioController(self)
        self.abrir_nuevo_servicio.show()

    # Apertura ventana nuevo turno
    def ventana_nuevo_turno(self):
        self.abrir_nuevo_turno = NuevoTurnoController(self)
        self.abrir_nuevo_turno.show()
    
    # Apertura ventana nuevo producto
    def ventana_nuevoproducto(self):
        self.abrir_nuevoproducto = NuevoProductoController(self)
        self.abrir_nuevoproducto.exec()
    
    # Apertura ventana detalle venta
    def ventana_detalleventa(self, nro_venta: int):
        self.abrir_detalleventa = DetalleVentaController(self, nro_venta)
        self.abrir_detalleventa.exec()

    # Apertura ventana observaciones de turnos
    def ventana_observacion(self, turno_id: int):
        self.abrir_observacion = VentanaObservacionController(self, turno_id)
        self.abrir_observacion.exec()

