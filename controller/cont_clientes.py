##############################################################################
# Importaciones
##############################################################################

from typing import TYPE_CHECKING

from PySide6.QtCore import QObject, Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QMainWindow, QMessageBox

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
        self.modelo_tcliente = QStandardItemModel()
        self.modelo_tcliente.setHorizontalHeaderLabels(
            ["ID","Nombre", "Teléfono", "Email"]
        )

        # Seteo de modelo en tabla de clientes
        self.tabla_cliente.setModel(self.modelo_tcliente)

        # Se oculta la columna de id de cliente
        self.tabla_cliente.setColumnHidden(0, True)

        # Seteo de dimensiones fijas de columnas
        self.tabla_cliente.setColumnWidth(1,200)
        self.tabla_cliente.setColumnWidth(2,300)


    ##########################################################################
    # Método para carga de clientes en tabla
    ##########################################################################

    def cargar_clientes(self):
        # Se limpia el modelo antes de cargar clientes
        self.modelo_tcliente.removeRows(0, self.modelo_tcliente.rowCount())

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
        
        # Se crean filas y se cargan al modelo
        for cliente in clientes:
                if cliente.nombre == 'CLIENTE NO REGISTRADO':
                    continue
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
