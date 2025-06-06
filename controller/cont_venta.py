##############################################################################
# Importaciones
##############################################################################

from typing import TYPE_CHECKING
from datetime import date

from PySide6.QtWidgets import (
    QDialog, QMessageBox, QTableWidgetItem, QPushButton
)
from PySide6.QtCore import QObject, Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel

from view.interfaces.ventana_detalleventa import VentanaDetalleVenta
from model.modelo_venta import ModeloVentas
from model.modelo_cliente import ModeloCliente
from model.modelo_producto import ModeloProducto
from model.modelo_ccorriente import ModeloCuentaCorriente
from utils.generador_facturas import generar_factura_pdf
if TYPE_CHECKING:
    from controller.cont_principal import MainController


##############################################################################
##############################################################################
#                        CONTROLADOR PRINCIPAL VENTAS                        #
##############################################################################
##############################################################################
class VentasController(QObject):
    def __init__(self, main_controller: 'MainController'):
        super().__init__()
        self.main_controller = main_controller

        ######################################################################
        # Llamada a widgets necesarios
        ######################################################################
        # Tablas
        self.tabla_consultaventa = main_controller.main_ui.tablaConsultaVentas
        self.tabla_carrito = main_controller.main_ui.tablaCarrito

        # DateEdits
        self.consulta_desde = main_controller.main_ui.consultaVentaDesde
        self.consulta_hasta = main_controller.main_ui.ConsultaVentaHasta

        # Radiobuttons y checkbox
        self.checkbox_interes = main_controller.main_ui.checkInteres
        self.rbtn_efectivo = main_controller.main_ui.rbtnEfectivo
        self.rbtn_transf = main_controller.main_ui.rbtnTransf
        self.rbtn_tarjeta = main_controller.main_ui.rbtnTarjeta

        # Labels
        self.lbl_totalabonar = main_controller.main_ui.lblTotalAbonar
        self.lbl_totalcarrito = main_controller.main_ui.lblTotalEnCarrito
        self.lbl_descr_prod = main_controller.main_ui.lblDescripProdVenta

        # Comboboxs
        self.cmb_cliente_venta = main_controller.main_ui.cmbClienteVenta
        self.cmb_cliente_consulta = main_controller.main_ui.cmbClienteConsulta
        self.cmb_vencimiento = main_controller.main_ui.cmbVencVenta
        self.cliente_consulta = main_controller.main_ui.cmbClienteConsulta

        # Spinbox
        self.spinbox_cantidad = main_controller.main_ui.spinBoxCantidadVenta

        # Txts
        self.txt_monto_entregado = main_controller.main_ui.txtEntrega
        self.txt_interes = main_controller.main_ui.txtInteresVenta
        self.txt_precio_prod = main_controller.main_ui.txtPrecioProdVenta
        self.txt_codigo_prod = main_controller.main_ui.txtCodigoProdVenta

        # Botones
        self.btn_agregar_carrito = main_controller.main_ui.btnAgregarCarrito
        self.btn_vaciar_carrito = main_controller.main_ui.btnVaciarCarrito
        self.btn_quitar_carrito = main_controller.main_ui.btnQuitarCarrito
        self.btn_finalizar_venta = main_controller.main_ui.btnFinalizarVenta
        self.btn_consulta_venta = main_controller.main_ui.btnConsultarVenta
        self.btn_elimina_venta = main_controller.main_ui.btnEliminarVenta

        ######################################################################
        # Definición de variables iniciales
        ######################################################################
        self.modo_pago = 'Efectivo'
        self.monto_venta = 0
        self.interes = 0
        self.total_abonar = 0
        self.productos_vendidos = []

        ######################################################################
        # Inicialización de modelos y configuraciones de interfaz
        ######################################################################
        # Inicio de lineEdit Interes de venta -> False
        self.txt_interes.setEnabled(False)

        # Llenado comboboxs clientes
        self.llenar_cmb_clientes_venta()

        # Inicialización modelos de tablas
        self.configuracion_modelo_carrito()
        self.configuracion_modelo_consultaventa()


        ######################################################################
        # Configuración de eventos
        ######################################################################
        # Evento para autocompletar descripción y combobox vencimientos
        self.txt_codigo_prod.textChanged.connect(
            self.set_descripcion_y_vencimientos
        )

        # Evento para setear maximo valor en SpinBox cantidad a vender
        self.cmb_vencimiento.currentTextChanged.connect(
            self.set_cantidad_y_precio
        )

        # Asignación de evento para habilitar caja de interes
        self.checkbox_interes.checkStateChanged.connect(
            self.habilitar_interes
        )

        # Asignación de evento para actualizar monto total con interés
        self.txt_interes.textChanged.connect(
            self.actualizar_monto_con_interes
        )

        ######################################################################
        # Asignación de métodos a botones
        ######################################################################
        # Asignación método para agregar producto a carrito
        self.btn_agregar_carrito.clicked.connect(
            self.agregar_producto_carrito
        )

        # Asignación método para limpiar carrito
        self.btn_vaciar_carrito.clicked.connect(
            self.vaciar_carrito
        )

        # Asignación de método para eliminar una fila del carrito
        self.btn_quitar_carrito.clicked.connect(
            self.remover_de_carrito
        )

        # Asignación método finalización de venta
        self.btn_finalizar_venta.clicked.connect(
            self.finalizar_venta
        )

        # Asignación método consulta de ventas
        self.btn_consulta_venta.clicked.connect(
            self.cargar_ventas
        )

        # Asignación método eliminación de ventas
        self.btn_elimina_venta.clicked.connect(
            self.eliminar_venta
        )
    

    ##########################################################################
    # MÉTODOS CONFIGURACIONES DE INTERFAZ Y MODELOS

    ##########################################################################
    # Métodos para seteo de ComboBoxs
    ##########################################################################
    # Método llenado ComboBox clientes venta
    def llenar_cmb_clientes_venta(self):
        ''' Método para llenar el comboBox de clientes en interfaz de ventas
            y consulta de ventas
        '''
        # Obtención de clientes
        clientes = ModeloCliente.lista_clientes()

        # Limpieza de cmb y seteo de primer valor
        self.cmb_cliente_venta.clear()
        self.cmb_cliente_venta.addItem("Seleccionar cliente", None)
        self.cmb_cliente_venta.addItem("CLIENTE NO REGISTRADO", 0)

        self.cmb_cliente_consulta.clear()
        self.cmb_cliente_consulta.addItem("Seleccionar cliente", None)
        self.cmb_cliente_consulta.addItem("CLIENTE NO REGISTRADO", 0)

        # Carga de clientes al combobox
        for cliente in clientes:
            if cliente.nombre == "CLIENTE NO REGISTRADO":
                continue
            self.cmb_cliente_venta.addItem(cliente.nombre, cliente.id)
            self.cmb_cliente_consulta.addItem(
                cliente.nombre, cliente.id
            )


    ##########################################################################
    # Método actualización lblDescripProdVenta según código ingresado
    ##########################################################################
    def set_descripcion_y_vencimientos(self):
        ''' Método para actualizar automáticamente la descripción del producto
            a vender y llenado automático de los vencimientos correspondientes
            dependiendo del código ingresado. Se asignará a evento textChanged
            en txtCodigoProdVenta.
        '''
        # Limpieza inicial de campos
        self.lbl_descr_prod.setText("Producto: ")
        self.cmb_vencimiento.clear()

        # Obtención del código proporcionado
        codigo = self.txt_codigo_prod.text()

        # Obtención de productos con código proporcionado
        productos = ModeloProducto.listado_productos(codigo=codigo)

        # Definición de variables para evitar errores
        descripcion = ""

        # Seteo del campo descripcion y llenado de comboBox
        if productos:
            descripcion = productos[0].descripcion
            self.lbl_descr_prod.setText(
                f"Producto: {descripcion}"
            )
            # Llenado de comboBox
            for producto in productos:
                venc = date.strftime(producto.vencimiento, "%d/%m/%Y")
                self.cmb_vencimiento.addItem(venc, producto.nro_producto)


    ##########################################################################
    # Método seteo cantidad máxima y precio de producto venta
    ##########################################################################
    def set_cantidad_y_precio(self):
        ''' Método para setear la cantidad máxima en el SpinBox y el precio del
            producto de acuerdo con la selección
        '''
        # Seteo a 1 del spinbox
        self.spinbox_cantidad.setValue(1)
        
        # Obtención del número de producto en función de vencimiento elegido
        nro_producto = self.cmb_vencimiento.currentData()

        # Obtención de stock disponible y precio del producto con nro_producto
        producto = ModeloProducto.listado_productos(nro_producto=nro_producto)
        stock_disponible = producto[0].stock
        precio = producto[0].precio_unitario

        #Seteo de valor máximo en SpinBox
        self.spinbox_cantidad.setMaximum(stock_disponible)
        # Seteo campo precio
        self.txt_precio_prod.setText(f"{precio:.0f}")


    ##########################################################################
    # MÉTODOS MANEJO CARRITO DE VENTA

    ##########################################################################
    # Método configuración de modelo en tabla de carrito
    ##########################################################################
    def configuracion_modelo_carrito(self):
        self.modelo_carrito = QStandardItemModel()
        self.modelo_carrito.setHorizontalHeaderLabels(
            ['id', 'Producto', 'Precio', 'Cant', 'Subtotal']
        )
        self.tabla_carrito.setModel(self.modelo_carrito)
        self.tabla_carrito.setColumnHidden(0, True)
        self.tabla_carrito.setColumnWidth(1, 500)
        self.tabla_carrito.setColumnWidth(2, 150)


    ##########################################################################
    # Método para agregar productos a carrito de venta
    ##########################################################################
    def agregar_producto_carrito(self):
        ''' Método para agregar un producto al carrito de la venta
        '''
        # Obtención de valores para agregar a carrito
        codigo = self.txt_codigo_prod.text()
        nro_producto = self.cmb_vencimiento.currentData()
        
        if not nro_producto or codigo == "":
            QMessageBox.warning(
                self.main_controller,
                'Ventas',
                'Se debe elegir un producto'
            )
            return
        
        producto = ModeloProducto.listado_productos(nro_producto=nro_producto)
        descripcion = producto[0].descripcion

        cantidad = self.spinbox_cantidad.value()
        precio = self.txt_precio_prod.text()
        
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
            self.lbl_totalcarrito.setText(
                f"Total en carrito: $ {self.monto_venta}"
            )
            self.lbl_totalabonar.setText(
                f"Total a abonar: $ {self.monto_venta}"
            )

            # Limpieza de campos
            self.txt_codigo_prod.setText("")
            self.txt_precio_prod.setText("")

        except ValueError:
            QMessageBox.critical(
                self.main_controller,
                'Venta',
                'Verificar campos de venta'
            )


    ##########################################################################
    # Método para vaciar carrito de venta
    ##########################################################################
    def vaciar_carrito(self):
        ''' Método para eliminar todos los productos existentes dentro del
            carrito
        '''
        self.modelo_carrito.removeRows(0, self.modelo_carrito.rowCount())
        self.monto_venta = 0
        self.total_abonar = 0
        self.lbl_totalcarrito.setText("Total en carrito: $ 0.0")
        self.lbl_totalabonar.setText("Total a abonar: $ 0.0")
        self.txt_interes.setText("")


    ##########################################################################
    # Método para remover producto seleccionado del carrito
    ##########################################################################
    def remover_de_carrito(self):
        ''' Método para eliminar un producto determinado del carrito
        '''
        # Obtención de la fila a remover
        fila = self.tabla_carrito.currentIndex().row()

        # Verificación de selección de fila
        if fila == -1:
            QMessageBox.warning(
                self.main_controller,
                'Ventas',
                'Tenes que seleccionar un producto del carrito'
            )
            return

        # Obtención del subtotal correspondiente a la fila eliminada
        subtotal_fila = self.modelo_carrito.item(fila, 4).text()
        self.monto_venta -= float(subtotal_fila)
        self.total_abonar -= float(subtotal_fila)
        
        # Seteo de labels
        self.lbl_totalcarrito.setText(
            f"Total en carrito: $ {self.monto_venta}"
        )
        self.lbl_totalabonar.setText(
            f"Total a abonar: $ {self.monto_venta}"
        )

        # Eliminación de la fila del carrito
        self.modelo_carrito.removeRow(fila)


    ##########################################################################
    # MÉTODOS FINALIZACIÓN DE VENTA

    ##########################################################################
    # Método para habilitar casilla de interes
    ##########################################################################
    def habilitar_interes(self):
        ''' Método para habilitar o deshabilitar caja para ingreso de interés
            de venta
        '''
        if self.checkbox_interes.isChecked():
            self.txt_interes.setEnabled(True)
        else:
            self.txt_interes.setEnabled(False)
            self.txt_interes.setText('')
    

    ##########################################################################
    # Método para actualizar el monto total de la venta si se agrega interés
    ##########################################################################
    def actualizar_monto_con_interes(self):
        ''' Método para actualizar el monto total a abonar en caso de que se
            agregue un interés de venta.
        '''
        # Se obtiene interes ingresado
        interes = self.txt_interes.text().strip()
        if interes == "":
            interes = 0

        try:
            # Se aplica interes a total de venta y se obtiene total a abonar
            self.interes = float(interes)
            self.total_abonar = self.monto_venta + self.interes

            # Seteo de label
            self.lbl_totalabonar.setText(
                f"Total a abonar: $ {self.total_abonar}"
            )
        
        except ValueError:
            QMessageBox.warning(
                self.main_controller,
                'Venta',
                'Revisar campo interés'
            )    


    ##########################################################################
    # Método para determinar el modo de pago seleccionado
    ##########################################################################
    def modo_pago_elegido(self):
        ''' Método para devolver el texto de la selección en los radiobutton
            de modo de pago
        '''
        if self.rbtn_efectivo.isChecked():
            self.modo_pago = self.rbtn_efectivo.text()
        if self.rbtn_transf.isChecked():
            self.modo_pago = self.rbtn_transf.text()
        if self.rbtn_tarjeta.isChecked():
            self.modo_pago = self.rbtn_tarjeta.text()
        
        return self.modo_pago


    ##########################################################################
    # Método para finalizar la venta
    ##########################################################################
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
        cliente = self.cmb_cliente_venta.currentData()
        monto_venta = self.monto_venta
        modo_pago = self.modo_pago_elegido()
        interes = self.interes
        monto_entregado = self.txt_monto_entregado.text()

        # Verificación formato de monto_entregado
        try:
            monto_entregado = float(monto_entregado)
        except ValueError:
            QMessageBox.warning(
                self.main_controller,
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

        # Verificación monto entregado
        if monto_entregado > self.total_abonar:
            QMessageBox.information(
                self.main_controller,
                'Venta',
                'El monto abonado es mayor al monto de venta'
            )
            return

        # Obtención de productos vendidos de la tabla de carrito
        filas = self.modelo_carrito.rowCount()

        # Verificación de que hay productos en el carrito
        if filas == 0:
            QMessageBox.warning(
                self.main_controller,
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
                self.main_controller.cc_controller.llenar_cmb_clientescc()

                # Actualización dinero en calle
                self.main_controller.cc_controller.ver_dinero_calle()

            # Mensaje de confirmación de venta generada
            if monto_entregado < self.total_abonar:
                mensaje = 'Venta y deuda cargadas !'
            else:
                mensaje = 'Venta cargada!'
            QMessageBox.information(
                self.main_controller,
                'Ventas',
                f'{mensaje}'
            )

        except Exception:
            QMessageBox.critical(
                self.main_controller,
                'Ventas',
                'No se pudo cargar la venta, intenta nuevamente'
            )
            self.productos_vendidos = []
            return

        # Seteo de valores a su estado inicial
        self.vaciar_carrito()
        self.interes = 0
        self.productos_vendidos = []
        self.cmb_cliente_venta.setCurrentIndex(0)
        self.txt_monto_entregado.setText("")
        self.checkbox_interes.setChecked(False)

        # Actualización listado productos
        self.main_controller.producto_controller.cargar_productos()


    ##########################################################################
    # MÉTODOS MANEJO CONSULTA DE VENTAS

    ##########################################################################
    # Método configuración de modelo en tabla consulta de ventas
    ##########################################################################
    def configuracion_modelo_consultaventa(self):
    # Definición de tabla consulta de ventas
        self.modelo_cventa = self.tabla_consultaventa
        self.modelo_cventa.setColumnCount(8)
        self.modelo_cventa.setHorizontalHeaderLabels(
            [   'id',
                'Fecha',
                'Cliente',
                'Modo Pago',
                'Monto', 
                'Interes',
                'Total',
                'Detalle' ]
        )
        self.modelo_cventa.setColumnHidden(0,True)
        self.modelo_cventa.setColumnWidth(1,100)
        self.modelo_cventa.setColumnWidth(2,250)
        self.modelo_cventa.setColumnWidth(3,130)
        self.modelo_cventa.setColumnWidth(4,100)
        self.modelo_cventa.setColumnWidth(5,80)
        self.modelo_cventa.setColumnWidth(6,100)



    ##########################################################################
    # Método para cargar ventas en tablaConsultaVenta
    ##########################################################################
    def cargar_ventas(self):
        ''' Método para cargar las ventas en la tabla de consulta de ventas,
            se obtienen entradas de usuario para fechas y cliente para obtener
            las ventas correspondientes.
            Se recorren dichas ventas con un bucle para cargar los valores en
            la tabla.
        '''
        # Obtención de fechas y/o cliente
        fecha_desde_qt = self.consulta_desde.date()
        fecha_hasta_qt = self.consulta_hasta.date()
        cliente = self.cliente_consulta.currentData()

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
        self.modelo_cventa.setRowCount(len(ventas))

        # Bucle para recorrer ventas y cargar en tabla
        for i, venta in enumerate(ventas):
            fecha = date.strftime(venta.fecha_venta, "%d/%m/%Y")
            total_venta = venta.monto_total + venta.interes

            if venta.cliente == None:
                cliente_venta = 'CLIENTE NO REGISTRADO'
            else:
                cliente_venta = venta.cliente.nombre

            # Posicionamiento de valores en filas y columnas
            self.modelo_cventa.setItem(
                i, 0, QTableWidgetItem(str(venta.nro_venta))
            )
            self.modelo_cventa.setItem(i, 1, QTableWidgetItem(fecha))
            self.modelo_cventa.setItem(i, 2, QTableWidgetItem(cliente_venta))
            self.modelo_cventa.setItem(i, 3, QTableWidgetItem(venta.modo_pago))
            self.modelo_cventa.setItem(
                i, 4, QTableWidgetItem(f'$ {venta.monto_total:.0f}')
            )
            self.modelo_cventa.setItem(
                i, 5, QTableWidgetItem(f'$ {venta.interes:.0f}')
            )
            self.modelo_cventa.setItem(
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
                nro_venta=venta.nro_venta:self.main_controller.ventana_detalleventa(nro_venta)
            )
            self.modelo_cventa.setCellWidget(i, 7, btn)


    ##########################################################################
    # Método para eliminar ventas
    ##########################################################################
    def eliminar_venta(self):
        ''' Método para eliminar una determinada venta seleccionada en la
            tabla de consulta de ventas.
            Se obtiene aquella fila seleccionada, se obtiene el nro_venta
            y se elimina dicho registro de la base de datos y se actualiza la
            tabla.
        '''
        # Obtención de la fila seleccionada
        fila = self.modelo_cventa.currentIndex().row()

        if fila == -1:
            QMessageBox.warning(
                self.main_controller,
                'Consulta de ventas',
                'Tenes que elegir una venta'
            )
            return

        # Obtención del número de venta y cliente
        nro_venta = int(self.modelo_cventa.item(fila, 0).text())
        cliente = self.modelo_cventa.item(fila, 2).text()

        # Consulta de eliminación
        eliminacion = QMessageBox.question(
            self.main_controller,
            'Eliminar Venta',
            f'Eliminar venta de {cliente}?'
        )
        if eliminacion == QMessageBox.Yes:
            # Consulta devolución de stock
            devolucion = QMessageBox.question(
                self.main_controller,
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
                self.main_controller,
                'Ventas',
                'Venta eliminada!'
            )



##############################################################################
##############################################################################
#                   CONTROLADOR VENTANA DETALLE VENTAS                       #
##############################################################################
##############################################################################

class DetalleVentaController(QDialog):

    def __init__(self, main_controller: 'MainController', nro_venta: int):
        super().__init__()
        self.ui_detalleventa = VentanaDetalleVenta()
        self.ui_detalleventa.setupUi(self)
        self.main_controller = main_controller
        self.nro_venta = nro_venta

        ######################################################################
        # Llamada a widgets necesarios
        ######################################################################
        self.btn_generar_factura = self.ui_detalleventa.btnGenFactura
        self.tabla_detalle = self.ui_detalleventa.tablaDetalleVenta
        self.lbl_titulo = self.ui_detalleventa.lblTitulo
        self.lbl_total_productos = self.ui_detalleventa.lblTotalProductos
        self.lbl_total_pagar = self.ui_detalleventa.lblTotalAbonar
        self.lbl_interes = self.ui_detalleventa.lblTotalInteres

        ######################################################################
        # Inicialización de modelos y configuraciones iniciales
        ######################################################################
        # Inicialización modelo tabla detalle de ventas
        self.configuracion_modelo_detalleventa()

        # Inicialización de la ventana detalle venta con venta correspondiente
        self.cargar_detalle_venta(nro_venta=nro_venta)

        ######################################################################
        # Asignación de métodos a botones
        ######################################################################
        # Asignación método generación de facturas pdf
        self.btn_generar_factura.clicked.connect(self.imprimir_factura)


    ##########################################################################
    # Configuración modelo en tabla detalle de ventas
    ##########################################################################
    def configuracion_modelo_detalleventa(self):
        self.modelo_dventa = QStandardItemModel()
        self.modelo_dventa.setHorizontalHeaderLabels(
            ['id','Producto','Precio', 'Cantidad', 'Subtotal']
        )
        self.tabla_detalle.setModel(self.modelo_dventa)
        self.tabla_detalle.setColumnHidden(0, True)
        self.tabla_detalle.setColumnWidth(1, 490)
        self.tabla_detalle.setColumnWidth(2,100)
        self.tabla_detalle.setColumnWidth(3,80)


    ##########################################################################
    # Método para cargar el detalle de venta seleccionado en consulta venta
    ##########################################################################
    def cargar_detalle_venta(self, nro_venta: int):
        # Se busca el detalle de venta segun nro_venta
        detalle = ModeloVentas.consulta_detalleventa(nro_venta=nro_venta)

        # Se pone número de venta en título
        self.lbl_titulo.setText(f"Detalle de venta #{nro_venta}")

        # Completado de información de venta en lables
        total_prod = detalle[0].venta.monto_total
        interes = detalle[0].venta.interes
        tot_abonar = total_prod + interes
        self.lbl_total_productos.setText(
            f"Total productos: $ {total_prod}"
        )
        self.lbl_interes.setText(f'Interes: $ {interes}')
        self.lbl_total_pagar.setText(
            f"Total a abonar: $ {tot_abonar}"
        )

        # Se carga información a la tabla de detalle venta
        for det in detalle:
            producto = det.producto.descripcion
            precio = det.precio_unitario
            cantidad = det.cantidad
            subtotal = precio * cantidad

            fila = [
                QStandardItem(det.nro_venta),
                QStandardItem(producto),
                QStandardItem(f'$ {precio:.0f}'),
                QStandardItem(str(cantidad)),
                QStandardItem(f'$ {subtotal:.0f}')
            ]

            self.modelo_dventa.appendRow(fila)


    ##########################################################################
    # Método para generación de factura pdf venta nro_venta
    ##########################################################################
    def imprimir_factura(self):
        ''' Método para generar generar la factura PDF de la compra que se ha
            seleccionado desde la tabla consulta de ventas.
        '''
        # Obtención detalle de ventas
        detalle = ModeloVentas.consulta_detalleventa(nro_venta=self.nro_venta)

        # Armado lista productos para pasar parametro a función
        productos = []

        for det in detalle:
            nombre_producto = det.producto.descripcion
            precio = det.precio_unitario
            cantidad = det.cantidad
            subtotal = precio * cantidad

            productos.append([  nombre_producto,
                                f'$ {precio:.0f}', 
                                cantidad, 
                                f'$ {subtotal:.0f}'
                            ])
        
        # Obtención informacion de venta
        venta = ModeloVentas.obtener_venta(nro_venta=self.nro_venta)
        if venta:
            cliente = venta.cliente.nombre
            fecha = venta.fecha_venta
            total = venta.monto_total
            interes = venta.interes
        
        # Generación de factura PDF
        generar_factura_pdf(
            cliente=cliente,
            productos=productos,
            total=total,
            nro_factura=self.nro_venta,
            fecha=fecha,
            interes=interes
        )

        # Bloqueo de botón
        self.btn_generar_factura.setEnabled(False)