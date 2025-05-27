##############################################################################
# Importaciones
##############################################################################

from typing import TYPE_CHECKING

from PySide6.QtWidgets import (
    QMainWindow, QWidget, QMessageBox, QSpacerItem, QSizePolicy
)
from PySide6.QtCore import QObject

from view.interfaces.ventana_servicios import VentanaServicio
from view.interfaces.widget_tarjetaservicio import WidgetTarjetaServicio
from model.modelo_servicio import ModeloServicio
if TYPE_CHECKING:
    from controller.cont_principal import MainController


##############################################################################
##############################################################################
#               Controlador Widget - Tarjetas de Servicios                   #
##############################################################################
##############################################################################
class TarjetaServiciosController(QWidget):
    def __init__(self):
        super().__init__()
        self.widget_tserv = WidgetTarjetaServicio()
        self.widget_tserv.setupUi(self)



##############################################################################
##############################################################################
#                     CONTROLADOR PRINCIPAL SERVICIOS                        #
##############################################################################
##############################################################################
class ServiciosController(QObject):

    def __init__(self, main_controller: 'MainController'):
        super().__init__()
        self.main_controller = main_controller

        ######################################################################
        # Llamada a widgets necesarios
        ######################################################################
        self.cont_servicios = main_controller.main_ui.contenedorServicios


        ######################################################################
        # Inicialización de modelos
        ######################################################################
        # Visualización tarjetas de servicios
        self.mostrar_servicios()


    ##########################################################################
    # Posicionamiento de tarjetas de Servicios
    ##########################################################################
    def mostrar_servicios(self):
        # Definición del contenedor de las tarjetas
        contenedor = self.cont_servicios.layout()
        contenedor.setContentsMargins(5,5,5,5)
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
                    f'$ {serv.precio:.0f}'
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


    ##########################################################################
    # Método eliminación de servicio
    ##########################################################################
    def eliminar_servicio(self, id_servicio):
        # Consulta de eliminación
        eliminar = QMessageBox.question(
            self.main_controller,
            "Servicios",
            "Eliminar el servicio?"
        )
        if eliminar == QMessageBox.Yes:
            # Eliminación del servicio
            ModeloServicio.eliminar_servicio(id_servicio)
            QMessageBox.information(
                self.main_controller,
                'Servicios',
                'Servicio Eliminado'
            )

            # Actualización del listado
            self.mostrar_servicios()


    ##########################################################################
    # Método edición de servicios
    ##########################################################################
    def servicio_editar(self, servicio_id):
        # Se obtiene el objeto Servicio a partir del id guardado en boton
        servicio = ModeloServicio.info_servicio(servicio_id)
        # Se inicializa ventana con metodo cargar_datos
        ventana = NuevoServicioController(self.main_controller)
        ventana.cargar_datos(servicio)
        ventana.show()
        # Se debe guardar la referencia para que no se destruya la ventana
        self.ventana_servicio = ventana



##############################################################################
##############################################################################
#                   CONTROLADOR VENTANA NUEVOS SERVICIOS                     #
##############################################################################
##############################################################################

class NuevoServicioController(QMainWindow):
    
    def __init__(self, main_controller: 'MainController'):
        super().__init__()
        self.ui_servicio = VentanaServicio()
        self.ui_servicio.setupUi(self)
        self.model_serv = ModeloServicio()
        self.main_controller = main_controller

        ######################################################################
        # Llamada a widgets necesarios
        ######################################################################
        self.txt_nombre = self.ui_servicio.txtNombre
        self.txt_duracion = self.ui_servicio.txtDuracion
        self.txt_precio = self.ui_servicio.txtPrecio

        self.btn_guardar_servicio = self.ui_servicio.btnGuardarServicio

        ######################################################################
        # Configuración de variables iniciales
        ######################################################################
        # Variable para decidir entre edición o creación de servicio
        self.modo = 'nuevo'
        # Variable para guardar el id del servicio
        self.id_servicio = None
    

        ######################################################################
        # Asignación de métodos a botones
        ######################################################################
        # Asignación método nuevo_servicio a boton btnGuardarServicio
        self.btn_guardar_servicio.clicked.connect(self.guardar_servicio)


    ##########################################################################
    # Método guardar servicio (Decicide entre crear y editar)
    ##########################################################################
    def guardar_servicio(self):
        # Recuperación de valores de campos
        nombre = self.txt_nombre.text().upper()
        duracion = self.txt_duracion.text()
        precio = self.txt_precio.text()

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
            self.txt_nombre.setText("")
            self.txt_duracion.setText("")
            self.txt_precio.setText("")

            # Actualización del listado de servicios
            self.main_controller.servicio_controller.mostrar_servicios()

            # Cierre de ventana al finalizar la carga
            self.close()

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


    ##########################################################################
    # Método para carga de información en ventana nuevo servicio
    ##########################################################################
    def cargar_datos(self, servicio=None):
        ''' Método para decidir si al presionar boton btnGuardarServicio, se 
            edita un servicio seleccionado o se carga un nuevo servicio.

            Se llama desde ServicioController y se le pasa el servicio que se
            selecciona en una determinada tarjeta. Se setea el self.modo a
            editar para que luego el metodo guardar_servicio no lo cargue como
            uno nuevo, sino que aplique el metodo editar_servicio
        '''
        if servicio:
            self.modo = 'editar'
            self.id_servicio = servicio.id
            self.txt_nombre.setText(servicio.nombre)
            self.txt_duracion.setText(str(servicio.duracion))
            self.txt_precio.setText(f'{servicio.precio:.0f}')
        else:
            self.modo = 'nuevo'
            self.id_servicio = None
