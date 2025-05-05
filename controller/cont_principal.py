##############################################################################
# Importaciones
##############################################################################

from datetime import datetime, date, time, timedelta
from view.interfaces.ventana_principal import VentanaPrincipal
from model.modelo_cliente import ModeloCliente
from model.modelo_servicio import ModeloServicio
from model.modelo_turno import ModeloTurno
from controller.cont_clientes import ClienteController
from controller.cont_servicios import (
    ServicioController, TarjetaServiciosController)
from controller.cont_turnos import (
    TurnoController, TarjetaTurnosController
)
from PySide6.QtWidgets import (
    QMainWindow, QSpacerItem, QSizePolicy, QMessageBox)
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import QDate, Qt

##############################################################################
# Controlador Principal
##############################################################################

class MainController(QMainWindow):

    def __init__(self):
        super().__init__()
        self.main_ui = VentanaPrincipal()
        self.main_ui.setupUi(self)

        ######################################################################
        # Seteo de botones para recorrer menú
        ######################################################################

        # Seteo de la página principal StackedWidget
        self.main_ui.StackedWidget.setCurrentIndex(3)

        self.main_ui.btn_clientes.clicked.connect(self.abrir_menu_clientes)
        self.main_ui.btn_servicios.clicked.connect(self.abrir_menu_servicios)
        self.main_ui.btn_turnos.clicked.connect(self.abrir_menu_turnos)
        self.main_ui.btnHistoriaClientes.clicked.connect(
            self.abrir_menu_historial
        )

        ######################################################################
        # Asignaciones de métodos a botones
        ######################################################################

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

        # Asignación método para mostrar historial de turnos por cliente
        self.main_ui.btnBuscarHist.clicked.connect(
            self.carga_historial
        )

        ######################################################################
        # Llenado comboboxs
        ######################################################################
        
        self.llenar_cmb_clientes()
        self.llenar_cmb_servicios()

        ######################################################################
        # Configuraciones turnos
        ######################################################################

        # Seteo del calendarWidget
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
        ######################################################################
        # Llamadas para agregar tarjetas de servicios
        ######################################################################
        
        # Visualización tarjetas de servicios
        self.mostrar_servicios()

        # Visualización de clientes en tabla
        self.cargar_clientes()

    ##########################################################################
    # Movimiento entre menú principal
    ##########################################################################
    
    def abrir_menu_clientes(self):
        self.main_ui.StackedWidget.setCurrentIndex(4)
    
    def abrir_menu_servicios(self):
        self.main_ui.StackedWidget.setCurrentIndex(0)
    
    def abrir_menu_turnos(self):
        self.main_ui.StackedWidget.setCurrentIndex(1)
    
    def abrir_menu_historial(self):
        self.main_ui.StackedWidget.setCurrentIndex(2)

    ##########################################################################
    # Apertura de ventanas secundarias
    ##########################################################################
    
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
    #                             CLIENTES                                   #
    ##########################################################################
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
                # Alineado de valores
                for item in fila:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                
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
    #                            SERVICIOS                                   #
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
        

