##############################################################################
# Importaciones
##############################################################################

from datetime import date
from PySide6.QtWidgets import (
    QMainWindow, QMessageBox
)
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt

from view.interfaces.ventana_principal import VentanaPrincipal

from model.modelo_ccorriente import ModeloCuentaCorriente

from controller.cont_clientes import ClienteController, NuevoClienteController
from controller.cont_servicios import (
    NuevoServicioController, ServiciosController
)
from controller.cont_turnos import NuevoTurnoController, TurnoController
from controller.cont_producto import (
    ProductoController, NuevoProductoController
)
from controller.cont_venta import DetalleVentaController, VentasController


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

        ######################################################################
        # Variables iniciales
        ######################################################################
    
        
        
        self.deuda = 0


        ######################################################################
        # Seteo de botones para recorrer menú
        ######################################################################

        # Seteo de la página principal StackedWidget
        self.main_ui.StackedWidget.setCurrentIndex(6)
        # Seteo de la pagina principal del stacked de ventas
        self.main_ui.stackedVentas.setCurrentIndex(1)

        self.main_ui.btnMenu.clicked.connect(self.ir_menu_principal)
        self.main_ui.btnMenuClientes.clicked.connect(self.abrir_menu_clientes)
        self.main_ui.btnMenuServicios.clicked.connect(self.abrir_menu_servicios)
        self.main_ui.btnMenuTurnos.clicked.connect(self.abrir_menu_turnos)
        self.main_ui.btnMenuHistorial.clicked.connect(
            self.abrir_menu_historial
        )
        self.main_ui.btnMenuProductos.clicked.connect(
            self.abrir_menu_productos
        )
        self.main_ui.btnMenuVentas.clicked.connect(
            self.abrir_menu_ventas
        )
        self.main_ui.btnMenuCCorriente.clicked.connect(
            self.abrir_menu_ccorriente
        )

        # Movimiento en stacked de ventas
        self.main_ui.btnVolverAVenta.clicked.connect(
            self.ir_nueva_venta
        )
        self.main_ui.btnConsultaVentas.clicked.connect(
            self.ir_consulta_ventas
        )


        ######################################################################
        # Configuracion de modelos
        ######################################################################
        # Definición tabla cuenta corriente
        self.model_cc = QStandardItemModel()
        self.model_cc.setHorizontalHeaderLabels(
            [
                'id', 
                'Cliente', 
                'Fecha', 
                'Operación', 
                'Monto Operación', 
                'Deuda pendiente'
            ]
        )
        self.main_ui.tablaCuentaCorriente.setModel(self.model_cc)
        self.main_ui.tablaCuentaCorriente.setColumnHidden(0, True)
        self.main_ui.tablaCuentaCorriente.setColumnWidth(1, 260)
        self.main_ui.tablaCuentaCorriente.setColumnWidth(2, 120)
        self.main_ui.tablaCuentaCorriente.setColumnWidth(3, 200)
        self.main_ui.tablaCuentaCorriente.setColumnWidth(4, 150)


        ######################################################################
        # Apertura ventanas secundarias
        ######################################################################
        
        # SERVICIOS
        ######################################################################
        # Abrir ventana para agregar nuevo servicio
        self.main_ui.btnNuevoServicio.clicked.connect(
            self.ventana_nuevo_servicio
        )

        # CLIENTES
        ######################################################################
        # Abrir ventana para agendar nuevo cliente
        self.main_ui.btnNuevoCliente.clicked.connect(
            self.ventana_nuevo_cliente
        )

        # PRODUCTOS
        ######################################################################
        # Abrir ventana nuevo producto
        self.main_ui.btnNuevoProducto.clicked.connect(
            self.ventana_nuevoproducto
        )


        # CUENTAS CORRIENTES
        ######################################################################
        # Asignación método carga de operación cuenta corriente
        self.main_ui.btnCargarCC.clicked.connect(
            self.cargar_operacion_cc
        )

        self.main_ui.btnEliminarUltimaCC.clicked.connect(
            self.eliminar_registro_cc
        )


        # TURNOS
        ######################################################################
        # Abrir ventana para agregar nuevo turno
        self.main_ui.btnNuevoTurno.clicked.connect(
            self.ventana_nuevo_turno
        )

        ######################################################################
        # Configuración de eventos
        ######################################################################
        
        # Asignación de evento para mostrar cuentas corrientes segun cliente
        self.main_ui.cmbClienteCC.currentTextChanged.connect(
            self.cargar_cuentacorriente
        )

        ######################################################################
        # Llenado comboboxs
        ######################################################################
        
        # Modulo de cuenta corriente
        self.llenar_cmb_clientescc()


    ##########################################################################
    # Movimiento entre menú principal
    ##########################################################################

    def ir_menu_principal(self):
        self.main_ui.StackedWidget.setCurrentIndex(6)

    def abrir_menu_clientes(self):
        self.main_ui.StackedWidget.setCurrentIndex(7)
        self.main_ui.lineEditCliente.setFocus()

    def abrir_menu_servicios(self):
        self.main_ui.StackedWidget.setCurrentIndex(0)
    
    def abrir_menu_turnos(self):
        self.main_ui.StackedWidget.setCurrentIndex(1)
    
    def abrir_menu_historial(self):
        self.main_ui.StackedWidget.setCurrentIndex(5)
    
    def abrir_menu_productos(self):
        self.main_ui.StackedWidget.setCurrentIndex(4)
        self.main_ui.txtCodigoProd.setFocus()
    
    def abrir_menu_ventas(self):
        self.main_ui.StackedWidget.setCurrentIndex(2)
        self.main_ui.txtCodigoProdVenta.setFocus()

    def abrir_menu_ccorriente(self):
        self.main_ui.StackedWidget.setCurrentIndex(3)
    
    def ir_consulta_ventas(self):
        self.main_ui.stackedVentas.setCurrentIndex(0)
    
    def ir_nueva_venta(self):
        self.main_ui.stackedVentas.setCurrentIndex(1)


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



    ##########################################################################
    #                       MODULO CUENTA CORRIENTE                          #
    ##########################################################################
    ##########################################################################
    # Métodos configuración de ventana
    ##########################################################################
    def llenar_cmb_clientescc(self):
        ''' Método para llenar combobox de clientes en ventana de cuenta
            corriente.
        '''
        # Limpieza cmb inicial
        self.main_ui.cmbClienteCC.clear()
        
        # Seteo primer elemento del combobox
        self.main_ui.cmbClienteCC.addItem('Seleccionar cliente', None)
        # Obtención de clientes y carga en combobox
        clientes_cc = ModeloCuentaCorriente.clientes_cuentacorriente()
        if clientes_cc:
            for cliente in clientes_cc:
                self.main_ui.cmbClienteCC.addItem(cliente[1], cliente[0])
    
    ##########################################################################
    # Método carga de cuentas corriente en tabla
    ##########################################################################
    def cargar_cuentacorriente(self):
        ''' Método para cargar cuenta corriente de un determinado cliente en
            tabla.
        '''
        # Limpieza inicial de tabla
        self.model_cc.removeRows(0, self.model_cc.rowCount())

        # Seteo de self.deuda a 0 para reiniciar
        self.deuda = 0

        # Obtención de cliente seleccionado en el combobox
        cliente = self.main_ui.cmbClienteCC.currentData()

        # Obtención historial cuenta corriente de dicho cliente
        cuenta_corriente = ModeloCuentaCorriente.lista_cuentacorriente(
            cliente=cliente
        )

        # Carga de historial en tabla
        for operacion in cuenta_corriente:
            fecha = date.strftime(operacion.fecha_operacion, "%d/%m/%Y")
            fila = [
                QStandardItem(str(operacion.nro_operacion)),
                QStandardItem(operacion.cliente.nombre),
                QStandardItem(fecha),
                QStandardItem(operacion.tipo_operacion),
                QStandardItem(f'$ {operacion.monto_operacion:.0f}'),
                QStandardItem(f'$ {operacion.monto_pendiente:.0f}')
            ]
            # Alineado de valores
            for item in fila:
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.model_cc.appendRow(fila)
        
        # Actualización de self.deuda y visualización en label deuda total
        if cliente is not None:
            ult_fila = self.model_cc.rowCount() - 1
            self.deuda = float(self.model_cc.item(ult_fila, 5).text()[2:])
            self.main_ui.lblDeudaTotalCC.setText(
                f"Deuda total: $ {self.deuda:.0f}"
            )
        else:
            self.main_ui.lblDeudaTotalCC.setText("Deuda total: $ 0")
    
    ##########################################################################
    # Método carga operación de cuenta corriente
    ##########################################################################
    def cargar_operacion_cc(self):
        ''' Método para cargar operación de cuenta corriente. Se recupera
            cliente seleccionado, selección del tipo de operación de acuerdo a
            radiobuttons y en función del tipo de operación y monto, se carga
            el registro en base de datos y se actualiza tabla.
            Si la deuda se salda completamente, se elimina la cuenta corriente
            del cliente en cuestión.
        '''
        # Obtención cliente seleccionado en combobox
        cliente = self.main_ui.cmbClienteCC.currentData()

        # Verificación de selección de cliente
        if not cliente:
            QMessageBox.warning(
                self,
                'Cuenta Corriente',
                'Seleccionar un cliente'
            )
            return
        
        # Obtención tipo de operación de radiobuttons
        tipo_operacion = None

        if self.main_ui.rbtnSaldarCC.isChecked():
            tipo_operacion = "Abona"
        
        if self.main_ui.rbtnActualizarCC.isChecked():
            tipo_operacion = "Actualización"
        
        # Verificación de selección de tipo de operación
        if tipo_operacion is None:
            QMessageBox.warning(
                self,
                'Cuenta Corriente',
                'Seleccionar tipo de operación'
            )
            return

        # Obtención de monto de operación
        try:
            monto_operacion = float(self.main_ui.txtMontoCC.text())
        except ValueError:
            QMessageBox.warning(
                self,
                'Cuenta Corriente',
                'Revisar monto de operación'
            )
            return
        
        # Carga de operación en base de datos
        monto_adeudado = self.deuda

        if tipo_operacion == "Abona":
            deuda_total = monto_adeudado - monto_operacion
        
        if tipo_operacion == "Actualización":
            deuda_total = monto_adeudado + monto_operacion

        ModeloCuentaCorriente.nueva_cuentacorriente(
            cliente=cliente,
            fecha=date.today(),
            tipo_operacion=tipo_operacion,
            monto_operacion=monto_operacion,
            monto_pendiente=deuda_total
        )

        # Mensaje de confirmación
        QMessageBox.information(
                self,
                'Cuenta Corriente',
                'Operación cargada!'
            )
        
        # Eliminación de cuenta corriente si deuda es saldada completamente
        if deuda_total <= 0:
            ModeloCuentaCorriente.eliminar_cuentacorriente(cliente=cliente)
            self.llenar_cmb_clientescc()
            self.main_ui.lblDeudaTotalCC.setText("Deuda total: $ 0")
            self.main_ui.txtMontoCC.setText("")
        
        self.main_ui.txtMontoCC.setText("")
        self.cargar_cuentacorriente()


    ##########################################################################
    # Método eliminación registro cuenta corriente
    ##########################################################################
    def eliminar_registro_cc(self):
        ''' Método para eliminar último registro realizado en una determinada
            cuenta corriente. Se obtiene ultimo número de operación y se
            elimina.
        '''
        # Obtención última fila tabla cuenta corriente
        ultima_fila = self.model_cc.rowCount() - 1
        
        # Verificación ultima_fila > 0 (hay cuenta corriente)
        if ultima_fila < 0:
            QMessageBox.warning(
                self,
                'Cuentas Corrientes',
                'Se debe seleccionar una cuenta corriente'
            )
            return
        
        # Obtención del número de operación
        nro_operacion = self.model_cc.item(ultima_fila, 0).text()

        # Consulta y eliminación de registro
        eliminar = QMessageBox.question(
            self,
            'Cuentas corrientes',
            'Eliminar último registro?'
        )

        if eliminar == QMessageBox.Yes:
            ModeloCuentaCorriente.eliminar_operacion(nro_operacion)
            if ultima_fila == 0:
                self.llenar_cmb_clientescc()
                self.main_ui.lblDeudaTotalCC.setText("Deuda total: $ 0")
                self.main_ui.txtMontoCC.setText("")

            QMessageBox.information(
                self,
                'Cuentas Corrientes',
                'Registro de cuenta corriente eliminado!'
            )

        # Carga de tabla
        self.cargar_cuentacorriente()