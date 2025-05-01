##############################################################################
# Importaciones
##############################################################################

from view.interfaces.ventana_servicios import VentanaServicio
from view.interfaces.widget_tarjetaservicio import WidgetTarjetaServicio
from model.modelo_servicios import ModeloServicio
from PySide6.QtWidgets import QMainWindow, QWidget, QMessageBox

##############################################################################
# Controlador Widget - Tarjetas de Servicios
##############################################################################
class TarjetaServiciosController(QWidget):
    def __init__(self):
        super().__init__()
        self.widget_tserv = WidgetTarjetaServicio()
        self.widget_tserv.setupUi(self)

##############################################################################
# Controlador ventana nuevos servicios
##############################################################################
class ServicioController(QMainWindow):
    
    def __init__(self, main_controller):
        super().__init__()
        self.ui_servicio = VentanaServicio()
        self.ui_servicio.setupUi(self)
        self.model_serv = ModeloServicio()
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
                self.model_serv.nuevo_servicio(nombre, duracion, precio)
                QMessageBox.information(
                    self,
                    'Nuevo Servicio',
                    f'{nombre} agregado a listado de servicios!'
                )

            elif self.modo == 'editar':
                self.model_serv.editar_servicio(
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