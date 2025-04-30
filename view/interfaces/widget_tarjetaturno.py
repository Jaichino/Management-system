# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_tarjetaturno.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class WidgetTarjetaTurno(object):
    def setupUi(self, widgetTarjetaTurnos):
        if not widgetTarjetaTurnos.objectName():
            widgetTarjetaTurnos.setObjectName(u"widgetTarjetaTurnos")
        widgetTarjetaTurnos.resize(746, 150)
        widgetTarjetaTurnos.setMinimumSize(QSize(0, 0))
        widgetTarjetaTurnos.setMaximumSize(QSize(16777215, 150))
        widgetTarjetaTurnos.setStyleSheet(u"background-color:white")
        self.gridLayout = QGridLayout(widgetTarjetaTurnos)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.tarjetaTurnos = QWidget(widgetTarjetaTurnos)
        self.tarjetaTurnos.setObjectName(u"tarjetaTurnos")
        self.tarjetaTurnos.setStyleSheet(u"\n"
"\n"
"background-color: #F7E7DC;\n"
"border: 2px solid #7D3928;\n"
"border-radius: 10px\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(self.tarjetaTurnos)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.tarjetaTurnos)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(100, 0))
        self.widget.setMaximumSize(QSize(100, 16777215))
        self.widget.setStyleSheet(u"border:0px;")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.contenedorHora = QWidget(self.widget)
        self.contenedorHora.setObjectName(u"contenedorHora")
        self.contenedorHora.setStyleSheet(u"border: 2px solid #7D3928;\n"
"\n"
"")
        self.gridLayout_2 = QGridLayout(self.contenedorHora)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lblHoraTurno = QLabel(self.contenedorHora)
        self.lblHoraTurno.setObjectName(u"lblHoraTurno")
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(18)
        font.setBold(True)
        self.lblHoraTurno.setFont(font)
        self.lblHoraTurno.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.lblHoraTurno.setStyleSheet(u"color: #7D3928; border: 0px;")
        self.lblHoraTurno.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lblHoraTurno, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.contenedorHora)

        self.contenedorDuracion = QWidget(self.widget)
        self.contenedorDuracion.setObjectName(u"contenedorDuracion")
        self.contenedorDuracion.setStyleSheet(u"border: 2px solid #7D3928;\n"
"")
        self.gridLayout_4 = QGridLayout(self.contenedorDuracion)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lblDuracion = QLabel(self.contenedorDuracion)
        self.lblDuracion.setObjectName(u"lblDuracion")
        self.lblDuracion.setFont(font)
        self.lblDuracion.setStyleSheet(u"color: #7D3928; border: 0px;")
        self.lblDuracion.setScaledContents(False)
        self.lblDuracion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblDuracion.setWordWrap(True)

        self.gridLayout_4.addWidget(self.lblDuracion, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.contenedorDuracion)


        self.horizontalLayout.addWidget(self.widget)

        self.encabezados = QWidget(self.tarjetaTurnos)
        self.encabezados.setObjectName(u"encabezados")
        self.encabezados.setMinimumSize(QSize(140, 0))
        self.encabezados.setMaximumSize(QSize(140, 16777215))
        self.encabezados.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.encabezados.setStyleSheet(u"border: 0px")
        self.verticalLayout_2 = QVBoxLayout(self.encabezados)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.titCliente = QLabel(self.encabezados)
        self.titCliente.setObjectName(u"titCliente")
        font1 = QFont()
        font1.setFamilies([u"Century Gothic"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.titCliente.setFont(font1)
        self.titCliente.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.titCliente.setStyleSheet(u"color: #7D3928;")
        self.titCliente.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.titCliente)

        self.titServicio = QLabel(self.encabezados)
        self.titServicio.setObjectName(u"titServicio")
        self.titServicio.setFont(font1)
        self.titServicio.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.titServicio.setStyleSheet(u"color: #7D3928;")
        self.titServicio.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.titServicio)

        self.titObservacion = QLabel(self.encabezados)
        self.titObservacion.setObjectName(u"titObservacion")
        self.titObservacion.setFont(font1)
        self.titObservacion.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.titObservacion.setStyleSheet(u"color: #7D3928;")
        self.titObservacion.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.titObservacion)

        self.titPrecio = QLabel(self.encabezados)
        self.titPrecio.setObjectName(u"titPrecio")
        self.titPrecio.setFont(font1)
        self.titPrecio.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.titPrecio.setStyleSheet(u"color: #7D3928;")
        self.titPrecio.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.titPrecio)


        self.horizontalLayout.addWidget(self.encabezados)

        self.labelsTurnos = QWidget(self.tarjetaTurnos)
        self.labelsTurnos.setObjectName(u"labelsTurnos")
        self.labelsTurnos.setStyleSheet(u"border: 0px")
        self.verticalLayout_3 = QVBoxLayout(self.labelsTurnos)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lblCliente = QLabel(self.labelsTurnos)
        self.lblCliente.setObjectName(u"lblCliente")
        font2 = QFont()
        font2.setFamilies([u"Century Gothic"])
        font2.setPointSize(12)
        self.lblCliente.setFont(font2)
        self.lblCliente.setStyleSheet(u"color: #7D3928;")

        self.verticalLayout_3.addWidget(self.lblCliente)

        self.lblServicio = QLabel(self.labelsTurnos)
        self.lblServicio.setObjectName(u"lblServicio")
        self.lblServicio.setFont(font2)
        self.lblServicio.setStyleSheet(u"color: #7D3928;")

        self.verticalLayout_3.addWidget(self.lblServicio)

        self.lblObservacion = QLabel(self.labelsTurnos)
        self.lblObservacion.setObjectName(u"lblObservacion")
        self.lblObservacion.setFont(font2)
        self.lblObservacion.setStyleSheet(u"color: #7D3928;")

        self.verticalLayout_3.addWidget(self.lblObservacion)

        self.lblPrecio = QLabel(self.labelsTurnos)
        self.lblPrecio.setObjectName(u"lblPrecio")
        self.lblPrecio.setFont(font2)
        self.lblPrecio.setStyleSheet(u"color: #7D3928;")

        self.verticalLayout_3.addWidget(self.lblPrecio)


        self.horizontalLayout.addWidget(self.labelsTurnos)

        self.widget_4 = QWidget(self.tarjetaTurnos)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(120, 16777215))
        self.widget_4.setStyleSheet(u"border: 0px")
        self.verticalLayout_4 = QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.widget_4)
        self.widget_7.setObjectName(u"widget_7")

        self.verticalLayout_4.addWidget(self.widget_7)

        self.botonera = QWidget(self.widget_4)
        self.botonera.setObjectName(u"botonera")
        self.botonera.setMinimumSize(QSize(120, 0))
        self.botonera.setMaximumSize(QSize(120, 60))
        self.gridLayout_3 = QGridLayout(self.botonera)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btnCancelarTurno = QPushButton(self.botonera)
        self.btnCancelarTurno.setObjectName(u"btnCancelarTurno")
        self.btnCancelarTurno.setMinimumSize(QSize(100, 30))
        self.btnCancelarTurno.setMaximumSize(QSize(100, 30))
        self.btnCancelarTurno.setFont(font2)
        self.btnCancelarTurno.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnCancelarTurno.setStyleSheet(u"QPushButton {\n"
"	color: #7D3928;\n"
"	border: 1px solid;\n"
"	border-radius: 5px;\n"
"	border-color: #DFAA98;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	font-weight: bold;\n"
"	color: #7D3928;\n"
"	border-radius: 5px;\n"
"	border-color: #DFAA98;\n"
"	background-color: #F7E0D3;\n"
"	\n"
"}")

        self.gridLayout_3.addWidget(self.btnCancelarTurno, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.botonera)


        self.horizontalLayout.addWidget(self.widget_4)


        self.gridLayout.addWidget(self.tarjetaTurnos, 0, 0, 1, 1)


        self.retranslateUi(widgetTarjetaTurnos)

        QMetaObject.connectSlotsByName(widgetTarjetaTurnos)
    # setupUi

    def retranslateUi(self, widgetTarjetaTurnos):
        widgetTarjetaTurnos.setWindowTitle(QCoreApplication.translate("widgetTarjetaTurnos", u"TarjetaTurno", None))
        self.lblHoraTurno.setText(QCoreApplication.translate("widgetTarjetaTurnos", u"18:00", None))
        self.lblDuracion.setText(QCoreApplication.translate("widgetTarjetaTurnos", u"120 min", None))
        self.titCliente.setText(QCoreApplication.translate("widgetTarjetaTurnos", u"Cliente:", None))
        self.titServicio.setText(QCoreApplication.translate("widgetTarjetaTurnos", u"Servicio:", None))
        self.titObservacion.setText(QCoreApplication.translate("widgetTarjetaTurnos", u"Observaci\u00f3n: ", None))
        self.titPrecio.setText(QCoreApplication.translate("widgetTarjetaTurnos", u"Precio servicio:", None))
        self.lblCliente.setText(QCoreApplication.translate("widgetTarjetaTurnos", u"TextLabel", None))
        self.lblServicio.setText(QCoreApplication.translate("widgetTarjetaTurnos", u"TextLabel", None))
        self.lblObservacion.setText(QCoreApplication.translate("widgetTarjetaTurnos", u"TextLabel", None))
        self.lblPrecio.setText(QCoreApplication.translate("widgetTarjetaTurnos", u"TextLabel", None))
        self.btnCancelarTurno.setText(QCoreApplication.translate("widgetTarjetaTurnos", u"Cancelar", None))
    # retranslateUi

