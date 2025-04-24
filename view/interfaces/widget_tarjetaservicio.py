# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_tarjetaservicio.ui'
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

class WidgetTarjetaServicio(object):
    def setupUi(self, widgetTarjetaServicio):
        if not widgetTarjetaServicio.objectName():
            widgetTarjetaServicio.setObjectName(u"widgetTarjetaServicio")
        widgetTarjetaServicio.resize(750, 150)
        widgetTarjetaServicio.setMinimumSize(QSize(750, 150))
        widgetTarjetaServicio.setMaximumSize(QSize(750, 150))
        widgetTarjetaServicio.setStyleSheet(u"background-color:white")
        self.gridLayout = QGridLayout(widgetTarjetaServicio)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.tarjetaServicio = QWidget(widgetTarjetaServicio)
        self.tarjetaServicio.setObjectName(u"tarjetaServicio")
        self.tarjetaServicio.setStyleSheet(u"background-color: #EDE2E0;\n"
"border: 2px solid #C18484;\n"
"border-radius: 10px;")
        self.horizontalLayout = QHBoxLayout(self.tarjetaServicio)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.widget = QWidget(self.tarjetaServicio)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"border: 0px")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.encabezadosServicios = QWidget(self.widget)
        self.encabezadosServicios.setObjectName(u"encabezadosServicios")
        self.encabezadosServicios.setMaximumSize(QSize(120, 16777215))
        self.verticalLayout = QVBoxLayout(self.encabezadosServicios)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 0, 0, 0)
        self.encabezadoServicio = QLabel(self.encabezadosServicios)
        self.encabezadoServicio.setObjectName(u"encabezadoServicio")
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(16)
        font.setBold(True)
        self.encabezadoServicio.setFont(font)
        self.encabezadoServicio.setStyleSheet(u"color: #C18484;\n"
"font-weight: bold;")

        self.verticalLayout.addWidget(self.encabezadoServicio)

        self.encabezadoDuracion = QLabel(self.encabezadosServicios)
        self.encabezadoDuracion.setObjectName(u"encabezadoDuracion")
        self.encabezadoDuracion.setFont(font)
        self.encabezadoDuracion.setStyleSheet(u"color: #C18484;\n"
"font-weight: bold;")

        self.verticalLayout.addWidget(self.encabezadoDuracion)

        self.encabezadoPrecio = QLabel(self.encabezadosServicios)
        self.encabezadoPrecio.setObjectName(u"encabezadoPrecio")
        self.encabezadoPrecio.setFont(font)
        self.encabezadoPrecio.setStyleSheet(u"color: #C18484;\n"
"font-weight: bold;")

        self.verticalLayout.addWidget(self.encabezadoPrecio)


        self.horizontalLayout_2.addWidget(self.encabezadosServicios)

        self.contenedorLabels = QWidget(self.widget)
        self.contenedorLabels.setObjectName(u"contenedorLabels")
        self.verticalLayout_2 = QVBoxLayout(self.contenedorLabels)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lblServicio = QLabel(self.contenedorLabels)
        self.lblServicio.setObjectName(u"lblServicio")
        font1 = QFont()
        font1.setFamilies([u"Century Gothic"])
        font1.setPointSize(16)
        self.lblServicio.setFont(font1)
        self.lblServicio.setStyleSheet(u"color: #C18484")

        self.verticalLayout_2.addWidget(self.lblServicio)

        self.lblDuracion = QLabel(self.contenedorLabels)
        self.lblDuracion.setObjectName(u"lblDuracion")
        self.lblDuracion.setFont(font1)
        self.lblDuracion.setStyleSheet(u"color: #C18484")

        self.verticalLayout_2.addWidget(self.lblDuracion)

        self.lblPrecio = QLabel(self.contenedorLabels)
        self.lblPrecio.setObjectName(u"lblPrecio")
        self.lblPrecio.setFont(font1)
        self.lblPrecio.setStyleSheet(u"color: #C18484")

        self.verticalLayout_2.addWidget(self.lblPrecio)


        self.horizontalLayout_2.addWidget(self.contenedorLabels)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_3 = QWidget(self.tarjetaServicio)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(200, 16777215))
        self.widget_3.setStyleSheet(u"border:0px;")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_3.addWidget(self.widget_2)

        self.contenedorBotones = QWidget(self.widget_3)
        self.contenedorBotones.setObjectName(u"contenedorBotones")
        self.contenedorBotones.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.verticalLayout_4 = QVBoxLayout(self.contenedorBotones)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btnEditarServicio = QPushButton(self.contenedorBotones)
        self.btnEditarServicio.setObjectName(u"btnEditarServicio")
        self.btnEditarServicio.setMaximumSize(QSize(100, 30))
        font2 = QFont()
        font2.setFamilies([u"Century Gothic"])
        font2.setPointSize(12)
        self.btnEditarServicio.setFont(font2)
        self.btnEditarServicio.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnEditarServicio.setStyleSheet(u"QPushButton {\n"
"	color: #C18484;\n"
"	border: 1px solid #C18484;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #C18484;\n"
"	border: 2px solid #C18484;\n"
"	border-radius: 5px;\n"
"	font-weight: bold;\n"
"}")

        self.verticalLayout_4.addWidget(self.btnEditarServicio)

        self.btnEliminarServicio = QPushButton(self.contenedorBotones)
        self.btnEliminarServicio.setObjectName(u"btnEliminarServicio")
        self.btnEliminarServicio.setMaximumSize(QSize(100, 30))
        self.btnEliminarServicio.setFont(font2)
        self.btnEliminarServicio.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnEliminarServicio.setStyleSheet(u"QPushButton {\n"
"	color: #C18484;\n"
"	border: 1px solid #C18484;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #C18484;\n"
"	border: 2px solid #C18484;\n"
"	border-radius: 5px;\n"
"	font-weight: bold;\n"
"}")

        self.verticalLayout_4.addWidget(self.btnEliminarServicio)


        self.verticalLayout_3.addWidget(self.contenedorBotones)


        self.horizontalLayout.addWidget(self.widget_3)


        self.gridLayout.addWidget(self.tarjetaServicio, 0, 0, 1, 1)


        self.retranslateUi(widgetTarjetaServicio)

        QMetaObject.connectSlotsByName(widgetTarjetaServicio)
    # setupUi

    def retranslateUi(self, widgetTarjetaServicio):
        widgetTarjetaServicio.setWindowTitle(QCoreApplication.translate("widgetTarjetaServicio", u"TarjetaServicio", None))
        self.encabezadoServicio.setText(QCoreApplication.translate("widgetTarjetaServicio", u"Servicio:", None))
        self.encabezadoDuracion.setText(QCoreApplication.translate("widgetTarjetaServicio", u"Duraci\u00f3n:", None))
        self.encabezadoPrecio.setText(QCoreApplication.translate("widgetTarjetaServicio", u"Precio:", None))
        self.lblServicio.setText(QCoreApplication.translate("widgetTarjetaServicio", u"TextLabel", None))
        self.lblDuracion.setText(QCoreApplication.translate("widgetTarjetaServicio", u"TextLabel", None))
        self.lblPrecio.setText(QCoreApplication.translate("widgetTarjetaServicio", u"TextLabel", None))
        self.btnEditarServicio.setText(QCoreApplication.translate("widgetTarjetaServicio", u"Editar", None))
        self.btnEliminarServicio.setText(QCoreApplication.translate("widgetTarjetaServicio", u"Eliminar", None))
    # retranslateUi

