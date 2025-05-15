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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QFrame,
    QGridLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableView, QVBoxLayout, QWidget)
from view import recursos_rc

class VentanaDetalleVenta(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 375)
        Dialog.setMinimumSize(QSize(800, 375))
        Dialog.setMaximumSize(QSize(800, 375))
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
        self.lblTitulo = QLabel(self.widget_2)
        self.lblTitulo.setObjectName(u"lblTitulo")
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(18)
        font.setBold(True)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setStyleSheet(u"color: #7D3928; ")
        self.lblTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lblTitulo, 0, 0, 1, 1)


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
        font1 = QFont()
        font1.setFamilies([u"Century Gothic"])
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        self.tablaDetalleVenta.setFont(font1)
        self.tablaDetalleVenta.setStyleSheet(u"\n"
"QTableView {\n"
"	border: 2px solid #DEC4AE;\n"
"	border-radius: 10px;\n"
"	color: rgb(125, 57, 40);\n"
"	font: 11pt \"Century Gothic\";\n"
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
"    font-size: 11pt;\n"
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
        self.tablaDetalleVenta.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tablaDetalleVenta.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tablaDetalleVenta.horizontalHeader().setStretchLastSection(True)
        self.tablaDetalleVenta.verticalHeader().setVisible(False)

        self.gridLayout_3.addWidget(self.tablaDetalleVenta, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 80))
        self.widget_4.setMaximumSize(QSize(16777215, 80))
        self.widget_4.setStyleSheet(u"border:0")
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 0, -1, 4)
        self.lblTotalProductos = QLabel(self.widget_4)
        self.lblTotalProductos.setObjectName(u"lblTotalProductos")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTotalProductos.sizePolicy().hasHeightForWidth())
        self.lblTotalProductos.setSizePolicy(sizePolicy)
        self.lblTotalProductos.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setFamilies([u"Century Gothic"])
        font2.setPointSize(12)
        self.lblTotalProductos.setFont(font2)
        self.lblTotalProductos.setStyleSheet(u"color:#7D3928;")
        self.lblTotalProductos.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.lblTotalProductos)

        self.lblTotalInteres = QLabel(self.widget_4)
        self.lblTotalInteres.setObjectName(u"lblTotalInteres")
        sizePolicy.setHeightForWidth(self.lblTotalInteres.sizePolicy().hasHeightForWidth())
        self.lblTotalInteres.setSizePolicy(sizePolicy)
        self.lblTotalInteres.setMinimumSize(QSize(0, 30))
        self.lblTotalInteres.setFont(font2)
        self.lblTotalInteres.setStyleSheet(u"color:#7D3928;")
        self.lblTotalInteres.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.lblTotalInteres)

        self.lblTotalAbonar = QLabel(self.widget_4)
        self.lblTotalAbonar.setObjectName(u"lblTotalAbonar")
        sizePolicy.setHeightForWidth(self.lblTotalAbonar.sizePolicy().hasHeightForWidth())
        self.lblTotalAbonar.setSizePolicy(sizePolicy)
        self.lblTotalAbonar.setMinimumSize(QSize(0, 30))
        self.lblTotalAbonar.setFont(font2)
        self.lblTotalAbonar.setStyleSheet(u"color:#7D3928;")
        self.lblTotalAbonar.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.lblTotalAbonar)


        self.verticalLayout.addWidget(self.widget_4)

        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 40))
        self.frame.setStyleSheet(u"border: 0")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btnGenFactura = QPushButton(self.frame)
        self.btnGenFactura.setObjectName(u"btnGenFactura")
        self.btnGenFactura.setMinimumSize(QSize(0, 35))
        self.btnGenFactura.setMaximumSize(QSize(200, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Century Gothic"])
        font3.setPointSize(14)
        self.btnGenFactura.setFont(font3)
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
        self.lblTitulo.setText(QCoreApplication.translate("Dialog", u"Detalle de venta", None))
        self.lblTotalProductos.setText(QCoreApplication.translate("Dialog", u"Total productos: $", None))
        self.lblTotalInteres.setText(QCoreApplication.translate("Dialog", u"Interes: $", None))
        self.lblTotalAbonar.setText(QCoreApplication.translate("Dialog", u"Total a abonar: $", None))
        self.btnGenFactura.setText(QCoreApplication.translate("Dialog", u"Generar Factura", None))
    # retranslateUi

