##############################################################################
# Importaciones
##############################################################################

from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QStandardItem, QStandardItemModel
from view.interfaces.ventana_detalleventa import VentanaDetalleVenta
from model.modelo_venta import ModeloVentas

##############################################################################
# Controlador ventana detalle de venta
##############################################################################

class DetalleVentaController(QDialog):

    def __init__(self, main_controller, nro_venta: int):
        super().__init__()
        self.ui_detalleventa = VentanaDetalleVenta()
        self.ui_detalleventa.setupUi(self)
        self.main_controller = main_controller

        # Definición del modelo de tabla para ver detalle venta
        self.modelo_dventa = QStandardItemModel()
        self.modelo_dventa.setHorizontalHeaderLabels(
            ['id','Producto','Precio', 'Cantidad', 'Subtotal']
        )
        self.ui_detalleventa.tablaDetalleVenta.setModel(self.modelo_dventa)
        self.ui_detalleventa.tablaDetalleVenta.setColumnHidden(0, True)
        self.ui_detalleventa.tablaDetalleVenta.setColumnWidth(1, 490)
        self.ui_detalleventa.tablaDetalleVenta.setColumnWidth(2,100)
        self.ui_detalleventa.tablaDetalleVenta.setColumnWidth(3,80)

        self.cargar_detalle_venta(nro_venta=nro_venta)


    # Método para cargar el detalle de venta seleccionado en consulta venta
    def cargar_detalle_venta(self, nro_venta: int):
        # Se busca el detalle de venta segun nro_venta
        detalle = ModeloVentas.consulta_detalleventa(nro_venta=nro_venta)

        # Se pone número de venta en título
        self.ui_detalleventa.lblTitulo.setText(f"Detalle de venta #{nro_venta}")

        # Completado de información de venta en lables
        total_prod = detalle[0].venta.monto_total
        interes = detalle[0].venta.interes
        tot_abonar = total_prod + interes
        self.ui_detalleventa.lblTotalProductos.setText(
            f"Total productos: $ {total_prod}"
        )
        self.ui_detalleventa.lblTotalInteres.setText(f'Interes: $ {interes}')
        self.ui_detalleventa.lblTotalAbonar.setText(
            f"Total a abonar: $ {tot_abonar}"
        )

        # Se carga información a la tabla de detalle venta
        for det in detalle:
            producto = det.producto.descripcion
            precio = det.precio_unitario
            cantidad = det.cantidad
            subtotal = precio * cantidad

            fila = [
                QStandardItem(det.nro_venta),
                QStandardItem(producto),
                QStandardItem(f'$ {precio:.0f}'),
                QStandardItem(str(cantidad)),
                QStandardItem(f'$ {subtotal:.0f}')
            ]

            self.modelo_dventa.appendRow(fila)
