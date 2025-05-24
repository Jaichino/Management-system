##############################################################################
# Importaciones
##############################################################################

from typing import TYPE_CHECKING
from datetime import date, datetime

from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import QObject, Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem

from view.interfaces.ventana_nuevoproducto import VentanaNuevoProducto
from model.modelo_producto import ModeloProducto
if TYPE_CHECKING:
    from controller.cont_principal import MainController

##############################################################################
##############################################################################
#               Controlador ventana Productos (StackedWidget)                #
##############################################################################
##############################################################################
class ProductoController(QObject):
    
    def __init__(self, main_controller: 'MainController'):
        super().__init__()
        self.main_controller = main_controller

        ######################################################################
        # Llamada a widgets necesarios
        ######################################################################

        self.tabla_productos = main_controller.main_ui.tablaProductos
        self.txt_codigo = main_controller.main_ui.txtCodigoProd
        self.txt_descripcion = main_controller.main_ui.txtDescripcionProd
        self.btn_filtrar = main_controller.main_ui.btnFiltrarProductos
        self.btn_eliminar = main_controller.main_ui.btnEliminarProducto
        self.btn_nuevoproducto = main_controller.main_ui.btnNuevoProducto


        ######################################################################
        # Inicialización de modelos
        ######################################################################
        # Seteo de modelo en tabla de productos
        self.configurar_modelo_tabla_productos()
        
        # Inicialización de productos cargados en tabla
        self.cargar_productos()


        ######################################################################
        # Asignación de métodos a botones
        ######################################################################        
        # Asignación método para filtrado de productos
        self.btn_filtrar.clicked.connect(
            self.cargar_productos
        )

        # Asignación método para eliminación de productos
        self.btn_eliminar.clicked.connect(
            self.eliminar_producto
        )

        ######################################################################
        # Configuración de eventos
        ######################################################################
        # Conexión evento para edición de productos
        self.model_tproducto.itemChanged.connect(self.editar_producto)


    # MÉTODOS PARA INICIALIZACIÓN DE INTERFAZ Y CONFIGURACIÓN DE MODELOS
    ##########################################################################

    ##########################################################################
    # Método para configuración de modelo en tabla de productos
    ##########################################################################
    def configurar_modelo_tabla_productos(self):
        ''' Método para la configuración del modelo para la tabla de productos
        '''
        # Se establece modelo y headers del modelo
        self.model_tproducto = QStandardItemModel()
        self.model_tproducto.setHorizontalHeaderLabels(
            ["id", "Código", "Producto", "Precio", "Stock", "Vencimiento"]
        )

        # Seteo de modelo
        self.tabla_productos.setModel(self.model_tproducto)

        # Se oculta columna "id" que guarda el nro_producto
        self.tabla_productos.setColumnHidden(0, True)

        # Configuración anchos de columnas
        self.tabla_productos.setColumnWidth(1, 150)
        self.tabla_productos.setColumnWidth(2, 400)


    # MÉTODOS PARA REALIZAR ACCIONES EN MODELO
    ##########################################################################
    
    ##########################################################################
    # Método para carga de productos en tabla
    ##########################################################################
    def cargar_productos(self):
        # Limpieza de modelo
        self.model_tproducto.removeRows(0, self.model_tproducto.rowCount())

        # Verificación de codigo o descripcion y recuperacion productos
        codigo = self.txt_codigo.text()
        descripcion = self.txt_descripcion.text()

        codigo = None if codigo == '' else codigo
        descripcion = None if descripcion == '' else descripcion

        if codigo is None and descripcion is None:
            productos = ModeloProducto.listado_productos(
                codigo=None, descripcion=None
            )

        else:
            productos = ModeloProducto.listado_productos(
                codigo=codigo, descripcion=descripcion
            )
            if not productos:
                QMessageBox.information(
                    self.main_controller,
                    "Busqueda de productos",
                    "No se encontraron productos!"
                )
                return
        
        # Ingreso de productos en tabla
        for producto in productos:
            venc = date.strftime(producto.vencimiento, "%d/%m/%Y")
            fila = [
                QStandardItem(str(producto.nro_producto)),
                QStandardItem(producto.codigo_producto),
                QStandardItem(producto.descripcion),
                QStandardItem(f'$ {str(producto.precio_unitario)}'),
                QStandardItem(str(producto.stock)),
                QStandardItem(venc)
            ]
            # Alineado de valores
            for item in fila:
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            
            # Agregado de fila a modelo
            self.model_tproducto.appendRow(fila)


    ##########################################################################
    # Método para edición de productos
    ##########################################################################
    def editar_producto(self):
        # Se busca fila seleccionada
        fila = self.tabla_productos.currentIndex().row()

        # Obtención del nro_producto en base a selección
        nro_producto = self.model_tproducto.item(fila, 0).text()

        # Recuperación campos a modificar
        descripcion = self.model_tproducto.item(fila,2).text()
        precio = self.model_tproducto.item(fila,3).text()
        stock = self.model_tproducto.item(fila,4).text()
        vencimiento = self.model_tproducto.item(fila,5).text()

        try:
            if not precio.startswith("$ "):
                precio = float(precio)
            else:
                precio = float(precio[2:])
            stock = int(stock)
            vencimiento = datetime.strptime(vencimiento, "%d/%m/%Y").date()

            # Llamado de método para editar producto
            ModeloProducto.actualizar_producto(
                nro_producto=nro_producto,
                descripcion=descripcion,
                precio=precio,
                stock=stock,
                vencimiento=vencimiento
            )
            # Mensaje de confirmación
            QMessageBox.information(
                self.main_controller,
                'Edición de Producto',
                'Producto modificado!'            
            )
            self.cargar_productos()

        except ValueError:
            QMessageBox.critical(
                self.main_controller,
                'Edición de Producto',
                'Verificar campos !'            
            )
            self.cargar_productos()

        except Exception as e:
            QMessageBox.critical(
                self.main_controller,
                'Nuevo Producto',
                f'Error inesperado - {e}'            
            )


    #########################################################################
    # Método para eliminación de productos
    ##########################################################################
    def eliminar_producto(self):
        # Se busca fila seleccionada
        fila = self.tabla_productos.currentIndex().row()

        # Comprobación de selección
        if fila == -1:
            QMessageBox.warning(
                self.main_controller,
                'Eliminación de producto',
                'Tenes que seleccionar un producto!'
            )
            return
        
        # Obtención del nro_producto en base a selección
        nro_producto = self.model_tproducto.item(fila, 0).text()
        descripcion = self.model_tproducto.item(fila, 2).text()

        # Consulta de eliminación
        eliminar = QMessageBox.question(
            self.main_controller,
            'Eliminación de producto',
            f'Eliminar el producto {descripcion}?'
        )
        if eliminar == QMessageBox.Yes:
            ModeloProducto.eliminar_producto(nro_producto)
            # Mensaje de confirmación
            QMessageBox.information(
                self.main_controller,
                'Eliminación de Producto',
                f'Producto ({descripcion}) eliminado!'            
            )
            self.cargar_productos()



