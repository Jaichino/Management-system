##############################################################################
# Importaciones
##############################################################################

from datetime import datetime, date, time, timedelta
from PySide6.QtWidgets import (
    QMainWindow, QSpacerItem, QSizePolicy, QMessageBox, QTableWidgetItem,
    QPushButton
)
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import QDate, Qt

from view.interfaces.ventana_principal import VentanaPrincipal
from model.modelo_cliente import ModeloCliente
from model.modelo_servicio import ModeloServicio
from model.modelo_turno import ModeloTurno
from model.modelo_producto import ModeloProducto
from model.modelo_venta import ModeloVentas
from model.modelo_ccorriente import ModeloCuentaCorriente

from controller.cont_clientes import ClienteController, NuevoClienteController
from controller.cont_servicios import (
    ServicioController, TarjetaServiciosController
)
from controller.cont_turnos import (
    TurnoController, TarjetaTurnosController
)
from controller.cont_producto import (
    ProductoController, NuevoProductoController
)
from controller.cont_venta import DetalleVentaController

from utils.generador_facturas import generar_factura_pdf


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

        self.producto_controller = ProductoController(self)
        self.cliente_controller = ClienteController(self)

        ######################################################################
        # Variables iniciales
        ######################################################################
    
        self.modo_pago = 'Efectivo'
        self.monto_venta = 0
        self.interes = 0
        self.total_abonar = 0
        self.productos_vendidos = []
        
        self.deuda = 0


        ######################################################################
        # Configuraciones interfaz
        ######################################################################

        # Inicio de lineEdit Interes de venta -> False
        self.main_ui.txtInteresVenta.setEnabled(False)

        # Seteo del calendarWidget
        self.main_ui.calendarWidget.setCurrentPage(
            QDate.currentDate().year(),
            QDate.currentDate().month()
        )
        self.main_ui.calendarWidget.setSelectedDate(datetime.now())

        # Que siempre arranque mostrando los turnos del día actual
        self.agregar_turnos(date.today())

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
        
        # Definición de modelo en tabla Carrito de venta
        self.modelo_carrito = QStandardItemModel()
        self.modelo_carrito.setHorizontalHeaderLabels(
            ['id', 'Producto', 'Precio', 'Cant', 'Subtotal']
        )
        self.main_ui.tablaCarrito.setModel(self.modelo_carrito)
        self.main_ui.tablaCarrito.setColumnHidden(0, True)
        self.main_ui.tablaCarrito.setColumnWidth(1, 500)
        self.main_ui.tablaCarrito.setColumnWidth(2, 150)


        # Definición de tabla consulta de ventas
        self.tabla_cventa = self.main_ui.tablaConsultaVentas
        self.tabla_cventa.setColumnCount(8)
        self.tabla_cventa.setHorizontalHeaderLabels(
            [   'id',
                'Fecha',
                'Cliente',
                'Modo Pago',
                'Monto', 
                'Interes',
                'Total',
                'Detalle' ]
        )
        self.tabla_cventa.setColumnHidden(0,True)
        self.tabla_cventa.setColumnWidth(1,100)
        self.tabla_cventa.setColumnWidth(2,250)
        self.tabla_cventa.setColumnWidth(3,130)
        self.tabla_cventa.setColumnWidth(4,100)
        self.tabla_cventa.setColumnWidth(5,80)
        self.tabla_cventa.setColumnWidth(6,100)


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
        # Asignaciones de métodos a botones
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
        # Abrir ventana nuevo producto
        self.main_ui.btnNuevoProducto.clicked.connect(
            self.ventana_nuevoproducto
        )


        # VENTAS
        ######################################################################
        # Asignación método para agregar producto a carrito
        self.main_ui.btnAgregarCarrito.clicked.connect(
            self.agregar_producto_carrito
        )

        # Asignación método para limpiar carrito
        self.main_ui.btnVaciarCarrito.clicked.connect(
            self.vaciar_carrito
        )

        # Asignación de método para eliminar una fila del carrito
        self.main_ui.btnQuitarCarrito.clicked.connect(
            self.remover_de_carrito
        )

        # Asignación método finalización de venta
        self.main_ui.btnFinalizarVenta.clicked.connect(
            self.finalizar_venta
        )

        # Asignación método consulta de ventas
        self.main_ui.btnConsultarVenta.clicked.connect(
            self.cargar_ventas
        )

        # Asignación método eliminación de ventas
        self.main_ui.btnEliminarVenta.clicked.connect(
            self.eliminar_venta
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

        # Asignación método para mostrar historial de turnos por cliente
        self.main_ui.btnBuscarHist.clicked.connect(
            self.carga_historial
        )


        ######################################################################
        # Configuración de eventos
        ######################################################################
        # Evento para autocompletar descripción y combobox vencimientos
        self.main_ui.txtCodigoProdVenta.textChanged.connect(
            self.set_descripcion_y_vencimientos
        )

        # Evento para setear maximo valor en SpinBox cantidad a vender
        self.main_ui.cmbVencVenta.currentTextChanged.connect(
            self.set_cantidad_y_precio
        )

        # Asignación de evento para mostrar tarjetas de turnos segun fecha
        self.main_ui.calendarWidget.selectionChanged.connect(
            self.actualizar_turnos
        )

        # Asignación de evento para habilitar caja de interes
        self.main_ui.checkInteres.checkStateChanged.connect(
            self.habilitar_interes
        )

        # Asignación de evento para actualizar monto total con interés
        self.main_ui.txtInteresVenta.textChanged.connect(
            self.actualizar_monto_con_interes
        )

        # Asignación de evento para mostrar cuentas corrientes segun cliente
        self.main_ui.cmbClienteCC.currentTextChanged.connect(
            self.cargar_cuentacorriente
        )

        ######################################################################
        # Llenado comboboxs
        ######################################################################
        
        # Modulo de turnos
        self.llenar_cmb_clientes()
        self.llenar_cmb_servicios()
        
        # Modulo de ventas
        self.llenar_cmb_clientes_venta()

        # Modulo de cuenta corriente
        self.llenar_cmb_clientescc()


        ######################################################################
        # Llamadas para agregar tarjetas de servicios
        ######################################################################
        # Visualización tarjetas de servicios
        self.mostrar_servicios()


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
        self.abrir_nuevo_servicio = ServicioController(self)
        self.abrir_nuevo_servicio.show()

    # Apertura ventana nuevo turno
    def ventana_nuevo_turno(self):
        self.abrir_nuevo_turno = TurnoController(self)
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
    #                            MODULO VENTAS                               #
    ##########################################################################
    ##########################################################################
    # Métodos para seteo de ComboBoxs y lineEdits
    ##########################################################################
    # Método llenado ComboBox clientes venta
    def llenar_cmb_clientes_venta(self):
        ''' Método para llenar el comboBox de clientes en interfaz de ventas
            y consulta de ventas
        '''
        # Obtención de clientes
        clientes = ModeloCliente.lista_clientes()

        # Limpieza de cmb y seteo de primer valor
        self.main_ui.cmbClienteVenta.clear()
        self.main_ui.cmbClienteVenta.addItem("Seleccionar cliente", None)
        self.main_ui.cmbClienteVenta.addItem("CLIENTE NO REGISTRADO", 0)

        self.main_ui.cmbClienteConsulta.clear()
        self.main_ui.cmbClienteConsulta.addItem("Seleccionar cliente", None)
        self.main_ui.cmbClienteConsulta.addItem("CLIENTE NO REGISTRADO", 0)

        # Carga de clientes al combobox
        for cliente in clientes:
            if cliente.nombre == "CLIENTE NO REGISTRADO":
                continue
            self.main_ui.cmbClienteVenta.addItem(cliente.nombre, cliente.id)
            self.main_ui.cmbClienteConsulta.addItem(
                cliente.nombre, cliente.id
            )


    # Método actualización lblDescripProdVenta según código
    def set_descripcion_y_vencimientos(self):
        ''' Método para actualizar automáticamente la descripción del producto
            a vender y llenado automático de los vencimientos correspondientes
            dependiendo del código ingresado. Se asignará a evento textChanged
            en txtCodigoProdVenta.
        '''
        # Limpieza inicial de campos
        self.main_ui.lblDescripProdVenta.setText("Producto: ")
        self.main_ui.cmbVencVenta.clear()

        # Obtención del código proporcionado
        codigo = self.main_ui.txtCodigoProdVenta.text()

        # Obtención de productos con código proporcionado
        productos = ModeloProducto.listado_productos(codigo=codigo)

        # Definición de variables para evitar errores
        descripcion = ""

        # Seteo del campo descripcion y llenado de comboBox
        if productos:
            descripcion = productos[0].descripcion
            self.main_ui.lblDescripProdVenta.setText(
                f"Producto: {descripcion}"
            )
            # Llenado de comboBox
            for producto in productos:
                venc = date.strftime(producto.vencimiento, "%d/%m/%Y")
                self.main_ui.cmbVencVenta.addItem(venc, producto.nro_producto)


    def set_cantidad_y_precio(self):
        ''' Método para setear la cantidad máxima en el SpinBox y el precio del
            producto de acuerdo con la selección
        '''
        # Seteo a 1 del spinbox
        self.main_ui.spinBoxCantidadVenta.setValue(1)
        
        # Obtención del número de producto en función de vencimiento elegido
        nro_producto = self.main_ui.cmbVencVenta.currentData()

        # Obtención de stock disponible y precio del producto con nro_producto
        producto = ModeloProducto.listado_productos(nro_producto=nro_producto)
        stock_disponible = producto[0].stock
        precio = producto[0].precio_unitario

        #Seteo de valor máximo en SpinBox
        self.main_ui.spinBoxCantidadVenta.setMaximum(stock_disponible)
        # Seteo campo precio
        self.main_ui.txtPrecioProdVenta.setText(f"{precio:.0f}")


    ##########################################################################
    # Métodos manejo del carrito de compra
    ##########################################################################
    def agregar_producto_carrito(self):
        ''' Método para agregar un producto al carrito de la venta
        '''
        # Obtención de valores para agregar a carrito
        codigo = self.main_ui.txtCodigoProdVenta.text()
        nro_producto = self.main_ui.cmbVencVenta.currentData()
        
        if not nro_producto or codigo == "":
            QMessageBox.warning(
                self,
                'Ventas',
                'Se debe elegir un producto'
            )
            return
        
        producto = ModeloProducto.listado_productos(nro_producto=nro_producto)
        descripcion = producto[0].descripcion

        cantidad = self.main_ui.spinBoxCantidadVenta.value()
        precio = self.main_ui.txtPrecioProdVenta.text()
        
        try:
            # Verificación de formatos y calculo de subtotal
            cantidad = int(cantidad)
            precio = float(precio)

            subtotal = cantidad * precio

            # Armado de fila para agregar a modelo
            fila_carrito = [
                QStandardItem(str(nro_producto)),
                QStandardItem(descripcion),
                QStandardItem(str(precio)),
                QStandardItem(str(cantidad)),
                QStandardItem(str(subtotal))
            ]
            # Se agrega fila al carrito
            self.modelo_carrito.appendRow(fila_carrito)

            # Ajuste de monto total de venta y actualización de label
            self.monto_venta += subtotal
            self.total_abonar = self.monto_venta
            self.main_ui.lblTotalEnCarrito.setText(f"Total en carrito: $ {self.monto_venta}")
            self.main_ui.lblTotalAbonar.setText(f"Total a abonar: $ {self.monto_venta}")

            # Limpieza de campos
            self.main_ui.txtCodigoProdVenta.setText("")
            self.main_ui.txtPrecioProdVenta.setText("")

        except ValueError:
            QMessageBox.critical(
                self,
                'Venta',
                'Verificar campos de venta'
            )


    def vaciar_carrito(self):
        ''' Método para eliminar todos los productos existentes dentro del
            carrito
        '''
        self.modelo_carrito.removeRows(0, self.modelo_carrito.rowCount())
        self.monto_venta = 0
        self.total_abonar = 0
        self.main_ui.lblTotalEnCarrito.setText("Total en carrito: $ 0.0")
        self.main_ui.lblTotalAbonar.setText("Total a abonar: $ 0.0")
        self.main_ui.txtInteresVenta.setText("")


    def remover_de_carrito(self):
        ''' Método para eliminar un producto determinado del carrito
        '''
        # Obtención de la fila a remover
        fila = self.main_ui.tablaCarrito.currentIndex().row()

        # Verificación de selección de fila
        if fila == -1:
            QMessageBox.warning(
                self,
                'Ventas',
                'Tenes que seleccionar una fila del carrito'
            )
            return

        # Obtención del subtotal correspondiente a la fila eliminada
        subtotal_fila = self.modelo_carrito.item(fila, 4).text()
        self.monto_venta -= float(subtotal_fila)
        self.total_abonar -= float(subtotal_fila)
        
        # Seteo de labels
        self.main_ui.lblTotalEnCarrito.setText(
            f"Total en carrito: $ {self.monto_venta}"
        )
        self.main_ui.lblTotalAbonar.setText(
            f"Total a abonar: $ {self.monto_venta}"
        )

        # Eliminación de la fila del carrito
        self.modelo_carrito.removeRow(fila)


    ##########################################################################
    # Métodos para finalización de venta
    ##########################################################################
    # Método para habilitar casilla de interes
    def habilitar_interes(self):
        ''' Método para habilitar o deshabilitar caja para ingreso de interés
            de venta
        '''
        if self.main_ui.checkInteres.isChecked():
            self.main_ui.txtInteresVenta.setEnabled(True)
        else:
            self.main_ui.txtInteresVenta.setEnabled(False)
            self.main_ui.txtInteresVenta.setText('')


    # Método para actualizar el monto total de la venta si se agrega interés
    def actualizar_monto_con_interes(self):
        ''' Método para actualizar el monto total a abonar en caso de que se
            agregue un interés de venta.
        '''
        # Se obtiene interes ingresado
        interes = self.main_ui.txtInteresVenta.text().strip()
        if interes == "":
            interes = 0

        try:
            # Se aplica interes a total de venta y se obtiene total a abonar
            self.interes = float(interes)
            self.total_abonar = self.monto_venta + self.interes

            # Seteo de label
            self.main_ui.lblTotalAbonar.setText(
                f"Total a abonar: $ {self.total_abonar}"
            )
        
        except ValueError:
            QMessageBox.warning(
                self,
                'Venta',
                'Revisar campo interés'
            )
    

    # Método para determinar el modo de pago seleccionado
    def modo_pago_elegido(self):
        ''' Método para devolver el texto de la selección en los radiobutton
            de modo de pago
        '''
        if self.main_ui.rbtnEfectivo.isChecked():
            self.modo_pago = self.main_ui.rbtnEfectivo.text()
        if self.main_ui.rbtnTransf.isChecked():
            self.modo_pago = self.main_ui.rbtnTransf.text()
        if self.main_ui.rbtnTarjeta.isChecked():
            self.modo_pago = self.main_ui.rbtnTarjeta.text()
        
        return self.modo_pago


    # Método para finalizar la venta
    def finalizar_venta(self):
        ''' Método para finalizar una venta determinada.
            Se obtienen las entradas de usuario, se recuperan los productos
            agregados al carrito y se procede a cargar la venta, el detalle
            de venta, descontar del stock de productos aquellos que fueron
            vendidos y, en caso de que no se pague la totalidad del monto de
            venta, se carga deuda en cuenta corriente
        '''
        # Obtención información de venta
        fecha_venta = date.today()
        cliente = self.main_ui.cmbClienteVenta.currentData()
        monto_venta = self.monto_venta
        modo_pago = self.modo_pago_elegido()
        interes = self.interes
        monto_entregado = self.main_ui.txtEntrega.text()

        # Verificación formato de monto_entregado
        try:
            monto_entregado = float(monto_entregado)
        except ValueError:
            QMessageBox.warning(
                self,
                'Venta',
                'Revisar campos de venta'
            )
            return

        # Verificación selección de cliente
        if cliente is None:
            QMessageBox.warning(
                self,
                'Ventas',
                'Se debe seleccionar un cliente'
            )
            return
        
        print(self.monto_venta)
        print(self.interes)
        print(self.total_abonar)

        # Verificación monto entregado
        if monto_entregado > self.total_abonar:
            QMessageBox.information(
                self,
                'Venta',
                'El monto abonado es mayor al monto de venta'
            )
            return

        # Obtención de productos vendidos de la tabla de carrito
        filas = self.modelo_carrito.rowCount()

        # Verificación de que hay productos en el carrito
        if filas == 0:
            QMessageBox.warning(
                self,
                'Ventas',
                'No hay productos en el carrito'
            )
            return
        
        # Guardado de productos del carrito en lista
        for fila in range(filas):
            nro_producto = self.modelo_carrito.index(fila, 0).data()
            cantidad = self.modelo_carrito.index(fila, 3).data()
            precio = self.modelo_carrito.index(fila, 2).data()

            self.productos_vendidos.append({
                'nro_producto':int(nro_producto),
                'cantidad': int(cantidad),
                'precio_unitario': float(precio)
            })

        try:
            # Generación de la venta
            ModeloVentas.nueva_venta(
                fecha=fecha_venta,
                cliente=cliente,
                monto_total=monto_venta,
                modo_pago=modo_pago,
                interes=interes,
                productos=self.productos_vendidos
            )

            # Si el monto abonado es menor al monto de venta, se carga CC
            if monto_entregado < self.total_abonar:
                cc_cliente = ModeloCuentaCorriente.lista_cuentacorriente(
                    cliente
                )

                if cc_cliente:
                    deuda_anterior = cc_cliente[-1].monto_pendiente
                else:
                    deuda_anterior = 0

                deuda_venta = self.total_abonar - monto_entregado

                ModeloCuentaCorriente.nueva_cuentacorriente(
                    cliente=cliente,
                    fecha=fecha_venta,
                    tipo_operacion='Adeuda',
                    monto_operacion=monto_entregado,
                    monto_pendiente= deuda_anterior + deuda_venta
                )

                # Actualización cmb clientes cc
                self.llenar_cmb_clientescc()

            # Mensaje de confirmación de venta generada
            if monto_entregado < self.total_abonar:
                mensaje = 'Venta y deuda cargadas !'
            else:
                mensaje = 'Venta cargada!'
            QMessageBox.information(
                self,
                'Ventas',
                f'{mensaje}'
            )

        except Exception:
            QMessageBox.critical(
                self,
                'Ventas',
                'No se pudo cargar la venta, intenta nuevamente'
            )
            self.productos_vendidos = []
            return

        # Seteo de valores a su estado inicial
        self.vaciar_carrito()
        self.interes = 0
        self.productos_vendidos = []
        self.main_ui.cmbClienteVenta.setCurrentIndex(0)
        self.main_ui.txtEntrega.setText("")
        self.main_ui.checkInteres.setChecked(False)
        # Actualización listado productos
        self.cargar_productos()
    

    ##########################################################################
    # Métodos para manejo de interfaz consulta de ventas
    ##########################################################################
    # Método para cargar ventas en tablaConsultaVenta
    def cargar_ventas(self):
        ''' Método para cargar las ventas en la tabla de consulta de ventas,
            se obtienen entradas de usuario para fechas y cliente para obtener
            las ventas correspondientes.
            Se recorren dichas ventas con un bucle para cargar los valores en
            la tabla.
        '''
        # Obtención de fechas y/o cliente
        fecha_desde_qt = self.main_ui.consultaVentaDesde.date()
        fecha_hasta_qt = self.main_ui.ConsultaVentaHasta.date()
        cliente = self.main_ui.cmbClienteConsulta.currentData()

        # Formateo de fechasQt a date()
        fecha_desde = date(
            year=fecha_desde_qt.year(),
            month=fecha_desde_qt.month(),
            day=fecha_desde_qt.day()
        )
        fecha_hasta = date(
            year=fecha_hasta_qt.year(),
            month=fecha_hasta_qt.month(),
            day=fecha_hasta_qt.day()
        )

        # Obtención de ventas
        ventas = ModeloVentas.listado_ventas(
            desde=fecha_desde, hasta=fecha_hasta, cliente=cliente
        )

        # Carga de ventas en la tabla
        self.tabla_cventa.setRowCount(len(ventas))

        # Bucle para recorrer ventas y cargar en tabla
        for i, venta in enumerate(ventas):
            fecha = date.strftime(venta.fecha_venta, "%d/%m/%Y")
            total_venta = venta.monto_total + venta.interes

            if venta.cliente == None:
                cliente_venta = 'CLIENTE NO REGISTRADO'
            else:
                cliente_venta = venta.cliente.nombre

            # Posicionamiento de valores en filas y columnas
            self.tabla_cventa.setItem(
                i, 0, QTableWidgetItem(str(venta.nro_venta))
            )
            self.tabla_cventa.setItem(i, 1, QTableWidgetItem(fecha))
            self.tabla_cventa.setItem(i, 2, QTableWidgetItem(cliente_venta))
            self.tabla_cventa.setItem(i, 3, QTableWidgetItem(venta.modo_pago))
            self.tabla_cventa.setItem(
                i, 4, QTableWidgetItem(f'$ {venta.monto_total:.0f}')
            )
            self.tabla_cventa.setItem(
                i, 5, QTableWidgetItem(f'$ {venta.interes:.0f}')
            )
            self.tabla_cventa.setItem(
                i, 6, QTableWidgetItem(f'$ {total_venta:.0f}')
            )

            # Creación de botón en ultima columna
            btn = QPushButton("Ver")
            btn.setStyleSheet(
                ''' QPushButton {
                                color: #7D3928;
                                font-size: 12pt
                                }
                    QPushButton:hover {
                                font-weight: bold;
                                color: #7D3928;
                                background-color: #F7E0D3;
                                }
                '''
            )
            btn.setCursor(Qt.PointingHandCursor)
            # Se conecta boton a método para mostrar detalle de ventas
            btn.clicked.connect(
                lambda _, 
                nro_venta=venta.nro_venta:self.ventana_detalleventa(nro_venta)
            )
            self.tabla_cventa.setCellWidget(i, 7, btn)


    # Método para eliminar ventas
    def eliminar_venta(self):
        ''' Método para eliminar una determinada venta seleccionada en la
            tabla de consulta de ventas.
            Se obtiene aquella fila seleccionada, se obtiene el nro_venta
            y se elimina dicho registro de la base de datos y se actualiza la
            tabla.
        '''
        # Obtención de la fila seleccionada
        fila = self.tabla_cventa.currentIndex().row()

        # Obtención del número de venta y cliente
        nro_venta = int(self.tabla_cventa.item(fila, 0).text())
        cliente = self.tabla_cventa.item(fila, 2).text()

        # Consulta de eliminación
        eliminacion = QMessageBox.question(
            self,
            'Eliminar Venta',
            f'Eliminar venta de {cliente}?'
        )
        if eliminacion == QMessageBox.Yes:
            # Consulta devolución de stock
            devolucion = QMessageBox.question(
                self,
                'Eliminar Venta',
                f'Devolver productos vendidos al stock?'
            )

            if devolucion == QMessageBox.Yes:
                # Eliminación y devolución de productos
                ModeloVentas.eliminar_venta(
                    nro_venta=nro_venta, dev_stock=True
            )
            
            else:
                # Eliminación de registro en base de datos
                ModeloVentas.eliminar_venta(
                    nro_venta=nro_venta, dev_stock=False
                )

            # Actualización de tabla de consulta de ventas
            self.cargar_ventas()
            QMessageBox.information(
                self,
                'Ventas',
                'Venta eliminada!'
            )



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


    ##########################################################################
    #                          MODULO SERVICIOS                              #
    ##########################################################################
    ##########################################################################
    # Posicionamiento de tarjetas de Servicios
    ##########################################################################

    def mostrar_servicios(self):

        # Definición del contenedor de las tarjetas
        contenedor = self.main_ui.contenedorServicios.layout()
        contenedor.setContentsMargins(10,10,10,10)
        contenedor.setSpacing(5)

        # Limpieza previa del contenedor
        while contenedor.count():
            item = contenedor.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        # Obtención de servicios de base de datos
        servicios = ModeloServicio.lista_servicios()
        if servicios:
            for serv in servicios:
                tarjeta = TarjetaServiciosController()
                tarjeta.widget_tserv.lblServicio.setText(
                    serv.nombre
                )
                tarjeta.widget_tserv.lblDuracion.setText(
                    f'{serv.duracion} minutos'
                )
                tarjeta.widget_tserv.lblPrecio.setText(
                    f'$ {serv.precio}'
                )
                # Asignación de método eliminar servicio
                tarjeta.widget_tserv.btnEliminarServicio.clicked.connect(
                    lambda _,id_servicio=serv.id : self.eliminar_servicio(
                        id_servicio
                    )
                )

                # Método que guarda el id asociado de cada tarjeta de servicio
                tarjeta.widget_tserv.btnEditarServicio.clicked.connect(
                    lambda _, servicio_id = serv.id : self.servicio_editar(
                        servicio_id
                    )
                )
                contenedor.addWidget(tarjeta)

            contenedor.addSpacerItem(
                QSpacerItem(20,40, QSizePolicy.Minimum, QSizePolicy.Expanding)
            )
    
    
    def eliminar_servicio(self, id_servicio):

        # Consulta de eliminación
        eliminar = QMessageBox.question(
            self,
            "Servicios",
            "Eliminar el servicio?"
        )
        if eliminar == QMessageBox.Yes:
            # Eliminación del servicio
            ModeloServicio.eliminar_servicio(id_servicio)
            QMessageBox.information(
                self,
                'Servicios',
                'Servicio Eliminado'
            )

            # Actualización del listado
            self.mostrar_servicios()
    

    def servicio_editar(self, servicio_id):
        # Se obtiene el objeto Servicio a partir del id guardado en boton
        servicio = ModeloServicio.info_servicio(servicio_id)
        # Se inicializa ventana con metodo cargar_datos
        ventana = ServicioController(self)
        ventana.cargar_datos(servicio)
        ventana.show()
        # Se debe guardar la referencia para que no se destruya la ventana
        self.ventana_servicio = ventana



    ##########################################################################
    #                               TURNOS                                   #
    ##########################################################################
    # Posicionamiento de tarjetas de Turnos
    ##########################################################################

    def agregar_turnos(self, fecha: date):
        # Se define el contenedor donde irán las tarjetas
        contenedor = self.main_ui.contenedorTurnos.layout()
        contenedor.setContentsMargins(10,10,10,10)
        contenedor.setSpacing(5)

        # Se borran widgets del layout
        while contenedor.count():
            item = contenedor.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        # Se recuperan turnos para fecha elegida
        turnos = ModeloTurno.turnos_fecha(fecha)

        for turno in turnos:
            tarjeta = TarjetaTurnosController()
            
            # Se obtiene hora de finalización
            hora_inicio = datetime.combine(datetime.today(), turno[1])
            hora_fin = hora_inicio + timedelta(minutes=turno[6])
            hora_fin_format = hora_fin.strftime("%H:%M")

            # Carga de valores en widget
            tarjeta.widget_tarjetaturno.lblCliente.setText(turno[2])
            tarjeta.widget_tarjetaturno.lblServicio.setText(turno[3])
            tarjeta.widget_tarjetaturno.lblObservacion.setText(turno[4])
            tarjeta.widget_tarjetaturno.lblHoraTurno.setText(time.strftime(turno[1],"%H:%M"))
            tarjeta.widget_tarjetaturno.lblPrecio.setText(f'$ {turno[5]}')
            tarjeta.widget_tarjetaturno.lblDuracion.setText(hora_fin_format)

            # Se captura id en botón
            tarjeta.widget_tarjetaturno.btnCancelarTurno.clicked.connect(
                lambda _, turno_id=turno[7]: self.eliminar_turno(turno_id))

            # Carga de tarjeta en contenedor
            contenedor.addWidget(tarjeta)

        contenedor.addSpacerItem(
            QSpacerItem(20,40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )


    # Método para asignar al evento de cambio de fecha en calendarWidget
    def actualizar_turnos(self):
        fecha_qdate = self.main_ui.calendarWidget.selectedDate()
        fecha = date(
            year=fecha_qdate.year(),
            month=fecha_qdate.month(),
            day=fecha_qdate.day()
        )
        self.agregar_turnos(fecha)
    
    
    # Método para eliminar turnos agendados
    def eliminar_turno(self, turno_id):
        # Se consulta si se quiere eliminar un turno
        eliminar = QMessageBox.question(
            self,
            'Turnos',
            'Queres eliminar este turno?'
        )
        if eliminar == QMessageBox.Yes:
            ModeloTurno.eliminar_turno(turno_id)
            QMessageBox.information(
            self,
            'Turnos',
            'Turno eliminado!'
            )

        # Se busca fecha seleccionada en calendario y se actualiza vista
        fecha_qt = self.main_ui.calendarWidget.selectedDate()
        fecha = date(
            year=fecha_qt.year(),
            month=fecha_qt.month(),
            day=fecha_qt.day()
        )

        self.agregar_turnos(fecha)



    ##########################################################################
    #                          HISTORIAL TURNOS                              #
    ##########################################################################
    
    ##########################################################################
    # Carga de ComboBoxs de cliente y servicios
    ##########################################################################
    def llenar_cmb_clientes(self):
        # Obtención de clientes
        clientes = ModeloTurno.clientes_con_turnos()
        # Asignación primer valor del combobox
        self.main_ui.cmbClienteHist.clear()
        self.main_ui.cmbClienteHist.addItem("Seleccionar cliente", None)
        # Asignación a combobox
        for cliente in clientes:
            self.main_ui.cmbClienteHist.addItem(cliente.nombre, cliente.id)

    def llenar_cmb_servicios(self):
        # Obtención de servicios
        servicios = ModeloServicio.lista_servicios()
        # Asignación primer valor del combobox
        self.main_ui.cmbServicioHist.clear()
        self.main_ui.cmbServicioHist.addItem("Seleccionar servicio", None)
        # Asignación a combobox
        for servicio in servicios:
            self.main_ui.cmbServicioHist.addItem(servicio.nombre, servicio.id)

    ##########################################################################
    # Carga de Historiales de tratamientos a clientes en Tabla
    ##########################################################################
    def carga_historial(self):
        # Obtención de entradas de usuario
        cliente = self.main_ui.cmbClienteHist.currentData()
        servicio = self.main_ui.cmbServicioHist.currentData()
        fecha = date.today()

        # Verificación de que cliente no es None
        if cliente == None:
            QMessageBox.critical(
                self,
                'Historial Clientes - Error',
                'Tenes que elegir un cliente !'
            )
            return
        
        # Definición del modelo para insertar datos
        self.model_thist = QStandardItemModel()
        self.model_thist.setHorizontalHeaderLabels(
            ["Turno", "Fecha Turno", "Tratamiento", "Observación"]
        )

        # Se limpia el modelo antes de cargar clientes
        self.model_thist.removeRows(0, self.model_thist.rowCount())

        # Obtención de historial
        turnos = ModeloTurno.historial_turnos(cliente=cliente, fecha=fecha, servicio=servicio)

        # Carga de datos en tabla
        for i, turno in enumerate(turnos, start=1):
            fecha_format = date.strftime(turno[0], '%d/%m/%Y')
            fila = [
                QStandardItem(str(i)),
                QStandardItem(fecha_format),
                QStandardItem(turno[2]),
                QStandardItem(turno[3])
            ]
            # Alineado de valores
            for item in fila:
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.model_thist.appendRow(fila)
        
        # Seteo del modelo a tabla y dimensiones de columnas
        self.main_ui.tablaHistorial.setModel(self.model_thist)

        self.main_ui.tablaHistorial.setColumnWidth(0,80)
        self.main_ui.tablaHistorial.setColumnWidth(1,120)
        self.main_ui.tablaHistorial.setColumnWidth(2,250)