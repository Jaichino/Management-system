##############################################################################
# Importaciones
##############################################################################

from datetime import datetime, timedelta, date, time
from view.interfaces.ventana_turnos import VentanaTurno
from view.interfaces.widget_tarjetaturno import WidgetTarjetaTurno
from model.modelo_turnos import ModeloTurno
from model.modelo_clientes import ModeloCliente
from model.modelo_servicios import ModeloServicio
from PySide6.QtWidgets import QMainWindow, QWidget, QMessageBox

##############################################################################
# Controlador Widget - Tarjetas de Turnos
##############################################################################
class TarjetaTurnosController(QWidget):
    def __init__(self):
        super().__init__()
        self.widget_tarjetaturno = WidgetTarjetaTurno()
        self.widget_tarjetaturno.setupUi(self)

##############################################################################
# Controlador ventana nuevos turnos
##############################################################################
class TurnoController(QMainWindow):
    
    def __init__(self, main_controller):
        super().__init__()
        self.ui_turno = VentanaTurno()
        self.ui_turno.setupUi(self)
        self.modelo_turno = ModeloTurno()
        self.main_controller = main_controller

        # Inicialización de ComboBox clientes y servicios
        self.cargar_lista_clientes()
        self.cargar_lista_servicios()

        # Inicialización de campo de fecha con día actual
        self.ui_turno.dateEditTurno.setDate(datetime.now())

        # Asignación método nuevo_turno a botón
        self.ui_turno.btnAgendarTurno.clicked.connect(
            self.nuevo_turno
        )

    ##########################################################################
    # Métodos para setear elementos en comboboxs
    ##########################################################################

    def cargar_lista_clientes(self):
        ''' Método para cargar el listado de clientes existentes al ComboBox
            cmbCliente
        '''
        self.ui_turno.cmbCliente.clear()
        self.ui_turno.cmbCliente.addItem("Seleccionar cliente", None)

        clientes = ModeloCliente.lista_clientes()
        for cliente in clientes:
            self.ui_turno.cmbCliente.addItem(cliente.nombre, cliente.id)
    
    def cargar_lista_servicios(self):
        ''' Método para cargar el listado de servicios existentes al ComboBox
            cmbServicio
        '''
        self.ui_turno.cmbServicio.clear()

        servicios = ModeloServicio.lista_servicios()
        for servicio in servicios:
            self.ui_turno.cmbServicio.addItem(servicio.nombre, servicio.id)


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
        cliente = self.ui_turno.cmbCliente.currentData()
        fecha = self.ui_turno.dateEditTurno.date()
        hora = self.ui_turno.timeEditTurno.time()
        servicio = self.ui_turno.cmbServicio.currentData()
        observacion = self.ui_turno.txtObservacion.toPlainText()
        nombre_servicio = self.ui_turno.cmbServicio.currentText()

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

        # Actualización de contenedor
        self.main_controller.agregar_turnos(fecha_form)
        self.main_controller.main_ui.calendarWidget.setSelectedDate(fecha)

        # Actualización de combobox pagina historial clientes
        self.main_controller.llenar_cmb_clientes()

        QMessageBox.information(
            self,
            'Carga de turno',
            f'{nombre_servicio} agendado para {fecha_form.strftime("%d/%m")}'
        )
