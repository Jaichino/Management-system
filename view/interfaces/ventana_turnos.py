# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz_turnos.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTimeEdit,
    QVBoxLayout, QWidget)
from view import recursos_rc

class VentanaTurno(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.ApplicationModal)
        MainWindow.resize(400, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(400, 500))
        MainWindow.setMaximumSize(QSize(400, 500))
        icon = QIcon()
        icon.addFile(u":/images/images/icono.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 500))
        self.centralwidget.setMaximumSize(QSize(16777215, 500))
        self.centralwidget.setStyleSheet(u"background-color:white;")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"\n"
"background-color: #F7E7DC;\n"
"border: 2px solid #DCBCA6;\n"
"border-radius: 10px\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.contenedorTitulo = QWidget(self.widget)
        self.contenedorTitulo.setObjectName(u"contenedorTitulo")
        self.contenedorTitulo.setMaximumSize(QSize(16777215, 50))
        self.contenedorTitulo.setStyleSheet(u"border:0px")
        self.gridLayout_2 = QGridLayout(self.contenedorTitulo)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.contenedorTitulo)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #7D3928; ")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.contenedorTitulo)

        self.contenedorForm = QWidget(self.widget)
        self.contenedorForm.setObjectName(u"contenedorForm")
        self.contenedorForm.setStyleSheet(u"border: 0px")
        self.verticalLayout_2 = QVBoxLayout(self.contenedorForm)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.widget_2 = QWidget(self.contenedorForm)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.widget_7 = QWidget(self.widget_2)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMaximumSize(QSize(150, 16777215))
        self.widget_7.setStyleSheet(u"color: #7D3928; ")
        self.gridLayout_3 = QGridLayout(self.widget_7)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.widget_7)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Century Gothic"])
        font1.setPointSize(14)
        self.label_2.setFont(font1)

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget_2)
        self.widget_8.setObjectName(u"widget_8")
        font2 = QFont()
        font2.setFamilies([u"Century Gothic"])
        font2.setPointSize(12)
        self.widget_8.setFont(font2)
        self.gridLayout_8 = QGridLayout(self.widget_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, -1, 0, -1)
        self.cmbCliente = QComboBox(self.widget_8)
        self.cmbCliente.setObjectName(u"cmbCliente")
        font3 = QFont()
        font3.setFamilies([u"Century Gothic"])
        self.cmbCliente.setFont(font3)
        self.cmbCliente.setStyleSheet(u"QComboBox {\n"
"    font-family: \"Century Gothic\";\n"
"    font-size: 14px;\n"
"    color: #7D3928;\n"
"    padding: 5px;\n"
"	border: 1px solid #7D3928;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    font-family: \"Century Gothic\";\n"
"    font-size: 14px;\n"
"	color: #7D3928;\n"
"    selection-background-color: #e0e0e0;\n"
"    padding: 5px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none; /* Elimina el borde del cuadro desplegable */\n"
"    background: transparent; /* Elimina el fondo del bot\u00f3n */\n"
"    width: 20px; /* Opcional: control\u00e1s el espacio ocupado por la flechita */\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	\n"
"	image: url(:/images/images/flecha.svg.svg);\n"
"	width: 30px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.cmbCliente.setEditable(True)
        self.cmbCliente.setMaxVisibleItems(5)
        self.cmbCliente.setMinimumContentsLength(0)
        self.cmbCliente.setModelColumn(0)

        self.gridLayout_8.addWidget(self.cmbCliente, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget_8)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget_5 = QWidget(self.contenedorForm)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.widget_9 = QWidget(self.widget_5)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMaximumSize(QSize(150, 16777215))
        self.gridLayout_4 = QGridLayout(self.widget_9)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_3 = QLabel(self.widget_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: #7D3928; ")

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.widget_5)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setFont(font2)
        self.gridLayout_9 = QGridLayout(self.widget_10)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, -1, 0, -1)
        self.dateEditTurno = QDateEdit(self.widget_10)
        self.dateEditTurno.setObjectName(u"dateEditTurno")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dateEditTurno.sizePolicy().hasHeightForWidth())
        self.dateEditTurno.setSizePolicy(sizePolicy1)
        self.dateEditTurno.setFont(font2)
        self.dateEditTurno.setStyleSheet(u"color: #7D3928;")
        self.dateEditTurno.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.dateEditTurno.setDateTime(QDateTime(QDate(2025, 1, 1), QTime(0, 0, 0)))
        self.dateEditTurno.setMinimumDateTime(QDateTime(QDate(2025, 1, 1), QTime(0, 0, 0)))
        self.dateEditTurno.setCalendarPopup(False)

        self.gridLayout_9.addWidget(self.dateEditTurno, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.widget_10)


        self.verticalLayout_2.addWidget(self.widget_5)

        self.widget_3 = QWidget(self.contenedorForm)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.widget_11 = QWidget(self.widget_3)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMaximumSize(QSize(150, 16777215))
        self.gridLayout_5 = QGridLayout(self.widget_11)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_4 = QLabel(self.widget_11)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: #7D3928; ")

        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.widget_3)
        self.widget_12.setObjectName(u"widget_12")
        self.gridLayout_10 = QGridLayout(self.widget_12)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, -1, -1, -1)
        self.timeEditTurno = QTimeEdit(self.widget_12)
        self.timeEditTurno.setObjectName(u"timeEditTurno")
        self.timeEditTurno.setFont(font2)
        self.timeEditTurno.setStyleSheet(u"color: #7D3928;")
        self.timeEditTurno.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.timeEditTurno.setKeyboardTracking(True)
        self.timeEditTurno.setProperty(u"showGroupSeparator", False)
        self.timeEditTurno.setCalendarPopup(True)
        self.timeEditTurno.setCurrentSectionIndex(0)

        self.gridLayout_10.addWidget(self.timeEditTurno, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.widget_12)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.contenedorForm)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.widget_13 = QWidget(self.widget_4)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMaximumSize(QSize(150, 16777215))
        self.gridLayout_6 = QGridLayout(self.widget_13)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_5 = QLabel(self.widget_13)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: #7D3928; ")

        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.widget_13)

        self.widget_14 = QWidget(self.widget_4)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setFont(font1)
        self.gridLayout_11 = QGridLayout(self.widget_14)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, -1, 0, -1)
        self.cmbServicio = QComboBox(self.widget_14)
        self.cmbServicio.setObjectName(u"cmbServicio")
        self.cmbServicio.setFont(font3)
        self.cmbServicio.setStyleSheet(u"QComboBox {\n"
"    font-family: \"Century Gothic\";\n"
"    font-size: 14px;\n"
"    color: #7D3928;\n"
"    padding: 5px;\n"
"	border: 1px solid #7D3928;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    font-family: \"Century Gothic\";\n"
"    font-size: 14px;\n"
"	color: #7D3928;\n"
"    selection-background-color: #e0e0e0;\n"
"    padding: 5px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none; /* Elimina el borde del cuadro desplegable */\n"
"    background: transparent; /* Elimina el fondo del bot\u00f3n */\n"
"    width: 20px; /* Opcional: control\u00e1s el espacio ocupado por la flechita */\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	\n"
"	image: url(:/images/images/flecha.svg.svg);\n"
"	width: 30px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.cmbServicio.setEditable(False)
        self.cmbServicio.setMaxVisibleItems(5)

        self.gridLayout_11.addWidget(self.cmbServicio, 0, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.widget_14)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget_6 = QWidget(self.contenedorForm)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(0, 80))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.widget_15 = QWidget(self.widget_6)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(150, 0))
        self.widget_15.setMaximumSize(QSize(150, 16777215))
        self.gridLayout_7 = QGridLayout(self.widget_15)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_6 = QLabel(self.widget_15)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: #7D3928; ")

        self.gridLayout_7.addWidget(self.label_6, 0, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.widget_15)

        self.widget_16 = QWidget(self.widget_6)
        self.widget_16.setObjectName(u"widget_16")
        self.gridLayout_12 = QGridLayout(self.widget_16)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.txtSenia = QLineEdit(self.widget_16)
        self.txtSenia.setObjectName(u"txtSenia")
        self.txtSenia.setFont(font1)
        self.txtSenia.setStyleSheet(u"color: rgb(125, 57, 40);\n"
"border: 2px solid #C18484;\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"")

        self.gridLayout_12.addWidget(self.txtSenia, 0, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.widget_16)


        self.verticalLayout_2.addWidget(self.widget_6)


        self.verticalLayout.addWidget(self.contenedorForm)

        self.contenedorBoton = QWidget(self.widget)
        self.contenedorBoton.setObjectName(u"contenedorBoton")
        self.contenedorBoton.setMinimumSize(QSize(0, 60))
        self.contenedorBoton.setMaximumSize(QSize(16777215, 100))
        self.contenedorBoton.setStyleSheet(u"border: 0px")
        self.gridLayout_13 = QGridLayout(self.contenedorBoton)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.btnAgendarTurno = QPushButton(self.contenedorBoton)
        self.btnAgendarTurno.setObjectName(u"btnAgendarTurno")
        self.btnAgendarTurno.setMaximumSize(QSize(120, 35))
        self.btnAgendarTurno.setFont(font1)
        self.btnAgendarTurno.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAgendarTurno.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_13.addWidget(self.btnAgendarTurno, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.contenedorBoton)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Nuevo Turno", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nuevo Turno", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Fecha", None))
        self.dateEditTurno.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/MM/yyyy", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Hora", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Servicio", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Se\u00f1a", None))
        self.btnAgendarTurno.setText(QCoreApplication.translate("MainWindow", u"Agendar", None))
    # retranslateUi

