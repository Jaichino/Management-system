##############################################################################
# Importaciones
##############################################################################

from view.interfaces.ventana_nuevoproducto import VentanaNuevoProducto
from PySide6.QtWidgets import QDialog

##############################################################################
# Controlador ventana Producto
##############################################################################

class NuevoProductoController(QDialog):
    def __init__(self):
        super().__init__()
        self.ventana_nuevoprod = VentanaNuevoProducto()
        self.ventana_nuevoprod.setupUi(self)

        # Hacer foco en campo de codigo
        self.ventana_nuevoprod.txtCodigo.setFocus()