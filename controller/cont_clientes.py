##############################################################################
# Importaciones
##############################################################################

from typing import TYPE_CHECKING

from PySide6.QtCore import QObject, Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import (
    QMainWindow, QMessageBox, QTableWidgetItem, QPushButton
)

from utils.generador_fichas import crear_ficha_cosmetologica
from view.interfaces.ventana_clientes import VentanaCliente
from model.modelo_cliente import ModeloCliente
if TYPE_CHECKING:
    from controller.cont_principal import MainController


##############################################################################
##############################################################################
#                CONTROLADOR VENTANA CLIENTES (StackedWidget)                #
##############################################################################
##############################################################################
class ClienteController(QObject):

    def __init__(self, main_controller: 'MainController'):
        super().__init__()
        self.main_controller = main_controller

        ######################################################################
        # Llamada a widgets necesarios
        ######################################################################
        self.txt_cliente = main_controller.main_ui.lineEditCliente
        self.tabla_cliente = main_controller.main_ui.tablaClientes
        self.btn_eliminarcliente = main_controller.main_ui.btnEliminarCliente
        self.btn_filtrarcliente = main_controller.main_ui.btnFiltrarCliente

        ######################################################################
        # Inicialización de modelos
        ######################################################################
        # Configuración de modelo en tabla
        self.configurar_modelo_tablaclientes()
        # Inicialización con clientes cargados
        self.cargar_clientes()


        ######################################################################    
        # Asignación de métodos a botones
        ######################################################################
        # Asignación método eliminación de clientes
        self.btn_eliminarcliente.clicked.connect(
            self.eliminar_cliente
        )

        # Asignación método para filtrado de clientes
        self.btn_filtrarcliente.clicked.connect(
            self.cargar_clientes
        )

        ######################################################################
        # Asignación de eventos
        ######################################################################
        # Se conecta evento itemChanged para cuando se modifica algún campo
        self.modelo_tcliente.itemChanged.connect(self.edicion_cliente)



    ##########################################################################
    # Método para configurar modelo en tabla de clientes
    ##########################################################################
    def configurar_modelo_tablaclientes(self):
        # Se establece modelo y headers del modelo
        self.modelo_tcliente = self.tabla_cliente
        self.modelo_tcliente.setColumnCount(5)
        self.modelo_tcliente.setHorizontalHeaderLabels(
            ["ID","Nombre", "Teléfono", "Email", "Ficha"]
        )

        # Se oculta la columna de id de cliente
        self.tabla_cliente.setColumnHidden(0, True)

        # Seteo de dimensiones fijas de columnas
        self.tabla_cliente.setColumnWidth(1,200)
        self.tabla_cliente.setColumnWidth(2,200)
        self.tabla_cliente.setColumnWidth(3,300)


    ##########################################################################
    # Método para carga de clientes en tabla
    ##########################################################################

    def cargar_clientes(self):

        try:
            self.modelo_tcliente.blockSignals(True)
            # Se verifica si hay algún filtro de nombre de cliente aplicado
            filtro = self.txt_cliente.text()
            if filtro == '':
                # Se recuperan clientes de la base de datos
                clientes = ModeloCliente.lista_clientes()

            else:
                # Se recuperan clientes con el filtro de nombre aplicado
                clientes = ModeloCliente.filtrar_cliente(filtro)
                if not clientes:
                    QMessageBox.information(
                        self.main_controller,
                        "Clientes",
                        "No se encontraron clientes"
                    )
                    return
            
            for i, c in enumerate(clientes, start=0):
                if c.nombre == "CLIENTE NO REGISTRADO":
                    clientes.pop(i)


            # Posicionamiento de clientes en tabla
            self.modelo_tcliente.setRowCount(len(clientes))

            for i, cliente in enumerate(clientes):

                    self.modelo_tcliente.setItem(
                        i, 0, QTableWidgetItem(str(cliente.id))
                    )
                    self.modelo_tcliente.setItem(
                        i, 1, QTableWidgetItem(cliente.nombre)
                    )
                    self.modelo_tcliente.setItem(
                        i, 2, QTableWidgetItem(str(cliente.telefono))
                    )
                    self.modelo_tcliente.setItem(
                        i, 3, QTableWidgetItem(cliente.email)
                    )

                    # Creación de botón en ultima columna
                    btn = QPushButton("Ficha cosmetológica")
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

                    # Conexión de botón con método creación ficha cosmetológica
                    btn.clicked.connect(
                        lambda _,
                        id=cliente.id : self.abrir_fichacosmetologica(
                            cliente_id=id
                        )
                    )

                    self.modelo_tcliente.setCellWidget(i, 4, btn)
        finally:
            self.modelo_tcliente.blockSignals(False)


    ##########################################################################
    # Método para edición de clientes
    ##########################################################################

    def edicion_cliente(self):
        # Obtención de fila seleccionada
        fila = self.tabla_cliente.currentIndex().row()
        
        # Verificación de fila seleccionada
        if fila == -1:
            QMessageBox.warning(
                self.main_controller,
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

            self.main_controller.venta_controller.llenar_cmb_clientes_venta()

        # Manejo de excepciones
        except ValueError:
            QMessageBox.critical(
                self.main_controller,
                "Edición de cliente",
                "Revisar el campo teléfono"
            )
            self.cargar_clientes()


    ##########################################################################
    # Método para eliminación de clientes
    ##########################################################################
    def eliminar_cliente(self):

        # Obtención de fila seleccionada
        fila = self.tabla_cliente.currentIndex().row()
        
        # Verificación de fila seleccionada
        if fila == -1:
            QMessageBox.warning(
                self.main_controller,
                "Edición de cliente",
                "Se debe seleccionar un cliente"
            )
            return
        
        # Obtención del id del cliente (columna 0)
        id_cliente = self.modelo_tcliente.item(fila, 0).text()
        nombre_cliente = ModeloCliente.info_cliente(id_cliente).nombre

        # Consulta de eliminación
        eliminar = QMessageBox.question(
            self.main_controller,
            'Eliminar Cliente',
            f"Desea eliminar al cliente ({nombre_cliente})?"
        )

        if eliminar == QMessageBox.Yes:
            ModeloCliente.eliminar_cliente(id_cliente)
            QMessageBox.information(
                self.main_controller,
                "Cliente Eliminado",
                f"Se eliminó a {nombre_cliente}"
            )
        
        # Actualización tabla clientes
        self.cargar_clientes()

        # Actualización combobox cliente cuenta corriente (si tiene)
        self.main_controller.cc_controller.llenar_cmb_clientescc()


    ##########################################################################
    # Método para la apertura de fichas cosmetológicas por cliente
    ##########################################################################
    def abrir_fichacosmetologica(self, cliente_id: int):
        ''' Método para vincular al botón de ver ficha cosmetológica en tabla
            de clientes. Se recupera el id respectivo del botón y se ejecuta
            la función crear_ficha_cosmetologica()
        '''
        # Información del cliente ingresado
        cliente = ModeloCliente.info_cliente(cliente_id)
        nombre = cliente.nombre

        # Creación o apertura de ficha cosmetológica
        crear_ficha_cosmetologica(cliente_id=cliente_id, nombre=nombre)


##############################################################################
##############################################################################
#                    CONTROLADOR VENTANA NUEVOS CLIENTES                     #
##############################################################################
##############################################################################
class NuevoClienteController(QMainWindow):
    
    def __init__(self, main_controller: 'MainController'):
        super().__init__()
        self.ui_cliente = VentanaCliente()
        self.ui_cliente.setupUi(self)
        self.main_controller = main_controller
        self.modelo_cliente = ModeloCliente()

        ######################################################################
        # Llamada a widgets necesarios
        ######################################################################
        self.txt_nombre = self.ui_cliente.txtNombre
        self.txt_cel = self.ui_cliente.txtCelular
        self.txt_email = self.ui_cliente.txtEmail

        self.btn_nuevocliente = self.ui_cliente.btnAgregarCliente

        ######################################################################
        # Asignación de métodos a botones
        ######################################################################
        # Asignación método para agregar nuevos clientes
        self.btn_nuevocliente.clicked.connect(self.nuevo_cliente)


    ##########################################################################
    # Método para crear nuevos clientes
    ##########################################################################
    def nuevo_cliente(self):
        try:
            # Recuperación de valores de campo
            nombre = self.txt_nombre.text().upper() 
            cel = self.txt_cel.text()
            email = self.txt_email.text().lower()

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
            nombre = self.txt_nombre.setText("")
            cel = self.txt_cel.setText("")
            email = self.txt_email.setText("")

            # Actualización de tabla
            self.main_controller.cliente_controller.cargar_clientes()

            # Mensaje de confirmación
            QMessageBox.information(self, "Nuevo Cliente", "Cliente Creado!")

            # Actualización de combobox de clientes interfaz de ventas
            self.main_controller.venta_controller.llenar_cmb_clientes_venta()

            # Cierre de ventana
            self.close()

        # Manejo de excepciones
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
