##############################################################################
# Importaciones
##############################################################################

from view.interfaces.ventana_clientes import VentanaCliente
from model.modelo_clientes import ModeloCliente
from PySide6.QtWidgets import QMainWindow, QMessageBox

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