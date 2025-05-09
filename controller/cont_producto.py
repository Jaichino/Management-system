##############################################################################
# Importaciones
##############################################################################

from datetime import date
from PySide6.QtWidgets import QDialog, QMessageBox
from view.interfaces.ventana_nuevoproducto import VentanaNuevoProducto
from model.modelo_producto import ModeloProducto

##############################################################################
# Controlador ventana Producto
##############################################################################

class NuevoProductoController(QDialog):
    def __init__(self, main_controller):
        super().__init__()
        self.ventana_nuevoprod = VentanaNuevoProducto()
        self.ventana_nuevoprod.setupUi(self)
        self.modelo_producto = ModeloProducto()
        self.main_controller = main_controller

        # Hacer foco en campo de código
        self.ventana_nuevoprod.txtCodigo.setFocus()

        # Evento autocompletado de código
        self.ventana_nuevoprod.txtCodigo.textChanged.connect(
            self.autocompletar_descripcion
        )

        # Asignación de métodos a botones
        self.ventana_nuevoprod.btnGuardarProducto.clicked.connect(
            self.crear_producto
        )

    ##########################################################################
    # Método para carga de nuevos productos
    ##########################################################################
    def crear_producto(self):
        # Recuperación de valores de campos
        codigo = self.ventana_nuevoprod.txtCodigo.text()
        desc = self.ventana_nuevoprod.txtDescripcion.text()
        precio = self.ventana_nuevoprod.txtPrecio.text()
        stock = self.ventana_nuevoprod.txtStock.text()
        venc_qt = self.ventana_nuevoprod.dateEditVencimiento.date()
        
        # Verificación de completado de campos
        if codigo == '' or desc == '' or precio == '' or stock == '':
            QMessageBox.critical(
                self,
                'Nuevo Producto',
                'Se deben completar todos los campos'            
            )
            return
    
        try:
            # Ajuste de formatos
            precio = float(precio)
            stock = int(stock)
            vencimiento = date(
                year=venc_qt.year(),
                month=venc_qt.month(),
                day=venc_qt.day()
            )

            # Verificación de que no existe producto con mismo vencimiento
            if self.modelo_producto.obtener_nro_producto(codigo, vencimiento):
                QMessageBox.warning(
                    self,
                    'Nuevo Producto',
                    'El producto ya existe!, buscar y actualizar stock'
                )
                return
            
            # Se carga producto en base de datos
            self.modelo_producto.nuevo_producto(
                codigo, desc, precio, stock, vencimiento, True
            )

            # Mensaje de confirmación y limpieza de campos
            QMessageBox.information(
                self,
                'Nuevo Producto',
                f'Producto ({desc}) agregado a stock!'
            )
            self.ventana_nuevoprod.txtPrecio.setText("")
            self.ventana_nuevoprod.txtStock.setText("")
            self.ventana_nuevoprod.txtPrecio.setFocus()

            # Actualización de tabla
            self.main_controller.cargar_productos()

        # Manejo de excepciones
        except ValueError:
            QMessageBox.critical(
                self,
                'Nuevo Producto',
                'Verificar campos !'            
            )
        except Exception as e:
            QMessageBox.critical(
                self,
                'Nuevo Producto',
                f'Error inesperado - {e}'            
            )

    ##########################################################################
    # Método para autocompletar descripción al introducir código en campo
    ##########################################################################
    def autocompletar_descripcion(self):
        # Limpieza de campo al inicio
        self.ventana_nuevoprod.txtDescripcion.setText("")

        # Obtención código campo
        codigo = self.ventana_nuevoprod.txtCodigo.text()
        
        # Busca de productos con ese codigo
        producto = self.modelo_producto.listado_productos(codigo=codigo)
        
        # Se define para evitar error
        descripcion = ''

        # Seteo de descripción y foco en siguiente campo
        if producto:
            descripcion = producto[0].descripcion
            # Seteo de campo descripción
            self.ventana_nuevoprod.txtDescripcion.setText(descripcion)
            # Foco en campo precio
            self.ventana_nuevoprod.txtPrecio.setFocus()
        
        