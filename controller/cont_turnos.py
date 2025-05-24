##############################################################################
# Importaciones
##############################################################################

from typing import TYPE_CHECKING
from datetime import datetime, timedelta, date, time

from PySide6.QtWidgets import (
    QMainWindow, QWidget, QMessageBox, QSpacerItem, QSizePolicy
)
from PySide6.QtCore import QObject, QDate, Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel

from view.interfaces.ventana_turnos import VentanaTurno
from view.interfaces.widget_tarjetaturno import WidgetTarjetaTurno
from model.modelo_turno import ModeloTurno
from model.modelo_cliente import ModeloCliente
from model.modelo_servicio import ModeloServicio
if TYPE_CHECKING:
    from controller.cont_principal import MainController


##############################################################################
##############################################################################
#                 Controlador Widget - Tarjetas de Turnos                    #
##############################################################################
##############################################################################
class TarjetaTurnosController(QWidget):
    def __init__(self):
        super().__init__()
        self.widget_tarjetaturno = WidgetTarjetaTurno()
        self.widget_tarjetaturno.setupUi(self)



##############################################################################
##############################################################################
#                      CONTROLADOR PRINCIPAL TURNOS                          #
##############################################################################
##############################################################################
class TurnoController(QObject):
    def __init__(self, main_controller: 'MainController'):
        super().__init__()
        self.main_controller = main_controller

        ######################################################################
        # Llamada a widgets necesarios
        ######################################################################
        self.cont_turnos = main_controller.main_ui.contenedorTurnos
        self.calendario = main_controller.main_ui.calendarWidget
        self.cmb_cliente_hist = main_controller.main_ui.cmbClienteHist
        self.cmb_servicio_hist = main_controller.main_ui.cmbServicioHist
        self.tabla_historial = main_controller.main_ui.tablaHistorial
        self.btn_buscar_historial = main_controller.main_ui.btnBuscarHist


        ######################################################################
        # Inicialización de modelos y configuraciones iniciales
        ######################################################################
        # Seteo del calendarWidget
        self.calendario.setCurrentPage(
            QDate.currentDate().year(),
            QDate.currentDate().month()
        )
        self.calendario.setSelectedDate(datetime.now())

        # Que siempre arranque mostrando los turnos del día actual
        self.agregar_turnos(date.today())

        # Inicialización de modelo tabla historial de turnos
        self.configuracion_modelo_tablahistorial()

        # Llenado de comboboxs
        self.llenar_cmb_clientes()
        self.llenar_cmb_servicios()


        ######################################################################
        # Configuración de eventos
        ######################################################################
        # Asignación de evento para mostrar tarjetas de turnos segun fecha
        self.calendario.selectionChanged.connect(
            self.actualizar_turnos
        )

        ######################################################################
        # Asignación de métodos a botones
        ######################################################################
        # Asignación método para mostrar historial de turnos por cliente
        self.btn_buscar_historial.clicked.connect(
            self.carga_historial
        )


    ##########################################################################
    # Posicionamiento de tarjetas de Turnos
    ##########################################################################
    def agregar_turnos(self, fecha: date):
        # Se define el contenedor donde irán las tarjetas
        contenedor = self.cont_turnos.layout()
        contenedor.setContentsMargins(5,5,5,5)
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
            tarjeta.widget_tarjetaturno.lblHoraTurno.setText(
                time.strftime(turno[1],"%H:%M")
            )
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


    ##########################################################################
    # Método para actualizar turnos según fecha seleccionada en calendarWidget
    ##########################################################################
    def actualizar_turnos(self):
        fecha_qdate = self.calendario.selectedDate()
        fecha = date(
            year=fecha_qdate.year(),
            month=fecha_qdate.month(),
            day=fecha_qdate.day()
        )
        self.agregar_turnos(fecha)


    ##########################################################################
    # Método para eliminar turnos agendados
    ##########################################################################
    def eliminar_turno(self, turno_id):
        # Se consulta si se quiere eliminar un turno
        eliminar = QMessageBox.question(
            self.main_controller,
            'Turnos',
            'Queres eliminar este turno?'
        )
        if eliminar == QMessageBox.Yes:
            ModeloTurno.eliminar_turno(turno_id)
            QMessageBox.information(
            self.main_controller,
            'Turnos',
            'Turno eliminado!'
            )

        # Se busca fecha seleccionada en calendario y se actualiza vista
        fecha_qt = self.calendario.selectedDate()
        fecha = date(
            year=fecha_qt.year(),
            month=fecha_qt.month(),
            day=fecha_qt.day()
        )

        # Actualización de pantalla y cmb clientes historial
        self.agregar_turnos(fecha)
        self.llenar_cmb_clientes()
        self.model_thist.removeRows(0, self.model_thist.rowCount())

    ##########################################################################
    #                          HISTORIAL TURNOS                              #
    ##########################################################################
    
    ##########################################################################
    # Carga de ComboBoxs de cliente y servicios historial de turnos
    ##########################################################################
    def llenar_cmb_clientes(self):
        # Obtención de clientes
        clientes = ModeloTurno.clientes_con_turnos()
        # Asignación primer valor del combobox
        self.cmb_cliente_hist.clear()
        self.cmb_cliente_hist.addItem("Seleccionar cliente", None)
        # Asignación a combobox
        for cliente in clientes:
            self.cmb_cliente_hist.addItem(cliente.nombre, cliente.id)


    def llenar_cmb_servicios(self):
        # Obtención de servicios
        servicios = ModeloServicio.lista_servicios()
        # Asignación primer valor del combobox
        self.cmb_servicio_hist.clear()
        self.cmb_servicio_hist.addItem("Seleccionar servicio", None)
        # Asignación a combobox
        for servicio in servicios:
            self.cmb_servicio_hist.addItem(servicio.nombre, servicio.id)


    ##########################################################################
    # Método para la definición del modelo en tabla historial de turnos
    ##########################################################################
    def configuracion_modelo_tablahistorial(self):
        # Definición del modelo para insertar datos
        self.model_thist = QStandardItemModel()
        self.model_thist.setHorizontalHeaderLabels(
            ["Turno", "Fecha Turno", "Tratamiento", "Observación"]
        )
        # Seteo del modelo a tabla y dimensiones de columnas
        self.tabla_historial.setModel(self.model_thist)

        self.tabla_historial.setColumnWidth(0,80)
        self.tabla_historial.setColumnWidth(1,120)
        self.tabla_historial.setColumnWidth(2,250)


    ##########################################################################
    # Carga de Historiales de tratamientos a clientes en Tabla
    ##########################################################################
    def carga_historial(self):
        # Obtención de entradas de usuario
        cliente = self.cmb_cliente_hist.currentData()
        servicio = self.cmb_servicio_hist.currentData()
        fecha = date.today()

        # Verificación de que cliente no es None
        if cliente == None:
            QMessageBox.critical(
                self.main_controller,
                'Historial Clientes',
                'Tenes que elegir un cliente !'
            )
            self.model_thist.removeRows(0, self.model_thist.rowCount())
            return

        # Se limpia el modelo antes de cargar clientes
        self.model_thist.removeRows(0, self.model_thist.rowCount())

        # Obtención de historial
        turnos = ModeloTurno.historial_turnos(
            cliente=cliente, fecha=fecha, servicio=servicio
        )

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



