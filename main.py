##############################################################################
# Importaciones
##############################################################################

from controller.cont_principal import MainController
from PySide6.QtWidgets import QApplication

##############################################################################
# Ejecución del sistema
##############################################################################

if __name__ == '__main__':
    app = QApplication([])
    controlador = MainController()
    controlador.show()
    app.exec()