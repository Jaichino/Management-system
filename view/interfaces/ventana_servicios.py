# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz_servicios.ui'
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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class VentanaServicio(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(380, 400)
        MainWindow.setMinimumSize(QSize(380, 400))
        MainWindow.setMaximumSize(QSize(380, 400))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color:white;")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color:  #C18484;\n"
"border-radius: 10px;")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 50))
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(120, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.widget_5)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelNombre = QLabel(self.widget_5)
        self.labelNombre.setObjectName(u"labelNombre")
        font1 = QFont()
        font1.setFamilies([u"Century Gothic"])
        font1.setPointSize(14)
        self.labelNombre.setFont(font1)

        self.verticalLayout_2.addWidget(self.labelNombre)

        self.labelDuracion = QLabel(self.widget_5)
        self.labelDuracion.setObjectName(u"labelDuracion")
        self.labelDuracion.setFont(font1)

        self.verticalLayout_2.addWidget(self.labelDuracion)

        self.labelPrecio = QLabel(self.widget_5)
        self.labelPrecio.setObjectName(u"labelPrecio")
        self.labelPrecio.setFont(font1)

        self.verticalLayout_2.addWidget(self.labelPrecio)


        self.horizontalLayout.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_3 = QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setSpacing(30)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.txtNombre = QLineEdit(self.widget_6)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setFont(font1)
        self.txtNombre.setStyleSheet(u"color:black;\n"
"background-color: white;\n"
"border-radius:5px;")

        self.verticalLayout_3.addWidget(self.txtNombre)

        self.txtDuracion = QLineEdit(self.widget_6)
        self.txtDuracion.setObjectName(u"txtDuracion")
        self.txtDuracion.setFont(font1)
        self.txtDuracion.setStyleSheet(u"color:black;\n"
"background-color: white;\n"
"border-radius:5px;")

        self.verticalLayout_3.addWidget(self.txtDuracion)

        self.txtPrecio = QLineEdit(self.widget_6)
        self.txtPrecio.setObjectName(u"txtPrecio")
        self.txtPrecio.setFont(font1)
        self.txtPrecio.setStyleSheet(u"color:black;\n"
"background-color: white;\n"
"border-radius:5px;")

        self.verticalLayout_3.addWidget(self.txtPrecio)


        self.horizontalLayout.addWidget(self.widget_6)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(16777215, 60))
        self.gridLayout_3 = QGridLayout(self.widget_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btnGuardarServicio = QPushButton(self.widget_4)
        self.btnGuardarServicio.setObjectName(u"btnGuardarServicio")
        self.btnGuardarServicio.setMaximumSize(QSize(120, 50))
        self.btnGuardarServicio.setFont(font1)
        self.btnGuardarServicio.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnGuardarServicio.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid white;\n"
"	border-radius: 10px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	font-weight: bold;\n"
"}")

        self.gridLayout_3.addWidget(self.btnGuardarServicio, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_4)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Servicios", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Servicios", None))
        self.labelNombre.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.labelDuracion.setText(QCoreApplication.translate("MainWindow", u"Duraci\u00f3n", None))
        self.labelPrecio.setText(QCoreApplication.translate("MainWindow", u"Precio", None))
        self.btnGuardarServicio.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
    # retranslateUi

