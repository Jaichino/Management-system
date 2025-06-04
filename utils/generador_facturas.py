##############################################################################
# Importaciones
##############################################################################

import os
from datetime import date

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors

from utils.resouce_path import get_resource_path, get_output_path

##############################################################################
# Función generadora de facturas
##############################################################################
def generar_factura_pdf(
        cliente: str, 
        productos: list, 
        total: float, 
        nro_factura: int, 
        fecha: date, 
        interes: float =0.0
):
    ''' Método para la generación de facturas PDF de una venta determinada

        :param str cliente: Cliente que realizó la compra
        :param list productos: Lista de productos de la venta
        :param total float: Monto total de productos vendidos
        :param int nro_factura: Número de venta correspondiente
        :param date fecha: Fecha de venta
        :param float interes: Recargo de la venta
    '''
    # Ruta de salida
    ruta_facturas = get_output_path('facturas')
    ruta_facturas.mkdir(parents=True, exist_ok=True)

    # Nombre del archivo
    nombre_archivo = f'factura_{nro_factura}_{cliente}.pdf'.replace(" ", "_")
    archivo_pdf = ruta_facturas / nombre_archivo

    # Canvas
    c = canvas.Canvas(str(archivo_pdf), pagesize=letter)
    width, height = letter

    # Logo
    ruta_logo = get_resource_path("view/images/logo_sin_fondo.png")
    if ruta_logo.exists():
        c.drawImage(str(ruta_logo), width/2-150, height - 250, width=300, height=300)

    # Datos del emprendimiento
    c.setFont("Helvetica-Bold", 20)
    c.drawString(50, height - 220, "BLA Estética")

    c.setFont("Helvetica", 12)
    c.drawString(50, height - 240, "Dirección: Hipólito Yrigoyen 561")
    c.drawString(50, height - 260, "Teléfono: 353-4230926")
    c.drawString(50, height - 280, "Email: aichinobrenda@gmail.com")

    c.line(50, height - 300, width - 50, height - 300)

    # Información de venta
    fecha_format = date.strftime(fecha, "%d/%m/%Y")
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 325, f"Venta número #{nro_factura}")

    c.setFont("Helvetica", 12)
    c.drawString(50, height - 345, f"Cliente: {cliente}")
    c.drawString(50, height - 365, f"Fecha: {fecha_format}")

    # Tabla de productos
    c.setFont("Helvetica-Bold", 15)
    c.drawString(50, height - 395, "Detalle de la venta")

    data = [["Producto", "Precio", "Cant", "Subtotal"]] + productos
    table = Table(data, colWidths=[350, 60, 50, 60])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ]))

    # Posición dinámica de la tabla
    table_height = len(data) * 20
    y_position = height - 410 - table_height
    table.wrapOn(c, width, height)
    table.drawOn(c, 50, y_position)

    # Total productos
    c.setFont("Helvetica", 14)
    c.drawString(50, y_position - 60, f"Total de productos: ${total:.0f}")
    y_position -= 30

    # Interés
    c.setFont("Helvetica", 14)
    c.drawString(50, y_position - 60, f"Recargo: ${interes:.0f}")
    y_position -= 30

    # Total
    monto_abonar = total + interes
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y_position - 60, f"Total a pagar: ${monto_abonar:.0f}")
    y_position -= 30

    c.line(50, y_position - 80, width - 50, y_position - 80)

    # Mensaje final
    c.setFont("Helvetica-Bold", 14)
    c.drawString(220, y_position - 100, "Gracias por tu compra :)")

    # Guardado del archivo
    c.save()

    # Abrir el PDF automáticamente 
    os.startfile(archivo_pdf)

    return archivo_pdf
