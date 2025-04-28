# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz_nuevocliente.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class VentanaCliente(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.ApplicationModal)
        MainWindow.resize(400, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(400, 300))
        MainWindow.setMaximumSize(QSize(400, 300))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: white")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.contenedorForm = QWidget(self.centralwidget)
        self.contenedorForm.setObjectName(u"contenedorForm")
        self.contenedorForm.setStyleSheet(u"background-color: #C18484;\n"
"border-radius:10px;")
        self.verticalLayout_2 = QVBoxLayout(self.contenedorForm)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.contenedorForm)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tituloVentana = QLabel(self.frame)
        self.tituloVentana.setObjectName(u"tituloVentana")
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(18)
        font.setBold(True)
        self.tituloVentana.setFont(font)
        self.tituloVentana.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tituloVentana.setWordWrap(True)

        self.gridLayout.addWidget(self.tituloVentana, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame)

        self.cuerpoForm = QWidget(self.contenedorForm)
        self.cuerpoForm.setObjectName(u"cuerpoForm")
        self.horizontalLayout = QHBoxLayout(self.cuerpoForm)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_2 = QWidget(self.cuerpoForm)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy2)
        self.widget_2.setMinimumSize(QSize(100, 0))
        self.widget_2.setMaximumSize(QSize(100, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setSpacing(21)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.labelNombre = QLabel(self.widget_2)
        self.labelNombre.setObjectName(u"labelNombre")
        font1 = QFont()
        font1.setFamilies([u"Century Gothic"])
        font1.setPointSize(14)
        self.labelNombre.setFont(font1)
        self.labelNombre.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.labelNombre)

        self.labelCelular = QLabel(self.widget_2)
        self.labelCelular.setObjectName(u"labelCelular")
        self.labelCelular.setFont(font1)
        self.labelCelular.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.labelCelular)

        self.labelEmail = QLabel(self.widget_2)
        self.labelEmail.setObjectName(u"labelEmail")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.labelEmail.sizePolicy().hasHeightForWidth())
        self.labelEmail.setSizePolicy(sizePolicy3)
        self.labelEmail.setFont(font1)
        self.labelEmail.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelEmail.setMargin(0)

        self.verticalLayout_3.addWidget(self.labelEmail)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.cuerpoForm)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setSpacing(30)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 4, 0, 4)
        self.txtNombre = QLineEdit(self.widget_3)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setFont(font1)
        self.txtNombre.setStyleSheet(u"color:black;\n"
"background-color: white;\n"
"border-radius: 5px;")

        self.verticalLayout_4.addWidget(self.txtNombre)

        self.txtCelular = QLineEdit(self.widget_3)
        self.txtCelular.setObjectName(u"txtCelular")
        self.txtCelular.setFont(font1)
        self.txtCelular.setStyleSheet(u"color:black;\n"
"background-color: white;\n"
"border-radius: 5px;")

        self.verticalLayout_4.addWidget(self.txtCelular)

        self.txtEmail = QLineEdit(self.widget_3)
        self.txtEmail.setObjectName(u"txtEmail")
        self.txtEmail.setFont(font1)
        self.txtEmail.setStyleSheet(u"color:black;\n"
"background-color: white;\n"
"border-radius: 5px;")

        self.verticalLayout_4.addWidget(self.txtEmail)


        self.horizontalLayout.addWidget(self.widget_3)


        self.verticalLayout_2.addWidget(self.cuerpoForm)

        self.contenedorBoton = QWidget(self.contenedorForm)
        self.contenedorBoton.setObjectName(u"contenedorBoton")
        self.contenedorBoton.setMaximumSize(QSize(16777215, 60))
        self.gridLayout_2 = QGridLayout(self.contenedorBoton)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btnAgregarCliente = QPushButton(self.contenedorBoton)
        self.btnAgregarCliente.setObjectName(u"btnAgregarCliente")
        self.btnAgregarCliente.setMinimumSize(QSize(0, 35))
        self.btnAgregarCliente.setMaximumSize(QSize(100, 35))
        self.btnAgregarCliente.setFont(font1)
        self.btnAgregarCliente.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAgregarCliente.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid white;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border: 2px solid white;\n"
"	font-weight: bold;\n"
"	border-radius: 5px;\n"
"}")

        self.gridLayout_2.addWidget(self.btnAgregarCliente, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.contenedorBoton)


        self.verticalLayout.addWidget(self.contenedorForm)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"BLA - Nuevo cliente", None))
        self.tituloVentana.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.labelNombre.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.labelCelular.setText(QCoreApplication.translate("MainWindow", u"Celular", None))
        self.labelEmail.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.btnAgregarCliente.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
    # retranslateUi