##############################################################################
##############################################################################
#                   CONTROLADOR VENTANA NUEVO PRODUCTO                       #
##############################################################################
##############################################################################
class NuevoProductoController(QDialog):
    def __init__(self, main_controller: 'MainController'):
        super().__init__()
        self.ventana_nuevoprod = VentanaNuevoProducto()
        self.ventana_nuevoprod.setupUi(self)
        self.modelo_producto = ModeloProducto()
        self.main_controller = main_controller

        ######################################################################
        # Llamada a widgets necesarios
        ######################################################################
        self.txt_codigo = self.ventana_nuevoprod.txtCodigo
        self.txt_descripcion = self.ventana_nuevoprod.txtDescripcion
        self.txt_precio = self.ventana_nuevoprod.txtPrecio
        self.txt_stock = self.ventana_nuevoprod.txtStock
        self.date_vencimiento = self.ventana_nuevoprod.dateEditVencimiento

        self.btn_guardar_producto = self.ventana_nuevoprod.btnGuardarProducto

        ######################################################################
        # Configuraciones iniciales de interfaz
        ######################################################################
        # Hacer foco en campo de código
        self.txt_codigo.setFocus()

        ######################################################################
        # Asignación de métodos a botones
        ######################################################################\
        # Asignación método guardar nuevo producto
        self.btn_guardar_producto.clicked.connect(self.crear_producto)

        ######################################################################
        # Asignación de eventos
        ######################################################################
        # Evento autocompletado de código
        self.txt_codigo.textChanged.connect(self.autocompletar_descripcion)


    ##########################################################################
    # Método para carga de nuevos productos
    ##########################################################################
    def crear_producto(self):
        # Recuperación de valores de campos
        codigo = self.txt_codigo.text()
        desc = self.txt_descripcion.text()
        precio = self.txt_precio.text()
        stock = self.txt_stock.text()
        venc_qt = self.date_vencimiento.date()
        
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
            self.txt_precio.setText("")
            self.txt_stock.setText("")
            self.txt_precio.setFocus()

            # Actualización de tabla
            self.main_controller.producto_controller.cargar_productos()

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
        self.txt_descripcion.setText("")

        # Obtención código campo
        codigo = self.txt_codigo.text()
        
        # Busca de productos con ese codigo
        producto = self.modelo_producto.listado_productos(codigo=codigo)
        
        # Se define para evitar error
        descripcion = ''

        # Seteo de descripción y foco en siguiente campo
        if producto:
            descripcion = producto[0].descripcion
            # Seteo de campo descripción
            self.txt_descripcion.setText(descripcion)
            # Foco en campo precio
            self.txt_precio.setFocus()
