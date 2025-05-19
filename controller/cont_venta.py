##############################################################################
# Importaciones
##############################################################################

from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtGui import QStandardItem, QStandardItemModel
from view.interfaces.ventana_detalleventa import VentanaDetalleVenta
from model.modelo_venta import ModeloVentas
from utils.generador_facturas import generar_factura_pdf

##############################################################################
# Controlador ventana detalle de venta
##############################################################################

class DetalleVentaController(QDialog):

    def __init__(self, main_controller, nro_venta: int):
        super().__init__()
        self.ui_detalleventa = VentanaDetalleVenta()
        self.ui_detalleventa.setupUi(self)
        self.main_controller = main_controller
        self.nro_venta = nro_venta

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

        # Inicialización de la ventana detalle venta con venta correspondiente
        self.cargar_detalle_venta(nro_venta=nro_venta)

        # Asignación método generación de facturas pdf
        self.ui_detalleventa.btnGenFactura.clicked.connect(
            self.imprimir_factura
        )


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


    # Generación de factura pdf venta nro_venta
    def imprimir_factura(self):
        ''' Método para generar generar la factura PDF de la compra que se ha
            seleccionado desde la tabla consulta de ventas.
        '''
        # Obtención detalle de ventas
        detalle = ModeloVentas.consulta_detalleventa(nro_venta=self.nro_venta)

        # Armado lista productos para pasar parametro a función
        productos = []

        for det in detalle:
            nombre_producto = det.producto.descripcion
            precio = det.precio_unitario
            cantidad = det.cantidad
            subtotal = precio * cantidad

            productos.append([  nombre_producto,
                                f'$ {precio:.0f}', 
                                cantidad, 
                                f'$ {subtotal:.0f}'
                            ])
        
        # Obtención informacion de venta
        venta = ModeloVentas.obtener_venta(nro_venta=self.nro_venta)
        if venta:
            cliente = venta.cliente.nombre
            fecha = venta.fecha_venta
            total = venta.monto_total
            interes = venta.interes
        
        # Generación de factura PDF
        generar_factura_pdf(
            cliente=cliente,
            productos=productos,
            total=total,
            nro_factura=self.nro_venta,
            fecha=fecha,
            interes=interes
        )

        # Bloqueo de botón
        self.ui_detalleventa.btnGenFactura.setEnabled(False)