##############################################################################
# Importaciones
##############################################################################

from typing import TYPE_CHECKING
from datetime import datetime, timedelta, date, time

from PySide6.QtWidgets import (
    QMainWindow, QWidget, QMessageBox, QSpacerItem, QSizePolicy, 
    QTableWidgetItem, QPushButton, QDialog
)
from PySide6.QtCore import QObject, QDate, Qt

from view.interfaces.ventana_turnos import VentanaTurno
from view.interfaces.widget_tarjetaturno import WidgetTarjetaTurno
from view.interfaces.ventana_observacion import VentanaObservacion
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
        self.lbl_obs = main_controller.main_ui.txtUltimaObservacion


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

        self.btn_buscar_historial.clicked.connect(
            self.inicializar_ultima_obs
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
            monto_faltante = turno[5] - turno[4]
            # Se obtiene hora de finalización
            hora_inicio = datetime.combine(datetime.today(), turno[1])
            hora_fin = hora_inicio + timedelta(minutes=turno[6])
            hora_fin_format = hora_fin.strftime("%H:%M")

            # Carga de valores en widget
            tarjeta.widget_tarjetaturno.lblCliente.setText(turno[2])
            tarjeta.widget_tarjetaturno.lblServicio.setText(turno[3])
            tarjeta.widget_tarjetaturno.lblSenia.setText(f'$ {turno[4]:.0f}')
            tarjeta.widget_tarjetaturno.lblHoraTurno.setText(
                time.strftime(turno[1],"%H:%M")
            )
            tarjeta.widget_tarjetaturno.lblPrecio.setText(f'$ {turno[5]:.0f}')
            tarjeta.widget_tarjetaturno.lblDuracion.setText(hora_fin_format)
            tarjeta.widget_tarjetaturno.lblFaltaPagar.setText(
                f'$ {monto_faltante:.0f}'
            )

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
        self.tabla_historial.setColumnCount(5)
        self.tabla_historial.setHorizontalHeaderLabels(
            ["id", "N°", "Fecha Turno", "Tratamiento", "Observación"]
        )
        
        self.tabla_historial.setColumnHidden(0, True)
        self.tabla_historial.setColumnWidth(1,50)
        self.tabla_historial.setColumnWidth(2,200)
        self.tabla_historial.setColumnWidth(3,300)


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
            self.tabla_historial.setRowCount(0)
            return
            

        # Obtención de historial
        turnos = ModeloTurno.historial_turnos(
            cliente=cliente, fecha=fecha, servicio=servicio
        )

        self.tabla_historial.setRowCount(len(turnos))

        # Carga de datos en tabla
        for i, turno in enumerate(turnos, start=1):
            fecha_format = date.strftime(turno[1], '%d/%m/%Y')
            
            self.tabla_historial.setItem(
                i-1, 0, QTableWidgetItem(str(turno[0]))
            )
            self.tabla_historial.setItem(
                i-1, 1, QTableWidgetItem(str(i))
            )
            self.tabla_historial.setItem(
                i-1, 2, QTableWidgetItem(fecha_format)
            )
            self.tabla_historial.setItem(
                i-1, 3, QTableWidgetItem(turno[3])
            )
            
            # Creación de botón
            btn = QPushButton("Observación")
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
            btn.clicked.connect(
                lambda _,
                turno_id = turno[0] : self.main_controller.ventana_observacion(
                    turno_id=turno_id
                )
            )
            self.tabla_historial.setCellWidget(i-1, 4, btn)
    

    ##########################################################################
    # Método para inicializar ventana con la última observación del cliente
    ##########################################################################
    def inicializar_ultima_obs(self):
        # Recuperación de cliente y servicio
        cliente = self.cmb_cliente_hist.currentData()
        servicio = self.cmb_servicio_hist.currentData()

        # Obtención de historiales para ese cliente y servicio
        historiales = ModeloTurno.historial_turnos(
            cliente, date.today(), servicio
        )

        if historiales:
            # Obtención de la última observación
            ultima_observacion = historiales[-1][4]
            ult_servicio = historiales[-1][3]
        else:
            ultima_observacion = ""
            ult_servicio = ""

        if ultima_observacion is None:
            ultima_observacion = ""

        # Seteo de última observación
        if not servicio:
            self.lbl_obs.setPlainText(
                f"Ultima observación [{ult_servicio}]: {ultima_observacion}")

        else:
            self.lbl_obs.setPlainText(
                f'Ultima observacion: {ultima_observacion}'
            )



##############################################################################
##############################################################################
#                   CONTROLADOR VENTANA OBSERVACIONES                        #
##############################################################################
##############################################################################
class VentanaObservacionController(QDialog):
    def __init__(self, main_controller: 'MainController', turno_id: int):
        super().__init__()
        self.ui_obs = VentanaObservacion()
        self.ui_obs.setupUi(self)
        self.main_controller = main_controller
        self.turno_id = turno_id

        ######################################################################
        # Llamada a widgets necesarios
        ######################################################################
        self.txt_observacion = self.ui_obs.editObservacion
        self.btn_guardar_obs = self.ui_obs.btnGuardarObs


        ######################################################################
        # Configuraciones inicialización
        ######################################################################
        # Inicialización con observación de turno
        self.inicializacion_observacion()

        ######################################################################
        # Seteo de métodos en botones
        ######################################################################
        self.btn_guardar_obs.clicked.connect(self.actualizar_observacion)


    ##########################################################################
    # Método para recuperar observación cargada en turno al iniciar ventana
    ##########################################################################
    def inicializacion_observacion(self):
        # Información de turno
        info = ModeloTurno.info_turno(self.turno_id)
        observacion = info.observacion

        # Configuración de campo de texto con observación
        self.txt_observacion.setPlainText(observacion)
    

    ##########################################################################
    # Método para modificar la observación de un turno determinado
    ##########################################################################
    def actualizar_observacion(self):
        # Recuperación de texto en txt_observacion
        observacion = self.txt_observacion.toPlainText()

        # Guardado de observación en base de datos
        ModeloTurno.actualizar_turno(self.turno_id, observacion)
        QMessageBox.information(
            self,
            'Observación de turno',
            'Observación cargada !'
        )

        # Actualización de ventana principal
        self.main_controller.turno_controller.inicializar_ultima_obs()


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
        self.txt_senia = self.ui_turno.txtSenia

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
        senia = self.txt_senia.text()
        nombre_servicio = self.cmb_servicio.currentText()

        # Comprobación de selección de cliente
        if cliente is None:
            QMessageBox.critical(
                self,
                "Carga de turno",
                "Se debe elegir un cliente"
            )
            return
        
        # Asignación de 0 si senia == ''
        if senia == '':
            senia = 0
        
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
            QMessageBox.information(
                self,
                'Carga de turno',
                'Hay un turno que coincide con el horario elegido!'
            )
            return
        try:
            senia = float(senia)
            
            # Carga de turno
            self.modelo_turno.nuevo_turno(
                cliente=cliente,
                servicio=servicio,
                fecha=fecha_form,
                hora=hora_form,
                senia=senia
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
            # Limpieza de tabla
            self.main_controller.turno_controller.tabla_historial.setRowCount(0)
            # Seteo ultima observación
            self.main_controller.turno_controller.lbl_obs.setPlainText("Ultima observación: ")

        except ValueError:
            QMessageBox.warning(
                self,
                'Nuevo Turno',
                'Revisar monto de seña ingresado'
            )