# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz_nuevoproducto.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDateEdit, QDialog,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
from view import recursos_rc

class VentanaNuevoProducto(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(540, 370)
        Dialog.setMinimumSize(QSize(540, 370))
        Dialog.setMaximumSize(QSize(540, 370))
        icon = QIcon()
        icon.addFile(u":/images/images/icono.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.cuerpoNuevoProducto = QWidget(Dialog)
        self.cuerpoNuevoProducto.setObjectName(u"cuerpoNuevoProducto")
        self.cuerpoNuevoProducto.setStyleSheet(u"\n"
"\n"
"background-color: #F7E7DC;\n"
"border: 2px solid #DCBCA6;\n"
"border-radius: 10px\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.cuerpoNuevoProducto)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.widgetTitulo = QWidget(self.cuerpoNuevoProducto)
        self.widgetTitulo.setObjectName(u"widgetTitulo")
        self.widgetTitulo.setMaximumSize(QSize(16777215, 50))
        self.widgetTitulo.setStyleSheet(u"border: 0px;")
        self.gridLayout_2 = QGridLayout(self.widgetTitulo)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tituloNuevoProducto = QLabel(self.widgetTitulo)
        self.tituloNuevoProducto.setObjectName(u"tituloNuevoProducto")
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(18)
        font.setBold(True)
        self.tituloNuevoProducto.setFont(font)
        self.tituloNuevoProducto.setStyleSheet(u"color: #7D3928; border: 0;")
        self.tituloNuevoProducto.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.tituloNuevoProducto, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widgetTitulo)

        self.cuerpoFormProd = QWidget(self.cuerpoNuevoProducto)
        self.cuerpoFormProd.setObjectName(u"cuerpoFormProd")
        self.cuerpoFormProd.setStyleSheet(u"border: 0px;")
        self.horizontalLayout = QHBoxLayout(self.cuerpoFormProd)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.contenedorLbl = QWidget(self.cuerpoFormProd)
        self.contenedorLbl.setObjectName(u"contenedorLbl")
        self.contenedorLbl.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.contenedorLbl)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lblCodigo = QLabel(self.contenedorLbl)
        self.lblCodigo.setObjectName(u"lblCodigo")
        font1 = QFont()
        font1.setFamilies([u"Century Gothic"])
        font1.setPointSize(14)
        self.lblCodigo.setFont(font1)
        self.lblCodigo.setStyleSheet(u"color: #7D3928;")

        self.verticalLayout_2.addWidget(self.lblCodigo)

        self.lblDescripcion = QLabel(self.contenedorLbl)
        self.lblDescripcion.setObjectName(u"lblDescripcion")
        self.lblDescripcion.setFont(font1)
        self.lblDescripcion.setStyleSheet(u"color: #7D3928;")

        self.verticalLayout_2.addWidget(self.lblDescripcion)

        self.lblPrecio = QLabel(self.contenedorLbl)
        self.lblPrecio.setObjectName(u"lblPrecio")
        self.lblPrecio.setFont(font1)
        self.lblPrecio.setStyleSheet(u"color: #7D3928;")

        self.verticalLayout_2.addWidget(self.lblPrecio)

        self.lblStock = QLabel(self.contenedorLbl)
        self.lblStock.setObjectName(u"lblStock")
        self.lblStock.setFont(font1)
        self.lblStock.setStyleSheet(u"color: #7D3928;")

        self.verticalLayout_2.addWidget(self.lblStock)

        self.lblVencimiento = QLabel(self.contenedorLbl)
        self.lblVencimiento.setObjectName(u"lblVencimiento")
        self.lblVencimiento.setFont(font1)
        self.lblVencimiento.setStyleSheet(u"color: #7D3928;")

        self.verticalLayout_2.addWidget(self.lblVencimiento)


        self.horizontalLayout.addWidget(self.contenedorLbl)

        self.contenedorTxt = QWidget(self.cuerpoFormProd)
        self.contenedorTxt.setObjectName(u"contenedorTxt")
        self.verticalLayout_3 = QVBoxLayout(self.contenedorTxt)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.txtCodigo = QLineEdit(self.contenedorTxt)
        self.txtCodigo.setObjectName(u"txtCodigo")
        self.txtCodigo.setFont(font1)
        self.txtCodigo.setStyleSheet(u"color: rgb(125, 57, 40);\n"
"border: 2px solid #C18484;\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"")

        self.verticalLayout_3.addWidget(self.txtCodigo)

        self.txtDescripcion = QLineEdit(self.contenedorTxt)
        self.txtDescripcion.setObjectName(u"txtDescripcion")
        self.txtDescripcion.setFont(font1)
        self.txtDescripcion.setStyleSheet(u"color: rgb(125, 57, 40);\n"
"border: 2px solid #C18484;\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"")

        self.verticalLayout_3.addWidget(self.txtDescripcion)

        self.txtPrecio = QLineEdit(self.contenedorTxt)
        self.txtPrecio.setObjectName(u"txtPrecio")
        self.txtPrecio.setFont(font1)
        self.txtPrecio.setStyleSheet(u"color: rgb(125, 57, 40);\n"
"border: 2px solid #C18484;\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"")

        self.verticalLayout_3.addWidget(self.txtPrecio)

        self.txtStock = QLineEdit(self.contenedorTxt)
        self.txtStock.setObjectName(u"txtStock")
        self.txtStock.setFont(font1)
        self.txtStock.setStyleSheet(u"color: rgb(125, 57, 40);\n"
"border: 2px solid #C18484;\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"")

        self.verticalLayout_3.addWidget(self.txtStock)

        self.dateEditVencimiento = QDateEdit(self.contenedorTxt)
        self.dateEditVencimiento.setObjectName(u"dateEditVencimiento")
        self.dateEditVencimiento.setFont(font1)
        self.dateEditVencimiento.setStyleSheet(u"color: #7D3928;")
        self.dateEditVencimiento.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.dateEditVencimiento.setMinimumDate(QDate(2025, 1, 1))

        self.verticalLayout_3.addWidget(self.dateEditVencimiento)


        self.horizontalLayout.addWidget(self.contenedorTxt)


        self.verticalLayout.addWidget(self.cuerpoFormProd)

        self.widgetBoton = QWidget(self.cuerpoNuevoProducto)
        self.widgetBoton.setObjectName(u"widgetBoton")
        self.widgetBoton.setMaximumSize(QSize(16777215, 60))
        self.widgetBoton.setStyleSheet(u"border:0px;")
        self.gridLayout_3 = QGridLayout(self.widgetBoton)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(6)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnGuardarProducto = QPushButton(self.widgetBoton)
        self.btnGuardarProducto.setObjectName(u"btnGuardarProducto")
        self.btnGuardarProducto.setMinimumSize(QSize(0, 35))
        self.btnGuardarProducto.setMaximumSize(QSize(100, 16777215))
        self.btnGuardarProducto.setFont(font1)
        self.btnGuardarProducto.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnGuardarProducto.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_3.addWidget(self.btnGuardarProducto, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widgetBoton)


        self.gridLayout.addWidget(self.cuerpoNuevoProducto, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"BLA - Nuevo Producto", None))
        self.tituloNuevoProducto.setText(QCoreApplication.translate("Dialog", u"Nuevo Producto", None))
        self.lblCodigo.setText(QCoreApplication.translate("Dialog", u"C\u00f3digo", None))
        self.lblDescripcion.setText(QCoreApplication.translate("Dialog", u"Descripci\u00f3n", None))
        self.lblPrecio.setText(QCoreApplication.translate("Dialog", u"Precio", None))
        self.lblStock.setText(QCoreApplication.translate("Dialog", u"Stock", None))
        self.lblVencimiento.setText(QCoreApplication.translate("Dialog", u"Vencimiento", None))
        self.btnGuardarProducto.setText(QCoreApplication.translate("Dialog", u"Guardar", None))
    # retranslateUi

