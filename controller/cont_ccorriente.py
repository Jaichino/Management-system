##############################################################################
# Importaciones
##############################################################################

from typing import TYPE_CHECKING
from datetime import date

from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtCore import QObject, Qt

from model.modelo_ccorriente import ModeloCuentaCorriente
if TYPE_CHECKING:
    from controller.cont_principal import MainController

##############################################################################
##############################################################################
#                CONTROLADOR PRINCIPAL CUENTA CORRIENTE                      #
##############################################################################
##############################################################################

class CuentaCorrienteController(QObject):
    def __init__(self, main_controller: 'MainController'):
        super().__init__()
        self.main_controller = main_controller

        ######################################################################
        # Llamadas a widgets necesarios
        ######################################################################
        self.tabla_cc = main_controller.main_ui.tablaCuentaCorriente
        self.cmb_cliente_cc = main_controller.main_ui.cmbClienteCC
        self.lbl_deudatotal = main_controller.main_ui.lblDeudaTotalCC
        self.rbtn_saldar = main_controller.main_ui.rbtnSaldarCC
        self.rbtn_actualizar = main_controller.main_ui.rbtnActualizarCC
        self.txt_montocc = main_controller.main_ui.txtMontoCC
        self.btn_cargarcc = main_controller.main_ui.btnCargarCC
        self.btn_eliminarcc = main_controller.main_ui.btnEliminarUltimaCC
        self.lbl_dinerocalle = main_controller.main_ui.lblDineroCalle

        ######################################################################
        # Variables iniciales
        ######################################################################
        # Variable para guardar deuda de cliente
        self.deuda = 0


        ######################################################################
        # Inicialización de modelos y configuración inicial de interfaz
        ######################################################################
        # Inicialización modelo tabla
        self.configuracion_modelo_tablacc()
        
        # Llenado de combobox de clientes
        self.llenar_cmb_clientescc()

        # Visualización de dinero en calle
        self.ver_dinero_calle()

        ######################################################################
        # Asignación de métodos a botones
        ######################################################################
        # Asignación método carga de operación cuenta corriente
        self.btn_cargarcc.clicked.connect(self.cargar_operacion_cc)

        self.btn_eliminarcc.clicked.connect(self.eliminar_registro_cc)

        ######################################################################
        # Configuración de eventos
        ######################################################################
        # Asignación de evento para mostrar cuentas corrientes segun cliente
        self.cmb_cliente_cc.currentTextChanged.connect(
            self.cargar_cuentacorriente
        )


    ##########################################################################
    # MÉTODOS CONFIGURACIÓN DE INTERFAZ Y MODELO

    ##########################################################################
    # Configuración de modelo en tabla de cuenta corriente
    ##########################################################################
    def configuracion_modelo_tablacc(self):
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
        self.tabla_cc.setModel(self.model_cc)
        self.tabla_cc.setColumnHidden(0, True)
        self.tabla_cc.setColumnWidth(1, 260)
        self.tabla_cc.setColumnWidth(2, 120)
        self.tabla_cc.setColumnWidth(3, 200)
        self.tabla_cc.setColumnWidth(4, 150)
    

    ##########################################################################
    # Método carga de clientes con cuentas corrientes en combobox
    ##########################################################################
    def llenar_cmb_clientescc(self):
        ''' Método para llenar combobox de clientes en ventana de cuenta
            corriente.
        '''
        # Limpieza cmb inicial
        self.cmb_cliente_cc.clear()
        
        # Seteo primer elemento del combobox
        self.cmb_cliente_cc.addItem('Seleccionar cliente', None)
        # Obtención de clientes y carga en combobox
        clientes_cc = ModeloCuentaCorriente.clientes_cuentacorriente()
        if clientes_cc:
            for cliente in clientes_cc:
                self.cmb_cliente_cc.addItem(cliente[1], cliente[0])


    ##########################################################################
    # MÉTODOS PARA REALIZAR ACCIONES EN MODELO

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
        cliente = self.cmb_cliente_cc.currentData()

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
            self.lbl_deudatotal.setText(
                f"Deuda total: $ {self.deuda:.0f}"
            )
        else:
            self.lbl_deudatotal.setText("Deuda total: $ 0")


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
        cliente = self.cmb_cliente_cc.currentData()

        # Verificación de selección de cliente
        if not cliente:
            QMessageBox.warning(
                self.main_controller,
                'Cuenta Corriente',
                'Seleccionar un cliente'
            )
            return
        
        # Obtención tipo de operación de radiobuttons
        tipo_operacion = None

        if self.rbtn_saldar.isChecked():
            tipo_operacion = "Abona"
        
        if self.rbtn_actualizar.isChecked():
            tipo_operacion = "Actualización"
        
        # Verificación de selección de tipo de operación
        if tipo_operacion is None:
            QMessageBox.warning(
                self.main_controller,
                'Cuenta Corriente',
                'Seleccionar tipo de operación'
            )
            return

        # Obtención de monto de operación
        try:
            monto_operacion = float(self.txt_montocc.text())
        except ValueError:
            QMessageBox.warning(
                self.main_controller,
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
                self.main_controller,
                'Cuenta Corriente',
                'Operación cargada!'
            )
        
        # Eliminación de cuenta corriente si deuda es saldada completamente
        if deuda_total <= 0:
            ModeloCuentaCorriente.eliminar_cuentacorriente(cliente=cliente)
            self.llenar_cmb_clientescc()
            self.lbl_deudatotal.setText("Deuda total: $ 0")
            self.txt_montocc.setText("")
        
        self.txt_montocc.setText("")
        self.cargar_cuentacorriente()

        # Actualización dinero en calle
        self.ver_dinero_calle()


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
                self.main_controller,
                'Cuentas Corrientes',
                'Se debe seleccionar una cuenta corriente'
            )
            return
        
        # Obtención del número de operación
        nro_operacion = self.model_cc.item(ultima_fila, 0).text()

        # Consulta y eliminación de registro
        eliminar = QMessageBox.question(
            self.main_controller,
            'Cuentas corrientes',
            'Eliminar último registro?'
        )

        if eliminar == QMessageBox.Yes:
            ModeloCuentaCorriente.eliminar_operacion(nro_operacion)
            if ultima_fila == 0:
                self.llenar_cmb_clientescc()
                self.lbl_deudatotal.setText("Deuda total: $ 0")
                self.txt_montocc.setText("")

            QMessageBox.information(
                self.main_controller,
                'Cuentas Corrientes',
                'Registro de cuenta corriente eliminado!'
            )

        # Carga de tabla
        self.cargar_cuentacorriente()

        # Actualización dinero en calle
        self.ver_dinero_calle()
    

    ##########################################################################
    # Método para visualizar dinero en calle
    ##########################################################################
    def ver_dinero_calle(self):
        # Obtención de dinero en calle
        dinero_calle = ModeloCuentaCorriente.deuda_total_cuentacorrientes()

        # Actualización de label
        self.lbl_dinerocalle.setText(f"Dinero en calle: $ {dinero_calle:.0f}")