##############################################################################
##############################################################################
#                   CONTROLADOR VENTANA NUEVO TURNO                          #
##############################################################################
##############################################################################

class NuevoTurnoController(QMainWindow):
    
    def __init__(self, main_controller: 'MainController'):
        super().__init__()
        self.ui_turno = VentanaTurno()
        self.ui_turno.setupUi(self)
        self.modelo_turno = ModeloTurno()
        self.main_controller = main_controller

        ######################################################################
        # Llamada a widgets necesarios
        ######################################################################
        # Txts
        self.txt_observacion = self.ui_turno.txtObservacion

        # Times
        self.date_turno = self.ui_turno.dateEditTurno
        self.hora_turno = self.ui_turno.timeEditTurno

        # Comboboxs
        self.cmb_cliente = self.ui_turno.cmbCliente
        self.cmb_servicio = self.ui_turno.cmbServicio
        
        # Botones
        self.btn_agendar = self.ui_turno.btnAgendarTurno

        ######################################################################
        # Configuraciones iniciales de interfaz y modelos
        ######################################################################
        # Inicialización de ComboBox clientes y servicios
        self.cargar_lista_clientes()
        self.cargar_lista_servicios()

        # Inicialización de campo de fecha con día actual
        self.date_turno.setDate(datetime.now())

        ######################################################################
        # Asignación de métodos a botones
        ######################################################################
        # Asignación método nuevo_turno a botón
        self.btn_agendar.clicked.connect(self.nuevo_turno)


    ##########################################################################
    # Métodos para setear elementos en comboboxs
    ##########################################################################
    def cargar_lista_clientes(self):
        ''' Método para cargar el listado de clientes existentes al ComboBox
            cmbCliente
        '''
        self.cmb_cliente.clear()
        self.cmb_cliente.addItem("Seleccionar cliente", None)

        clientes = ModeloCliente.lista_clientes()
        for cliente in clientes:
            if cliente.nombre == "CLIENTE NO REGISTRADO":
                continue
            self.cmb_cliente.addItem(cliente.nombre, cliente.id)


    def cargar_lista_servicios(self):
        ''' Método para cargar el listado de servicios existentes al ComboBox
            cmbServicio
        '''
        self.cmb_servicio.clear()

        servicios = ModeloServicio.lista_servicios()
        for servicio in servicios:
            self.cmb_servicio.addItem(servicio.nombre, servicio.id)


    ##########################################################################
    # Métodos para cargar nuevos turnos y logíca de agendado
    ##########################################################################
    def solapamiento_turnos(self, fecha_turno, hora_inicio, duracion):
        ''' Este método contiene la lógica que se utiliza para comprobar que
            no se superpongan turnos.
            Se calcula la fecha y hora inicial y final del turno agendar, y
            luego se recorre el listado de turnos agendados para esa fecha
            y se verifica que no haya superposición horaria
        '''
        # Cálculo inicio y fin del turno a agendar
        inicio = datetime.combine(fecha_turno, hora_inicio)
        fin = inicio + timedelta(minutes=duracion)

        # Obtención del listado de turnos existentes
        turnos = self.modelo_turno.turnos_fecha(fecha_turno)
        
        # Se recorren turnos y se comprueba que no haya solapamiento
        for turno in turnos:
            turno_inicio = datetime.combine(turno[0], turno[1])
            turno_fin = turno_inicio + timedelta(minutes=turno[6])

            # Logica de solapamiento
            if inicio < turno_fin and fin > turno_inicio:
                return False # Hay solapamiento de turno
            
        return True # No hay solapamientos, se puede agendar el turno


    def nuevo_turno(self):
        ''' Método para agendar nuevos turnos en la base de datos. Se
            recuperan valores de campos, se carga turno a la base de datos y
            se actualiza el contenedor de turnos.
        '''
        # Obtención de campos
        cliente = self.cmb_cliente.currentData()
        fecha = self.date_turno.date()
        hora = self.hora_turno.time()
        servicio = self.cmb_servicio.currentData()
        observacion = self.txt_observacion.toPlainText()
        nombre_servicio = self.cmb_servicio.currentText()

        # Comprobación de selección de cliente
        if cliente is None:
            QMessageBox.critical(
                self,
                "Carga de turno",
                "Se debe elegir un cliente"
            )
            return
        
        # Obtención de la duración del turno
        duracion = ModeloServicio.info_servicio(servicio).duracion

        # Se convierte fecha y hora en formatos date y time de python
        fecha_form = date(
            fecha.year(),
            fecha.month(),
            fecha.day()
        )
        hora_form = time(
            hora.hour(),
            hora.minute()
        )

        # Comprobación de que no hay solapamiento de turnos
        if not self.solapamiento_turnos(fecha_form, hora_form, duracion):
            QMessageBox.critical(
                self,
                'Carga de turno',
                'Hay un turno que coincide con el horario elegido!'
            )
            return

        # Carga de turno
        self.modelo_turno.nuevo_turno(
            cliente, servicio, fecha_form, hora_form, observacion
        )

        # Cerrado de ventana
        self.close()

        QMessageBox.information(
            self,
            'Carga de turno',
            f'{nombre_servicio} agendado para {fecha_form.strftime("%d/%m")}'
        )

        # Actualización de contenedor
        self.main_controller.turno_controller.agregar_turnos(fecha_form)
        self.main_controller.turno_controller.calendario.setSelectedDate(
            fecha
        )

        # Actualización de combobox pagina historial clientes
        self.main_controller.turno_controller.llenar_cmb_clientes()
