##############################################################################
# Importaciones
##############################################################################

from datetime import datetime, date, time, timedelta
from view.interfaces.ventana_principal import VentanaPrincipal
from view.interfaces.ventana_clientes import VentanaCliente
from view.interfaces.ventana_servicios import VentanaServicio
from view.interfaces.ventana_turnos import VentanaTurno
from view.interfaces.widget_tarjetaservicio import WidgetTarjetaServicio
from view.interfaces.widget_tarjetaturno import WidgetTarjetaTurno
from model.modelo_clientes import ModeloCliente
from model.modelo_servicios import ModeloServicio
from model.modelo_turnos import ModeloTurno
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QMessageBox)
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import QDate

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
        self.widget_tserv = WidgetTarjetaServicio()
        self.widget_tserv.setupUi(self)

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
            cel = self.ui_cliente.txtCelular.text()
            email = self.ui_cliente.txtEmail.text().lower()

            # Comprobación de que se llenan campos obligatorios
            if nombre == '':
                QMessageBox.critical(
                    self,
                    "Nuevo Cliente",
                    "El campo de nombre es obligatorio"
                )
                return
            
            if cel != '':
                cel = int(cel)

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
    
    def __init__(self, main_controller):
        super().__init__()
        self.ui_servicio = VentanaServicio()
        self.ui_servicio.setupUi(self)
        self.main_controller = main_controller

        # Variables que sirven para decidir en método guardar_servicio
        self.modo = 'nuevo'
        self.id_servicio = None
    
        # Asignación método nuevo_servicio a boton btnGuardarServicio
        self.ui_servicio.btnGuardarServicio.clicked.connect(
            self.guardar_servicio
        )
    
    ##############################################################################
    # Métodos guardar servicio (Decicide entre crear y editar)
    ##############################################################################

    def guardar_servicio(self):
        # Recuperación de valores de campos
        nombre = self.ui_servicio.txtNombre.text().upper()
        duracion = self.ui_servicio.txtDuracion.text()
        precio = self.ui_servicio.txtPrecio.text()

        try:
            duracion = int(duracion)
            precio = float(precio)

            # Decición si se carga nuevo producto o se edita uno seleccionado
            if self.modo == 'nuevo':
                ModeloServicio.nuevo_servicio(nombre, duracion, precio)
                QMessageBox.information(
                    self,
                    'Nuevo Servicio',
                    f'{nombre} agregado a listado de servicios!'
                )

            elif self.modo == 'editar':
                ModeloServicio.editar_servicio(
                    self.id_servicio, nombre, duracion, precio
                )
                QMessageBox.information(
                    self,
                    'Servicios',
                    'Servicio actualizado!'
                )
            
            # Limpieza de campos
            self.ui_servicio.txtNombre.setText("")
            self.ui_servicio.txtDuracion.setText("")
            self.ui_servicio.txtPrecio.setText("")

            # Actualización del listado de servicios
            self.main_controller.mostrar_servicios()
            
        except ValueError:
            QMessageBox.critical(
                self,
                'Nuevo Servicio',
                'Revisar campos'
            )
        
        except Exception as e:
            QMessageBox.critical(
                self,
                'Nuevo Servicio',
                f'Error - {e}'
            )


    def cargar_datos(self, servicio=None):
        ''' Método para decidir si al presionar boton btnGuardarServicio, se 
            edita un servicio seleccionado o se carga un nuevo servicio.

            Se llama desde MainController y se le pasa el servicio que se
            selecciona en una determinada tarjeta. Se setea el self.modo a
            editar para que luego el metodo guardar_servicio no lo cargue como
            uno nuevo, sino que aplique el metodo editar_servicio
        '''
        if servicio:
            self.modo = 'editar'
            self.id_servicio = servicio.id
            self.ui_servicio.txtNombre.setText(servicio.nombre)
            self.ui_servicio.txtDuracion.setText(str(servicio.duracion))
            self.ui_servicio.txtPrecio.setText(str(servicio.precio))
        else:
            self.modo = 'nuevo'
            self.id_servicio = None



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

        QMessageBox.information(
            self,
            'Carga de turno',
            f'{nombre_servicio} agendado para {fecha_form.strftime("%d/%m")}'
        )



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

        # Asignación método eliminación de clientes
        self.main_ui.btnEliminarCliente.clicked.connect(
            self.eliminar_cliente
        )

        # Asignación método para filtrado de clientes
        self.main_ui.btnFiltrarCliente.clicked.connect(
            self.cargar_clientes
        )

        self.main_ui.calendarWidget.setCurrentPage(
            QDate.currentDate().year(),
            QDate.currentDate().month()
        )
        self.main_ui.calendarWidget.setSelectedDate(datetime.now())


        # Que siempre arranque mostrando los turnos del día actual
        self.agregar_turnos(date.today())

        # Asignación de evento para mostrar tarjetas de turnos segun fecha
        self.main_ui.calendarWidget.selectionChanged.connect(
            self.actualizar_turnos
        )

        # Llamadas para agregar tarjetas de servicios
        self.mostrar_servicios()

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
        self.abrir_nuevo_servicio = ServicioController(self)
        self.abrir_nuevo_servicio.show()

    # Apertura ventana nuevo turno
    def ventana_nuevo_turno(self):
        self.abrir_nuevo_turno = TurnoController(self)
        self.abrir_nuevo_turno.show()

    ##########################################################################
    # Método para carga de clientes en QTableView
    ##########################################################################

    def cargar_clientes(self):
        
        # Se establece modelo y headers del modelo
        self.modelo_tcliente = QStandardItemModel()
        self.modelo_tcliente.setHorizontalHeaderLabels(
            ["ID","Nombre", "Teléfono", "Email"]
        )

        # Se limpia el modelo antes de cargar clientes
        self.modelo_tcliente.removeRows(0, self.modelo_tcliente.rowCount())

        # Se verifica si hay algún filtro de nombre de cliente aplicado
        filtro = self.main_ui.lineEditCliente.text()
        if filtro == '':
            # Se recuperan clientes de la base de datos
            clientes = ModeloCliente.lista_clientes()

        else:
            # Se recuperan clientes con el filtro de nombre aplicado
            clientes = ModeloCliente.filtrar_cliente(filtro)
            if not clientes:
                QMessageBox.information(
                    self,
                    "Clientes",
                    "No se encontraron clientes"
                )
                return
        
        # Se crean filas y se cargan al modelo
        for cliente in clientes:
                fila = [
                    QStandardItem(str(cliente.id)),
                    QStandardItem(cliente.nombre),
                    QStandardItem(str(cliente.telefono)),
                    QStandardItem(cliente.email)
                ]
                self.modelo_tcliente.appendRow(fila)

        self.main_ui.tablaClientes.setModel(self.modelo_tcliente)

        # Se conecta evento itemChanged para cuando se modifica algún campo
        self.modelo_tcliente.itemChanged.connect(self.edicion_cliente)
        
        # Se oculta la columna de id de cliente
        self.main_ui.tablaClientes.setColumnHidden(0, True)

        # Seteo de dimensiones fijas de columnas
        self.main_ui.tablaClientes.setColumnWidth(1,200)
        self.main_ui.tablaClientes.setColumnWidth(2,300)
    
    ##########################################################################
    # Método para edición de clientes
    ##########################################################################

    def edicion_cliente(self):

        # Obtención de fila seleccionada
        fila = self.main_ui.tablaClientes.currentIndex().row()
        
        # Verificación de fila seleccionada
        if fila == -1:
            QMessageBox.warning(
                self,
                "Edición de cliente",
                "Se debe seleccionar un cliente"
            )
            return
        
        # Obtención del id del cliente (columna 0)
        id_cliente = self.modelo_tcliente.item(fila, 0).text()

        # Se recuperan valores de campos
        nombre = self.modelo_tcliente.item(fila, 1).text().upper()
        email = self.modelo_tcliente.item(fila, 3).text().lower()
        try:
            telefono = self.modelo_tcliente.item(fila, 2).text()
            if telefono != "":
                telefono = int(telefono)
            # Se llama a metodo de edición de cliente
            ModeloCliente.editar_cliente(id_cliente, nombre, telefono, email)
            self.cargar_clientes()

        except ValueError:
            QMessageBox.critical(
                self,
                "Edición de cliente",
                "Revisar el campo teléfono"
            )
            self.cargar_clientes()
    
    ##########################################################################
    # Método para eliminación de clientes
    ##########################################################################
    def eliminar_cliente(self):

        # Obtención de fila seleccionada
        fila = self.main_ui.tablaClientes.currentIndex().row()
        
        # Verificación de fila seleccionada
        if fila == -1:
            QMessageBox.warning(
                self,
                "Edición de cliente",
                "Se debe seleccionar un cliente"
            )
            return
        
        # Obtención del id del cliente (columna 0)
        id_cliente = self.modelo_tcliente.item(fila, 0).text()
        nombre_cliente = ModeloCliente.info_cliente(id_cliente).nombre

        # Consulta de eliminación
        eliminar = QMessageBox.question(
            self,
            'Eliminar Cliente',
            f"Desea eliminar al cliente ({nombre_cliente})?"
        )

        if eliminar == QMessageBox.Yes:
            ModeloCliente.eliminar_cliente(id_cliente)
            QMessageBox.information(
                self,
                "Cliente Eliminado",
                f"Se eliminó a {nombre_cliente}"
            )
        
        self.cargar_clientes()

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
