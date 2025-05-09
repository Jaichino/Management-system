# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_detalleventa.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)
from view import recursos_rc

class VentanaDetalleVenta(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(750, 375)
        Dialog.setMinimumSize(QSize(750, 375))
        Dialog.setMaximumSize(QSize(750, 375))
        icon = QIcon()
        icon.addFile(u":/images/images/icono.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"background-color: white")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"\n"
"\n"
"background-color: #F7E7DC;\n"
"border: 2px solid #DCBCA6;\n"
"border-radius: 10px\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 50))
        self.widget_2.setStyleSheet(u"border: 0")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #7D3928; ")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 300))
        self.widget_3.setStyleSheet(u"border: 0")
        self.gridLayout_3 = QGridLayout(self.widget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tablaDetalleVenta = QTableView(self.widget_3)
        self.tablaDetalleVenta.setObjectName(u"tablaDetalleVenta")
        self.tablaDetalleVenta.setStyleSheet(u"\n"
"QTableView {\n"
"	border: 2px solid #DEC4AE;\n"
"	border-radius: 10px;\n"
"	color: rgb(125, 57, 40);\n"
"	font: 12pt \"Century Gothic\";\n"
"	gridline-color: rgb(125, 57, 40);\n"
"	selection-background-color: #D3B9B4;\n"
"	selection-color: rgb(0, 0, 0);\n"
"	background-color: #FDF5EE;\n"
"}\n"
"\n"
"\n"
"/*QHeaderView {\n"
"	color: rgb(125, 57, 40);\n"
"	background-color: #F7E7DC;\n"
"	font-weight: bold;\n"
"	font-family: century-gothic;\n"
"	font-size: 12pt;\n"
"	gridline-color: rgb(125, 57, 40);\n"
"	border-radius: 10px;\n"
"	border-right: 1px solid rgb(125, 57, 40);\n"
"}*/\n"
"\n"
"QHeaderView::section {\n"
"    color: rgb(125, 57, 40);\n"
"    background-color: #F7E0D3;\n"
"    font-weight: bold;\n"
"    font-family: century-gothic;\n"
"    font-size: 12pt;\n"
"    padding: 5px;\n"
"    border: none;\n"
"    border-right: 1px solid rgb(125, 57, 40); /* Esto simula el gridline */\n"
"    border-bottom: 1px solid rgb(125, 57, 40); /* Opcional, l\u00ednea debajo del header */\n"
"}\n"
"\n"
"QLineEdit {\n"
""
                        "	color: rgb(125, 57, 40);\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.tablaDetalleVenta, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_3)

        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border: 0")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btnGenFactura = QPushButton(self.frame)
        self.btnGenFactura.setObjectName(u"btnGenFactura")
        self.btnGenFactura.setMinimumSize(QSize(0, 35))
        self.btnGenFactura.setMaximumSize(QSize(200, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Century Gothic"])
        font1.setPointSize(14)
        self.btnGenFactura.setFont(font1)
        self.btnGenFactura.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnGenFactura.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_4.addWidget(self.btnGenFactura, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"BLA - Detalle de Venta", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Detalle de venta", None))
        self.btnGenFactura.setText(QCoreApplication.translate("Dialog", u"Generar Factura", None))
    # retranslateUi

