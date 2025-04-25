##############################################################################
# Importaciones
##############################################################################

from controller.main_controller import MainController
from PySide6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication([])
    controlador = MainController()
    controlador.show()
    app.exec()