# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app_interface.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QCalendarWidget,
    QCheckBox, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSpinBox,
    QStackedWidget, QTableView, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
from view import recursos_rc

class VentanaPrincipal(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.WindowModal)
        MainWindow.resize(1100, 650)
        MainWindow.setMinimumSize(QSize(1100, 650))
        MainWindow.setMaximumSize(QSize(1100, 650))
        icon = QIcon()
        icon.addFile(u":/images/images/icono.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(1100, 650))
        self.centralwidget.setMaximumSize(QSize(1100, 650))
        self.centralwidget.setStyleSheet(u"background-color: #F7EDE5;")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.LeftMenu = QWidget(self.centralwidget)
        self.LeftMenu.setObjectName(u"LeftMenu")
        self.LeftMenu.setMinimumSize(QSize(200, 0))
        self.LeftMenu.setMaximumSize(QSize(200, 16777215))
        self.LeftMenu.setStyleSheet(u"background-color: #F7E7DC;\n"
"border: 2px solid #DCBCA6;\n"
"border-radius: 10px\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.LeftMenu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, -1)
        self.LogoNegocio = QWidget(self.LeftMenu)
        self.LogoNegocio.setObjectName(u"LogoNegocio")
        sizePolicy.setHeightForWidth(self.LogoNegocio.sizePolicy().hasHeightForWidth())
        self.LogoNegocio.setSizePolicy(sizePolicy)
        self.LogoNegocio.setMaximumSize(QSize(16777215, 200))
        self.LogoNegocio.setStyleSheet(u"image: url(:/images/images/logo_sinfondo.png);\n"
"border: 0px;\n"
"")
        self.verticalLayout_14 = QVBoxLayout(self.LogoNegocio)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.LogoNegocio)

        self.MenuBotones = QWidget(self.LeftMenu)
        self.MenuBotones.setObjectName(u"MenuBotones")
        self.MenuBotones.setMinimumSize(QSize(0, 400))
        self.MenuBotones.setMaximumSize(QSize(16777215, 450))
        self.MenuBotones.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MenuBotones.setStyleSheet(u"border: 2px solid #C18484;\n"
"border-radius: 30px;\n"
"background-color: #F7E7DB;")
        self.verticalLayout_2 = QVBoxLayout(self.MenuBotones)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, -1, 15, -1)
        self.btnMenu = QPushButton(self.MenuBotones)
        self.btnMenu.setObjectName(u"btnMenu")
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(20)
        font.setBold(True)
        self.btnMenu.setFont(font)
        self.btnMenu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnMenu.setStyleSheet(u"color: #7D3928; border: 0px")

        self.verticalLayout_2.addWidget(self.btnMenu)

        self.btnMenuProductos = QPushButton(self.MenuBotones)
        self.btnMenuProductos.setObjectName(u"btnMenuProductos")
        self.btnMenuProductos.setMinimumSize(QSize(0, 30))
        self.btnMenuProductos.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setFamilies([u"Century Gothic"])
        font1.setPointSize(12)
        self.btnMenuProductos.setFont(font1)
        self.btnMenuProductos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnMenuProductos.setStyleSheet(u"QPushButton {\n"
"	color: #7D3928;\n"
"	border: 0px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	font-weight: bold;\n"
"	border-bottom: 2px solid;\n"
"	border-radius: 5px;\n"
"	border-color: #7D3928;\n"
"}")

        self.verticalLayout_2.addWidget(self.btnMenuProductos)

        self.btnMenuVentas = QPushButton(self.MenuBotones)
        self.btnMenuVentas.setObjectName(u"btnMenuVentas")
        self.btnMenuVentas.setMinimumSize(QSize(0, 30))
        self.btnMenuVentas.setMaximumSize(QSize(16777215, 50))
        self.btnMenuVentas.setFont(font1)
        self.btnMenuVentas.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnMenuVentas.setStyleSheet(u"QPushButton {\n"
"	color: #7D3928;\n"
"	border: 0px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	font-weight: bold;\n"
"	border-bottom: 2px solid;\n"
"	border-radius: 5px;\n"
"	border-color: #7D3928;\n"
"}")

        self.verticalLayout_2.addWidget(self.btnMenuVentas)

        self.btnMenuServicios = QPushButton(self.MenuBotones)
        self.btnMenuServicios.setObjectName(u"btnMenuServicios")
        self.btnMenuServicios.setMinimumSize(QSize(0, 30))
        self.btnMenuServicios.setMaximumSize(QSize(16777215, 50))
        self.btnMenuServicios.setFont(font1)
        self.btnMenuServicios.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnMenuServicios.setStyleSheet(u"QPushButton {\n"
"	color: #7D3928;\n"
"	border: 0px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	font-weight: bold;\n"
"	border-bottom: 2px solid;\n"
"	border-radius: 5px;\n"
"	border-color: #7D3928;\n"
"}")

        self.verticalLayout_2.addWidget(self.btnMenuServicios)

        self.btnMenuTurnos = QPushButton(self.MenuBotones)
        self.btnMenuTurnos.setObjectName(u"btnMenuTurnos")
        self.btnMenuTurnos.setMinimumSize(QSize(0, 30))
        self.btnMenuTurnos.setMaximumSize(QSize(16777215, 50))
        self.btnMenuTurnos.setFont(font1)
        self.btnMenuTurnos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnMenuTurnos.setStyleSheet(u"QPushButton {\n"
"	color: #7D3928;\n"
"	border: 0px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	font-weight: bold;\n"
"	border-bottom: 2px solid;\n"
"	border-radius: 5px;\n"
"	border-color: #7D3928;\n"
"}")

        self.verticalLayout_2.addWidget(self.btnMenuTurnos)

        self.btnMenuClientes = QPushButton(self.MenuBotones)
        self.btnMenuClientes.setObjectName(u"btnMenuClientes")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnMenuClientes.sizePolicy().hasHeightForWidth())
        self.btnMenuClientes.setSizePolicy(sizePolicy1)
        self.btnMenuClientes.setMinimumSize(QSize(0, 30))
        self.btnMenuClientes.setMaximumSize(QSize(16777215, 50))
        self.btnMenuClientes.setFont(font1)
        self.btnMenuClientes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnMenuClientes.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnMenuClientes.setStyleSheet(u"QPushButton {\n"
"	color: #7D3928;\n"
"	border: 0px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	font-weight: bold;\n"
"	border-bottom: 2px solid;\n"
"	border-radius: 5px;\n"
"	border-color: #7D3928;\n"
"}")
        self.btnMenuClientes.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.btnMenuClientes)

        self.btnMenuHistorial = QPushButton(self.MenuBotones)
        self.btnMenuHistorial.setObjectName(u"btnMenuHistorial")
        self.btnMenuHistorial.setMinimumSize(QSize(0, 30))
        self.btnMenuHistorial.setMaximumSize(QSize(16777215, 50))
        self.btnMenuHistorial.setFont(font1)
        self.btnMenuHistorial.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnMenuHistorial.setStyleSheet(u"QPushButton {\n"
"	color: #7D3928;\n"
"	border: 0px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	font-weight: bold;\n"
"	border-bottom: 2px solid;\n"
"	border-radius: 5px;\n"
"	border-color: #7D3928;\n"
"}")

        self.verticalLayout_2.addWidget(self.btnMenuHistorial)

        self.btnMenuCCorriente = QPushButton(self.MenuBotones)
        self.btnMenuCCorriente.setObjectName(u"btnMenuCCorriente")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnMenuCCorriente.sizePolicy().hasHeightForWidth())
        self.btnMenuCCorriente.setSizePolicy(sizePolicy2)
        self.btnMenuCCorriente.setMinimumSize(QSize(0, 30))
        self.btnMenuCCorriente.setMaximumSize(QSize(16777215, 50))
        self.btnMenuCCorriente.setFont(font1)
        self.btnMenuCCorriente.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnMenuCCorriente.setStyleSheet(u"QPushButton {\n"
"	color: #7D3928;\n"
"	border: 0px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	font-weight: bold;\n"
"	border-bottom: 2px solid;\n"
"	border-radius: 5px;\n"
"	border-color: #7D3928;\n"
"}")

        self.verticalLayout_2.addWidget(self.btnMenuCCorriente)


        self.verticalLayout.addWidget(self.MenuBotones)


        self.horizontalLayout.addWidget(self.LeftMenu)

        self.MainBody = QWidget(self.centralwidget)
        self.MainBody.setObjectName(u"MainBody")
        sizePolicy1.setHeightForWidth(self.MainBody.sizePolicy().hasHeightForWidth())
        self.MainBody.setSizePolicy(sizePolicy1)
        self.MainBody.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.MainBody)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout_4.setContentsMargins(4, 0, 0, 0)
        self.StackedWidget = QStackedWidget(self.MainBody)
        self.StackedWidget.setObjectName(u"StackedWidget")
        sizePolicy.setHeightForWidth(self.StackedWidget.sizePolicy().hasHeightForWidth())
        self.StackedWidget.setSizePolicy(sizePolicy)
        self.StackedWidget.setMinimumSize(QSize(0, 0))
        self.StackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.StackedWidget.setStyleSheet(u"")
        self.MenuServicios = QWidget()
        self.MenuServicios.setObjectName(u"MenuServicios")
        self.verticalLayout_6 = QVBoxLayout(self.MenuServicios)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(2, 0, 2, 0)
        self.encabezadoServicios = QWidget(self.MenuServicios)
        self.encabezadoServicios.setObjectName(u"encabezadoServicios")
        self.encabezadoServicios.setMinimumSize(QSize(0, 100))
        self.encabezadoServicios.setMaximumSize(QSize(16777215, 100))
        self.encabezadoServicios.setStyleSheet(u"background-color: #F7E7DC;\n"
"border: 2px solid #DCBCA6;\n"
"border-radius: 10px\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.encabezadoServicios)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 4, -1, 4)
        self.widgetTituloServicios = QWidget(self.encabezadoServicios)
        self.widgetTituloServicios.setObjectName(u"widgetTituloServicios")
        sizePolicy.setHeightForWidth(self.widgetTituloServicios.sizePolicy().hasHeightForWidth())
        self.widgetTituloServicios.setSizePolicy(sizePolicy)
        self.widgetTituloServicios.setMinimumSize(QSize(250, 0))
        self.widgetTituloServicios.setMaximumSize(QSize(200, 150))
        self.widgetTituloServicios.setStyleSheet(u"border: 0px;")
        self.verticalLayout_17 = QVBoxLayout(self.widgetTituloServicios)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 9, 9, 9)
        self.tituloServicios = QLabel(self.widgetTituloServicios)
        self.tituloServicios.setObjectName(u"tituloServicios")
        sizePolicy1.setHeightForWidth(self.tituloServicios.sizePolicy().hasHeightForWidth())
        self.tituloServicios.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"Century Gothic"])
        font2.setPointSize(24)
        font2.setBold(True)
        self.tituloServicios.setFont(font2)
        self.tituloServicios.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tituloServicios.setStyleSheet(u"color: #7D3928;\n"
"border: 0px\n"
"\n"
"")
        self.tituloServicios.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.tituloServicios.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.tituloServicios)


        self.horizontalLayout_3.addWidget(self.widgetTituloServicios)

        self.widgetBotones = QWidget(self.encabezadoServicios)
        self.widgetBotones.setObjectName(u"widgetBotones")
        sizePolicy.setHeightForWidth(self.widgetBotones.sizePolicy().hasHeightForWidth())
        self.widgetBotones.setSizePolicy(sizePolicy)
        self.widgetBotones.setMinimumSize(QSize(400, 80))
        self.widgetBotones.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.widgetBotones.setStyleSheet(u"border: 0px;")
        self.horizontalLayout_4 = QHBoxLayout(self.widgetBotones)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 4, -1, 4)
        self.espaciador = QWidget(self.widgetBotones)
        self.espaciador.setObjectName(u"espaciador")
        self.gridLayout_2 = QGridLayout(self.espaciador)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.horizontalLayout_4.addWidget(self.espaciador)

        self.botonera = QWidget(self.widgetBotones)
        self.botonera.setObjectName(u"botonera")
        self.botonera.setMinimumSize(QSize(400, 0))
        self.botonera.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.verticalLayout_15 = QVBoxLayout(self.botonera)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, 0, -1, 0)
        self.btnNuevoServicio = QPushButton(self.botonera)
        self.btnNuevoServicio.setObjectName(u"btnNuevoServicio")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btnNuevoServicio.sizePolicy().hasHeightForWidth())
        self.btnNuevoServicio.setSizePolicy(sizePolicy3)
        self.btnNuevoServicio.setMaximumSize(QSize(150, 50))
        font3 = QFont()
        font3.setFamilies([u"Century Gothic"])
        font3.setPointSize(14)
        self.btnNuevoServicio.setFont(font3)
        self.btnNuevoServicio.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnNuevoServicio.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.btnNuevoServicio.setAutoFillBackground(False)
        self.btnNuevoServicio.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_15.addWidget(self.btnNuevoServicio)


        self.horizontalLayout_4.addWidget(self.botonera)


        self.horizontalLayout_3.addWidget(self.widgetBotones)


        self.verticalLayout_6.addWidget(self.encabezadoServicios)

        self.scrollAreaServicio = QScrollArea(self.MenuServicios)
        self.scrollAreaServicio.setObjectName(u"scrollAreaServicio")
        self.scrollAreaServicio.setStyleSheet(u"border: 1px solid #DEC4AE;\n"
"border-radius: 10px;\n"
"background-color: #FDF5EE;")
        self.scrollAreaServicio.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollAreaServicio.setWidgetResizable(True)
        self.scrollAreaServicio.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.contenedorServicios = QWidget()
        self.contenedorServicios.setObjectName(u"contenedorServicios")
        self.contenedorServicios.setGeometry(QRect(0, 0, 879, 532))
        self.verticalLayout_3 = QVBoxLayout(self.contenedorServicios)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 0, 2, 0)
        self.scrollAreaServicio.setWidget(self.contenedorServicios)

        self.verticalLayout_6.addWidget(self.scrollAreaServicio)

        self.StackedWidget.addWidget(self.MenuServicios)
        self.MenuTurnos = QWidget()
        self.MenuTurnos.setObjectName(u"MenuTurnos")
        self.MenuTurnos.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.MenuTurnos)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(2, 0, 2, 0)
        self.encabezadoTurnos = QWidget(self.MenuTurnos)
        self.encabezadoTurnos.setObjectName(u"encabezadoTurnos")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.encabezadoTurnos.sizePolicy().hasHeightForWidth())
        self.encabezadoTurnos.setSizePolicy(sizePolicy4)
        self.encabezadoTurnos.setMaximumSize(QSize(16777215, 170))
        self.encabezadoTurnos.setStyleSheet(u"background-color: #F7E7DC;\n"
"border: 2px solid #DCBCA6;\n"
"border-radius: 10px\n"
"")
        self.horizontalLayout_5 = QHBoxLayout(self.encabezadoTurnos)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 9, -1, -1)
        self.contenedorTitulo = QWidget(self.encabezadoTurnos)
        self.contenedorTitulo.setObjectName(u"contenedorTitulo")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.contenedorTitulo.sizePolicy().hasHeightForWidth())
        self.contenedorTitulo.setSizePolicy(sizePolicy5)
        self.contenedorTitulo.setMaximumSize(QSize(200, 16777215))
        self.contenedorTitulo.setStyleSheet(u"border: 0px;")
        self.horizontalLayout_6 = QHBoxLayout(self.contenedorTitulo)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.tituloTurnos = QLabel(self.contenedorTitulo)
        self.tituloTurnos.setObjectName(u"tituloTurnos")
        self.tituloTurnos.setFont(font2)
        self.tituloTurnos.setStyleSheet(u"color: #7D3928;\n"
"border: 0px")
        self.tituloTurnos.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.tituloTurnos.setWordWrap(True)

        self.horizontalLayout_6.addWidget(self.tituloTurnos)


        self.horizontalLayout_5.addWidget(self.contenedorTitulo)

        self.contenedorCalendario = QWidget(self.encabezadoTurnos)
        self.contenedorCalendario.setObjectName(u"contenedorCalendario")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.contenedorCalendario.sizePolicy().hasHeightForWidth())
        self.contenedorCalendario.setSizePolicy(sizePolicy6)
        self.contenedorCalendario.setMaximumSize(QSize(400, 16777215))
        self.contenedorCalendario.setStyleSheet(u"border: 0px")
        self.horizontalLayout_8 = QHBoxLayout(self.contenedorCalendario)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 2, 0, 2)
        self.calendarWidget = QCalendarWidget(self.contenedorCalendario)
        self.calendarWidget.setObjectName(u"calendarWidget")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy7)
        self.calendarWidget.setMinimumSize(QSize(0, 149))
        font4 = QFont()
        font4.setFamilies([u"Century Gothic"])
        font4.setPointSize(8)
        font4.setBold(True)
        font4.setItalic(False)
        self.calendarWidget.setFont(font4)
        self.calendarWidget.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.calendarWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.calendarWidget.setStyleSheet(u"QCalendarWidget QAbstractItemView {\n"
"    color: rgb(125, 57, 40);\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView::item:selected {\n"
"    background-color: #D3B9B4;\n"
"    color: black;\n"
"	border-radius: 5px;\n"
"\n"
"}\n"
"QCalendarWidget QWidget {\n"
"	font:8pt \"Century Gothic\";\n"
"    color: rgb(125, 57, 40);\n"
"}")
        self.calendarWidget.setSelectedDate(QDate(2025, 4, 1))
        self.calendarWidget.setMinimumDate(QDate(2025, 4, 1))
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setHorizontalHeaderFormat(QCalendarWidget.HorizontalHeaderFormat.SingleLetterDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)

        self.horizontalLayout_8.addWidget(self.calendarWidget)


        self.horizontalLayout_5.addWidget(self.contenedorCalendario)

        self.botoneraTurnos = QWidget(self.encabezadoTurnos)
        self.botoneraTurnos.setObjectName(u"botoneraTurnos")
        sizePolicy5.setHeightForWidth(self.botoneraTurnos.sizePolicy().hasHeightForWidth())
        self.botoneraTurnos.setSizePolicy(sizePolicy5)
        self.botoneraTurnos.setMaximumSize(QSize(200, 19999))
        self.botoneraTurnos.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.botoneraTurnos.setStyleSheet(u"border: 0px;")
        self.verticalLayout_9 = QVBoxLayout(self.botoneraTurnos)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.btnNuevoTurno = QPushButton(self.botoneraTurnos)
        self.btnNuevoTurno.setObjectName(u"btnNuevoTurno")
        sizePolicy3.setHeightForWidth(self.btnNuevoTurno.sizePolicy().hasHeightForWidth())
        self.btnNuevoTurno.setSizePolicy(sizePolicy3)
        self.btnNuevoTurno.setMaximumSize(QSize(150, 50))
        self.btnNuevoTurno.setFont(font3)
        self.btnNuevoTurno.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnNuevoTurno.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.btnNuevoTurno.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_9.addWidget(self.btnNuevoTurno)


        self.horizontalLayout_5.addWidget(self.botoneraTurnos)


        self.verticalLayout_8.addWidget(self.encabezadoTurnos)

        self.scrollAreaTurnos = QScrollArea(self.MenuTurnos)
        self.scrollAreaTurnos.setObjectName(u"scrollAreaTurnos")
        self.scrollAreaTurnos.setStyleSheet(u"border: 1px solid #DEC4AE;\n"
"border-radius: 10px;\n"
"background-color: #FDF5EE;")
        self.scrollAreaTurnos.setWidgetResizable(True)
        self.contenedorTurnos = QWidget()
        self.contenedorTurnos.setObjectName(u"contenedorTurnos")
        self.contenedorTurnos.setGeometry(QRect(0, 0, 879, 462))
        self.verticalLayout_16 = QVBoxLayout(self.contenedorTurnos)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.scrollAreaTurnos.setWidget(self.contenedorTurnos)

        self.verticalLayout_8.addWidget(self.scrollAreaTurnos)

        self.StackedWidget.addWidget(self.MenuTurnos)
        self.MenuVentas = QWidget()
        self.MenuVentas.setObjectName(u"MenuVentas")
        self.gridLayout_9 = QGridLayout(self.MenuVentas)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.stackedVentas = QStackedWidget(self.MenuVentas)
        self.stackedVentas.setObjectName(u"stackedVentas")
        self.MenuConsultaVenta = QWidget()
        self.MenuConsultaVenta.setObjectName(u"MenuConsultaVenta")
        self.verticalLayout_33 = QVBoxLayout(self.MenuConsultaVenta)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.encabezadoConsultaVenta = QWidget(self.MenuConsultaVenta)
        self.encabezadoConsultaVenta.setObjectName(u"encabezadoConsultaVenta")
        self.encabezadoConsultaVenta.setMinimumSize(QSize(0, 80))
        self.encabezadoConsultaVenta.setMaximumSize(QSize(16777215, 120))
        self.encabezadoConsultaVenta.setStyleSheet(u"background-color: #F7E7DC;\n"
"border: 2px solid #DCBCA6;\n"
"border-radius: 10px\n"
"")
        self.horizontalLayout_19 = QHBoxLayout(self.encabezadoConsultaVenta)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(4, 4, 4, 4)
        self.widget_39 = QWidget(self.encabezadoConsultaVenta)
        self.widget_39.setObjectName(u"widget_39")
        self.widget_39.setMaximumSize(QSize(200, 16777215))
        self.widget_39.setStyleSheet(u"border: 0px")
        self.verticalLayout_34 = QVBoxLayout(self.widget_39)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(4, 4, 4, 4)
        self.widget_43 = QWidget(self.widget_39)
        self.widget_43.setObjectName(u"widget_43")
        self.widget_43.setMaximumSize(QSize(16777215, 40))
        self.gridLayout_35 = QGridLayout(self.widget_43)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.gridLayout_35.setContentsMargins(0, 4, 120, 4)
        self.btnVolverAVenta = QPushButton(self.widget_43)
        self.btnVolverAVenta.setObjectName(u"btnVolverAVenta")
        self.btnVolverAVenta.setMinimumSize(QSize(0, 25))
        self.btnVolverAVenta.setMaximumSize(QSize(80, 16777215))
        font5 = QFont()
        font5.setFamilies([u"Century Gothic"])
        font5.setPointSize(10)
        self.btnVolverAVenta.setFont(font5)
        self.btnVolverAVenta.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnVolverAVenta.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_35.addWidget(self.btnVolverAVenta, 0, 0, 1, 1)


        self.verticalLayout_34.addWidget(self.widget_43)

        self.widget_44 = QWidget(self.widget_39)
        self.widget_44.setObjectName(u"widget_44")
        self.gridLayout_24 = QGridLayout(self.widget_44)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setHorizontalSpacing(7)
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget_44)
        self.label_5.setObjectName(u"label_5")
        font6 = QFont()
        font6.setFamilies([u"Century Gothic"])
        font6.setPointSize(22)
        font6.setBold(True)
        self.label_5.setFont(font6)
        self.label_5.setStyleSheet(u"color: #7D3928;")
        self.label_5.setWordWrap(True)

        self.gridLayout_24.addWidget(self.label_5, 0, 0, 1, 1)


        self.verticalLayout_34.addWidget(self.widget_44)


        self.horizontalLayout_19.addWidget(self.widget_39)

        self.widget_40 = QWidget(self.encabezadoConsultaVenta)
        self.widget_40.setObjectName(u"widget_40")
        self.widget_40.setMaximumSize(QSize(150, 16777215))
        self.widget_40.setStyleSheet(u"border: 0px")
        self.verticalLayout_35 = QVBoxLayout(self.widget_40)
        self.verticalLayout_35.setSpacing(10)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_9 = QLabel(self.widget_40)
        self.label_9.setObjectName(u"label_9")
        font7 = QFont()
        font7.setFamilies([u"Century Gothic"])
        font7.setPointSize(12)
        font7.setBold(True)
        self.label_9.setFont(font7)
        self.label_9.setStyleSheet(u"color: #7D3928;")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_35.addWidget(self.label_9)

        self.label_11 = QLabel(self.widget_40)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font7)
        self.label_11.setStyleSheet(u"color: #7D3928;")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_35.addWidget(self.label_11)

        self.label_12 = QLabel(self.widget_40)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font7)
        self.label_12.setStyleSheet(u"color: #7D3928;")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_35.addWidget(self.label_12)


        self.horizontalLayout_19.addWidget(self.widget_40)

        self.widget_41 = QWidget(self.encabezadoConsultaVenta)
        self.widget_41.setObjectName(u"widget_41")
        self.widget_41.setMaximumSize(QSize(250, 16777215))
        self.widget_41.setStyleSheet(u"border: 0;")
        self.verticalLayout_36 = QVBoxLayout(self.widget_41)
        self.verticalLayout_36.setSpacing(10)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, -1, -1, -1)
        self.consultaVentaDesde = QDateEdit(self.widget_41)
        self.consultaVentaDesde.setObjectName(u"consultaVentaDesde")
        self.consultaVentaDesde.setStyleSheet(u"color: #7D3928;\n"
"font: 12pt \"Century Gothic\";")
        self.consultaVentaDesde.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.consultaVentaDesde.setMinimumDate(QDate(2025, 1, 1))

        self.verticalLayout_36.addWidget(self.consultaVentaDesde)

        self.ConsultaVentaHasta = QDateEdit(self.widget_41)
        self.ConsultaVentaHasta.setObjectName(u"ConsultaVentaHasta")
        self.ConsultaVentaHasta.setStyleSheet(u"color: #7D3928;\n"
"font: 12pt \"Century Gothic\";")
        self.ConsultaVentaHasta.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.ConsultaVentaHasta.setMinimumDate(QDate(2025, 1, 1))

        self.verticalLayout_36.addWidget(self.ConsultaVentaHasta)

        self.cmbClienteConsulta = QComboBox(self.widget_41)
        self.cmbClienteConsulta.setObjectName(u"cmbClienteConsulta")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.cmbClienteConsulta.sizePolicy().hasHeightForWidth())
        self.cmbClienteConsulta.setSizePolicy(sizePolicy8)
        self.cmbClienteConsulta.setMinimumSize(QSize(0, 25))
        self.cmbClienteConsulta.setMaximumSize(QSize(220, 16777215))
        font8 = QFont()
        font8.setFamilies([u"Century Gothic"])
        self.cmbClienteConsulta.setFont(font8)
        self.cmbClienteConsulta.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cmbClienteConsulta.setStyleSheet(u"QComboBox {\n"
"    font-family: \"Century Gothic\";\n"
"    font-size: 12px;\n"
"    color: #7D3928;\n"
"	padding: 3px;\n"
"	border: 2px solid #C18484;;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    font-family: \"Century Gothic\";\n"
"    font-size: 12px;\n"
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
"\\")
        self.cmbClienteConsulta.setEditable(True)
        self.cmbClienteConsulta.setMaxVisibleItems(5)

        self.verticalLayout_36.addWidget(self.cmbClienteConsulta)


        self.horizontalLayout_19.addWidget(self.widget_41)

        self.widget_42 = QWidget(self.encabezadoConsultaVenta)
        self.widget_42.setObjectName(u"widget_42")
        self.widget_42.setStyleSheet(u"border: 0;")
        self.verticalLayout_37 = QVBoxLayout(self.widget_42)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(-1, -1, 80, -1)
        self.btnConsultarVenta = QPushButton(self.widget_42)
        self.btnConsultarVenta.setObjectName(u"btnConsultarVenta")
        self.btnConsultarVenta.setMinimumSize(QSize(0, 35))
        self.btnConsultarVenta.setMaximumSize(QSize(150, 16777215))
        self.btnConsultarVenta.setFont(font3)
        self.btnConsultarVenta.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnConsultarVenta.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_37.addWidget(self.btnConsultarVenta)

        self.btnEliminarVenta = QPushButton(self.widget_42)
        self.btnEliminarVenta.setObjectName(u"btnEliminarVenta")
        self.btnEliminarVenta.setMinimumSize(QSize(0, 35))
        self.btnEliminarVenta.setMaximumSize(QSize(150, 16777215))
        self.btnEliminarVenta.setFont(font3)
        self.btnEliminarVenta.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnEliminarVenta.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_37.addWidget(self.btnEliminarVenta)


        self.horizontalLayout_19.addWidget(self.widget_42)


        self.verticalLayout_33.addWidget(self.encabezadoConsultaVenta)

        self.contenedorTablaConsulta = QWidget(self.MenuConsultaVenta)
        self.contenedorTablaConsulta.setObjectName(u"contenedorTablaConsulta")
        self.gridLayout_37 = QGridLayout(self.contenedorTablaConsulta)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_37.setContentsMargins(0, 0, 0, 0)
        self.tablaConsultaVentas = QTableWidget(self.contenedorTablaConsulta)
        self.tablaConsultaVentas.setObjectName(u"tablaConsultaVentas")
        self.tablaConsultaVentas.setStyleSheet(u"QTableWidget {\n"
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
"}")
        self.tablaConsultaVentas.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tablaConsultaVentas.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tablaConsultaVentas.setDragDropOverwriteMode(True)
        self.tablaConsultaVentas.setAlternatingRowColors(True)
        self.tablaConsultaVentas.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tablaConsultaVentas.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tablaConsultaVentas.horizontalHeader().setStretchLastSection(True)
        self.tablaConsultaVentas.verticalHeader().setVisible(False)

        self.gridLayout_37.addWidget(self.tablaConsultaVentas, 0, 0, 1, 1)


        self.verticalLayout_33.addWidget(self.contenedorTablaConsulta)

        self.stackedVentas.addWidget(self.MenuConsultaVenta)
        self.MenuNuevaVenta = QWidget()
        self.MenuNuevaVenta.setObjectName(u"MenuNuevaVenta")
        self.verticalLayout_25 = QVBoxLayout(self.MenuNuevaVenta)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.contenedorEncabezadoVentas = QWidget(self.MenuNuevaVenta)
        self.contenedorEncabezadoVentas.setObjectName(u"contenedorEncabezadoVentas")
        sizePolicy8.setHeightForWidth(self.contenedorEncabezadoVentas.sizePolicy().hasHeightForWidth())
        self.contenedorEncabezadoVentas.setSizePolicy(sizePolicy8)
        self.contenedorEncabezadoVentas.setMinimumSize(QSize(0, 80))
        self.contenedorEncabezadoVentas.setMaximumSize(QSize(16777215, 80))
        self.contenedorEncabezadoVentas.setStyleSheet(u"background-color: #F7E7DC;\n"
"border: 2px solid #DCBCA6;\n"
"border-radius: 10px\n"
"")
        self.horizontalLayout_11 = QHBoxLayout(self.contenedorEncabezadoVentas)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.contenedorTituloVentas = QWidget(self.contenedorEncabezadoVentas)
        self.contenedorTituloVentas.setObjectName(u"contenedorTituloVentas")
        self.contenedorTituloVentas.setStyleSheet(u"border: 0px;")
        self.gridLayout_10 = QGridLayout(self.contenedorTituloVentas)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.tituloNuevaVenta = QLabel(self.contenedorTituloVentas)
        self.tituloNuevaVenta.setObjectName(u"tituloNuevaVenta")
        self.tituloNuevaVenta.setFont(font6)
        self.tituloNuevaVenta.setStyleSheet(u"color: #7D3928;")

        self.gridLayout_10.addWidget(self.tituloNuevaVenta, 0, 0, 1, 1)


        self.horizontalLayout_11.addWidget(self.contenedorTituloVentas)

        self.contBotonConsulta = QWidget(self.contenedorEncabezadoVentas)
        self.contBotonConsulta.setObjectName(u"contBotonConsulta")
        self.contBotonConsulta.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.contBotonConsulta.setStyleSheet(u"border: 0px;")
        self.gridLayout_11 = QGridLayout(self.contBotonConsulta)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(180, -1, -1, -1)
        self.btnConsultaVentas = QPushButton(self.contBotonConsulta)
        self.btnConsultaVentas.setObjectName(u"btnConsultaVentas")
        self.btnConsultaVentas.setMinimumSize(QSize(0, 35))
        self.btnConsultaVentas.setMaximumSize(QSize(200, 16777215))
        self.btnConsultaVentas.setFont(font3)
        self.btnConsultaVentas.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnConsultaVentas.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_11.addWidget(self.btnConsultaVentas, 0, 0, 1, 1)


        self.horizontalLayout_11.addWidget(self.contBotonConsulta)


        self.verticalLayout_25.addWidget(self.contenedorEncabezadoVentas)

        self.cuerpoNuevaVenta = QWidget(self.MenuNuevaVenta)
        self.cuerpoNuevaVenta.setObjectName(u"cuerpoNuevaVenta")
        self.cuerpoNuevaVenta.setStyleSheet(u"border: 0;")
        self.verticalLayout_26 = QVBoxLayout(self.cuerpoNuevaVenta)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.formularioDatosVenta = QWidget(self.cuerpoNuevaVenta)
        self.formularioDatosVenta.setObjectName(u"formularioDatosVenta")
        sizePolicy8.setHeightForWidth(self.formularioDatosVenta.sizePolicy().hasHeightForWidth())
        self.formularioDatosVenta.setSizePolicy(sizePolicy8)
        self.formularioDatosVenta.setMaximumSize(QSize(16777215, 150))
        self.formularioDatosVenta.setStyleSheet(u"border: 2px solid #DEC4AE;\n"
"border-radius: 10px;")
        self.verticalLayout_28 = QVBoxLayout(self.formularioDatosVenta)
        self.verticalLayout_28.setSpacing(2)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(2, 5, 2, 7)
        self.widget_3 = QWidget(self.formularioDatosVenta)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 40))
        self.widget_3.setStyleSheet(u"border: 0")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_12.setSpacing(1)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.widget_3)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMaximumSize(QSize(100, 16777215))
        self.gridLayout_12 = QGridLayout(self.widget_7)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(5, 0, 0, 0)
        self.label = QLabel(self.widget_7)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(90, 0))
        self.label.setFont(font7)
        self.label.setStyleSheet(u"color: #7D3928;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_12.addWidget(self.label, 0, 0, 1, 1)


        self.horizontalLayout_12.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget_3)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(150, 0))
        self.widget_8.setMaximumSize(QSize(150, 16777215))
        self.gridLayout_16 = QGridLayout(self.widget_8)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(19, 0, 0, 0)
        self.txtCodigoProdVenta = QLineEdit(self.widget_8)
        self.txtCodigoProdVenta.setObjectName(u"txtCodigoProdVenta")
        self.txtCodigoProdVenta.setFont(font1)
        self.txtCodigoProdVenta.setStyleSheet(u"color: rgb(125, 57, 40);\n"
"border: 2px solid #C18484;\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"")

        self.gridLayout_16.addWidget(self.txtCodigoProdVenta, 0, 0, 1, 1)


        self.horizontalLayout_12.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.widget_3)
        self.widget_9.setObjectName(u"widget_9")
        self.gridLayout_17 = QGridLayout(self.widget_9)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(9, -1, -1, -1)
        self.lblDescripProdVenta = QLabel(self.widget_9)
        self.lblDescripProdVenta.setObjectName(u"lblDescripProdVenta")
        self.lblDescripProdVenta.setFont(font7)
        self.lblDescripProdVenta.setStyleSheet(u"color: #7D3928;")
        self.lblDescripProdVenta.setWordWrap(True)

        self.gridLayout_17.addWidget(self.lblDescripProdVenta, 0, 0, 1, 1)


        self.horizontalLayout_12.addWidget(self.widget_9)


        self.verticalLayout_28.addWidget(self.widget_3)

        self.widget_5 = QWidget(self.formularioDatosVenta)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(16777215, 50))
        self.widget_5.setStyleSheet(u"border:0")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.widget_10 = QWidget(self.widget_5)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy9)
        self.widget_10.setMinimumSize(QSize(270, 0))
        self.widget_10.setMaximumSize(QSize(250, 16777215))
        self.horizontalLayout_14 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.widget_13 = QWidget(self.widget_10)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMinimumSize(QSize(90, 0))
        self.gridLayout_13 = QGridLayout(self.widget_13)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(5, 0, 0, 0)
        self.label_3 = QLabel(self.widget_13)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font7)
        self.label_3.setStyleSheet(u"color: #7D3928;")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_13.addWidget(self.label_3, 0, 0, 1, 1)


        self.horizontalLayout_14.addWidget(self.widget_13)

        self.widget_14 = QWidget(self.widget_10)
        self.widget_14.setObjectName(u"widget_14")
        sizePolicy1.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy1)
        self.widget_14.setMinimumSize(QSize(150, 0))
        self.widget_14.setMaximumSize(QSize(150, 16777215))
        self.widget_14.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gridLayout_18 = QGridLayout(self.widget_14)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 17, 0)
        self.cmbVencVenta = QComboBox(self.widget_14)
        self.cmbVencVenta.setObjectName(u"cmbVencVenta")
        self.cmbVencVenta.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cmbVencVenta.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.cmbVencVenta.setStyleSheet(u"QComboBox {\n"
"    font-family: \"Century Gothic\";\n"
"    font-size: 14px;\n"
"    color: #7D3928;\n"
"	padding: 3px;\n"
"	border: 2px solid #C18484;;\n"
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
        self.cmbVencVenta.setMaxVisibleItems(5)

        self.gridLayout_18.addWidget(self.cmbVencVenta, 0, 0, 1, 1)


        self.horizontalLayout_14.addWidget(self.widget_14)


        self.horizontalLayout_13.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.widget_5)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy9.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy9)
        self.horizontalLayout_15 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(34, 0, 0, 0)
        self.widget_15 = QWidget(self.widget_11)
        self.widget_15.setObjectName(u"widget_15")
        self.gridLayout_14 = QGridLayout(self.widget_15)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_15.addWidget(self.widget_15)

        self.label_2 = QLabel(self.widget_11)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(95, 0))
        self.label_2.setFont(font7)
        self.label_2.setStyleSheet(u"color: #7D3928;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_2)

        self.widget_16 = QWidget(self.widget_11)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMinimumSize(QSize(180, 0))
        self.gridLayout_20 = QGridLayout(self.widget_16)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(0, 8, 100, 12)
        self.spinBoxCantidadVenta = QSpinBox(self.widget_16)
        self.spinBoxCantidadVenta.setObjectName(u"spinBoxCantidadVenta")
        sizePolicy4.setHeightForWidth(self.spinBoxCantidadVenta.sizePolicy().hasHeightForWidth())
        self.spinBoxCantidadVenta.setSizePolicy(sizePolicy4)
        self.spinBoxCantidadVenta.setMinimumSize(QSize(0, 35))
        self.spinBoxCantidadVenta.setMaximumSize(QSize(80, 16777215))
        font9 = QFont()
        font9.setFamilies([u"Century Gothic"])
        font9.setPointSize(12)
        font9.setBold(False)
        font9.setItalic(False)
        self.spinBoxCantidadVenta.setFont(font9)
        self.spinBoxCantidadVenta.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.spinBoxCantidadVenta.setStyleSheet(u" QSpinBox {\n"
"	font: 12pt \"Century Gothic\";\n"
"	color: rgb(125, 57, 40);\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"	width: 19;\n"
"	height:19;\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button {\n"
"	width: 19;\n"
"	height:19;\n"
"}\n"
"\n"
"")
        self.spinBoxCantidadVenta.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinBoxCantidadVenta.setReadOnly(False)
        self.spinBoxCantidadVenta.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)

        self.gridLayout_20.addWidget(self.spinBoxCantidadVenta, 0, 0, 1, 1)


        self.horizontalLayout_15.addWidget(self.widget_16)


        self.horizontalLayout_13.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.widget_5)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy9.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy9)
        self.widget_12.setMinimumSize(QSize(100, 0))
        self.horizontalLayout_16 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.widget_17 = QWidget(self.widget_12)
        self.widget_17.setObjectName(u"widget_17")
        self.gridLayout_15 = QGridLayout(self.widget_17)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_4 = QLabel(self.widget_17)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font7)
        self.label_4.setStyleSheet(u"color: #7D3928;")

        self.gridLayout_15.addWidget(self.label_4, 0, 0, 1, 1)


        self.horizontalLayout_16.addWidget(self.widget_17)

        self.widget_18 = QWidget(self.widget_12)
        self.widget_18.setObjectName(u"widget_18")
        self.gridLayout_19 = QGridLayout(self.widget_18)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.txtPrecioProdVenta = QLineEdit(self.widget_18)
        self.txtPrecioProdVenta.setObjectName(u"txtPrecioProdVenta")
        self.txtPrecioProdVenta.setFont(font1)
        self.txtPrecioProdVenta.setStyleSheet(u"color: rgb(125, 57, 40);\n"
"border: 2px solid #C18484;\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"")

        self.gridLayout_19.addWidget(self.txtPrecioProdVenta, 0, 0, 1, 1)


        self.horizontalLayout_16.addWidget(self.widget_18)


        self.horizontalLayout_13.addWidget(self.widget_12)


        self.verticalLayout_28.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.formularioDatosVenta)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(16777215, 40))
        self.widget_6.setStyleSheet(u"border:0")
        self.gridLayout_21 = QGridLayout(self.widget_6)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 4, 0, 0)
        self.btnAgregarCarrito = QPushButton(self.widget_6)
        self.btnAgregarCarrito.setObjectName(u"btnAgregarCarrito")
        self.btnAgregarCarrito.setMinimumSize(QSize(180, 35))
        self.btnAgregarCarrito.setMaximumSize(QSize(180, 16777215))
        self.btnAgregarCarrito.setFont(font1)
        self.btnAgregarCarrito.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAgregarCarrito.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_21.addWidget(self.btnAgregarCarrito, 0, 0, 1, 1)


        self.verticalLayout_28.addWidget(self.widget_6)


        self.verticalLayout_26.addWidget(self.formularioDatosVenta)

        self.cuerpoCarrito = QWidget(self.cuerpoNuevaVenta)
        self.cuerpoCarrito.setObjectName(u"cuerpoCarrito")
        sizePolicy.setHeightForWidth(self.cuerpoCarrito.sizePolicy().hasHeightForWidth())
        self.cuerpoCarrito.setSizePolicy(sizePolicy)
        self.cuerpoCarrito.setMinimumSize(QSize(0, 0))
        self.cuerpoCarrito.setMaximumSize(QSize(16777215, 280))
        self.cuerpoCarrito.setStyleSheet(u"border: 0px")
        self.verticalLayout_27 = QVBoxLayout(self.cuerpoCarrito)
        self.verticalLayout_27.setSpacing(2)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.contenedorCarrito = QWidget(self.cuerpoCarrito)
        self.contenedorCarrito.setObjectName(u"contenedorCarrito")
        sizePolicy.setHeightForWidth(self.contenedorCarrito.sizePolicy().hasHeightForWidth())
        self.contenedorCarrito.setSizePolicy(sizePolicy)
        self.contenedorCarrito.setMinimumSize(QSize(0, 200))
        self.contenedorCarrito.setMaximumSize(QSize(16777215, 200))
        self.contenedorCarrito.setStyleSheet(u"border: 0px;")
        self.gridLayout_22 = QGridLayout(self.contenedorCarrito)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(0, 5, 0, 0)
        self.tablaCarrito = QTableView(self.contenedorCarrito)
        self.tablaCarrito.setObjectName(u"tablaCarrito")
        sizePolicy4.setHeightForWidth(self.tablaCarrito.sizePolicy().hasHeightForWidth())
        self.tablaCarrito.setSizePolicy(sizePolicy4)
        self.tablaCarrito.setStyleSheet(u"\n"
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
        self.tablaCarrito.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tablaCarrito.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked)
        self.tablaCarrito.setAlternatingRowColors(True)
        self.tablaCarrito.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tablaCarrito.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tablaCarrito.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_22.addWidget(self.tablaCarrito, 0, 0, 1, 1)


        self.verticalLayout_27.addWidget(self.contenedorCarrito)

        self.botoneraCarrito = QWidget(self.cuerpoCarrito)
        self.botoneraCarrito.setObjectName(u"botoneraCarrito")
        sizePolicy8.setHeightForWidth(self.botoneraCarrito.sizePolicy().hasHeightForWidth())
        self.botoneraCarrito.setSizePolicy(sizePolicy8)
        self.botoneraCarrito.setMinimumSize(QSize(0, 50))
        self.botoneraCarrito.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_17 = QHBoxLayout(self.botoneraCarrito)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 0, -1, 9)
        self.widget = QWidget(self.botoneraCarrito)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(300, 16777215))
        self.horizontalLayout_18 = QHBoxLayout(self.widget)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.btnQuitarCarrito = QPushButton(self.widget)
        self.btnQuitarCarrito.setObjectName(u"btnQuitarCarrito")
        self.btnQuitarCarrito.setMinimumSize(QSize(0, 30))
        self.btnQuitarCarrito.setFont(font1)
        self.btnQuitarCarrito.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnQuitarCarrito.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_18.addWidget(self.btnQuitarCarrito)

        self.btnVaciarCarrito = QPushButton(self.widget)
        self.btnVaciarCarrito.setObjectName(u"btnVaciarCarrito")
        self.btnVaciarCarrito.setMinimumSize(QSize(0, 30))
        self.btnVaciarCarrito.setFont(font1)
        self.btnVaciarCarrito.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnVaciarCarrito.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_18.addWidget(self.btnVaciarCarrito)


        self.horizontalLayout_17.addWidget(self.widget)

        self.widget_2 = QWidget(self.botoneraCarrito)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_23 = QGridLayout(self.widget_2)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(17, -1, -1, -1)
        self.lblTotalEnCarrito = QLabel(self.widget_2)
        self.lblTotalEnCarrito.setObjectName(u"lblTotalEnCarrito")
        self.lblTotalEnCarrito.setFont(font7)
        self.lblTotalEnCarrito.setStyleSheet(u"color: #7D3928;")
        self.lblTotalEnCarrito.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lblTotalEnCarrito.setWordWrap(True)

        self.gridLayout_23.addWidget(self.lblTotalEnCarrito, 0, 0, 1, 1)


        self.horizontalLayout_17.addWidget(self.widget_2)


        self.verticalLayout_27.addWidget(self.botoneraCarrito)


        self.verticalLayout_26.addWidget(self.cuerpoCarrito)

        self.cuerpoFinalizacionVenta = QWidget(self.cuerpoNuevaVenta)
        self.cuerpoFinalizacionVenta.setObjectName(u"cuerpoFinalizacionVenta")
        sizePolicy.setHeightForWidth(self.cuerpoFinalizacionVenta.sizePolicy().hasHeightForWidth())
        self.cuerpoFinalizacionVenta.setSizePolicy(sizePolicy)
        self.cuerpoFinalizacionVenta.setMinimumSize(QSize(0, 100))
        self.cuerpoFinalizacionVenta.setMaximumSize(QSize(16777215, 16777215))
        self.cuerpoFinalizacionVenta.setStyleSheet(u"border: 2px solid #DEC4AE;\n"
"border-radius: 10px;")
        self.gridLayout_34 = QGridLayout(self.cuerpoFinalizacionVenta)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_34.setHorizontalSpacing(0)
        self.gridLayout_34.setVerticalSpacing(8)
        self.gridLayout_34.setContentsMargins(4, 4, 4, 4)
        self.widget_37 = QWidget(self.cuerpoFinalizacionVenta)
        self.widget_37.setObjectName(u"widget_37")
        self.widget_37.setStyleSheet(u"border: 0")
        self.verticalLayout_32 = QVBoxLayout(self.widget_37)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.widget_37)
        self.label_6.setObjectName(u"label_6")
        font10 = QFont()
        font10.setFamilies([u"Century Gothic"])
        font10.setPointSize(14)
        font10.setBold(True)
        self.label_6.setFont(font10)
        self.label_6.setStyleSheet(u"color: #7D3928;")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_6)


        self.gridLayout_34.addWidget(self.widget_37, 0, 0, 1, 2)

        self.widget_19 = QWidget(self.cuerpoFinalizacionVenta)
        self.widget_19.setObjectName(u"widget_19")
        sizePolicy9.setHeightForWidth(self.widget_19.sizePolicy().hasHeightForWidth())
        self.widget_19.setSizePolicy(sizePolicy9)
        self.widget_19.setStyleSheet(u"border: 0px;\n"
"border-radius: 10px;")
        self.verticalLayout_29 = QVBoxLayout(self.widget_19)
        self.verticalLayout_29.setSpacing(9)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.widget_21 = QWidget(self.widget_19)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_20 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.widget_27 = QWidget(self.widget_21)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setMinimumSize(QSize(102, 0))
        self.widget_27.setMaximumSize(QSize(150, 16777215))
        self.gridLayout_25 = QGridLayout(self.widget_27)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(4, 0, 0, 0)
        self.label_7 = QLabel(self.widget_27)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font7)
        self.label_7.setStyleSheet(u"color: #7D3928;")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_25.addWidget(self.label_7, 0, 0, 1, 1)


        self.horizontalLayout_20.addWidget(self.widget_27)

        self.widget_28 = QWidget(self.widget_21)
        self.widget_28.setObjectName(u"widget_28")
        self.gridLayout_26 = QGridLayout(self.widget_28)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(6, 0, 121, 0)
        self.cmbClienteVenta = QComboBox(self.widget_28)
        self.cmbClienteVenta.setObjectName(u"cmbClienteVenta")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.cmbClienteVenta.sizePolicy().hasHeightForWidth())
        self.cmbClienteVenta.setSizePolicy(sizePolicy10)
        self.cmbClienteVenta.setMaximumSize(QSize(250, 16777215))
        self.cmbClienteVenta.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cmbClienteVenta.setStyleSheet(u"QComboBox {\n"
"    font-family: \"Century Gothic\";\n"
"    font-size: 14px;\n"
"    color: #7D3928;\n"
"	padding: 3px;\n"
"	border: 2px solid #C18484;;\n"
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
        self.cmbClienteVenta.setEditable(True)
        self.cmbClienteVenta.setMaxVisibleItems(5)

        self.gridLayout_26.addWidget(self.cmbClienteVenta, 0, 0, 1, 1)


        self.horizontalLayout_20.addWidget(self.widget_28)


        self.verticalLayout_29.addWidget(self.widget_21)

        self.widget_22 = QWidget(self.widget_19)
        self.widget_22.setObjectName(u"widget_22")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.widget_29 = QWidget(self.widget_22)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setMaximumSize(QSize(100, 16777215))
        self.gridLayout_27 = QGridLayout(self.widget_29)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(4, 0, 0, 0)
        self.label_8 = QLabel(self.widget_29)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font7)
        self.label_8.setStyleSheet(u"color: #7D3928;")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_27.addWidget(self.label_8, 0, 0, 1, 1)


        self.horizontalLayout_21.addWidget(self.widget_29)

        self.widget_30 = QWidget(self.widget_22)
        self.widget_30.setObjectName(u"widget_30")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_30)
        self.horizontalLayout_22.setSpacing(11)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.rbtnEfectivo = QRadioButton(self.widget_30)
        self.rbtnEfectivo.setObjectName(u"rbtnEfectivo")
        self.rbtnEfectivo.setFont(font1)
        self.rbtnEfectivo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.rbtnEfectivo.setStyleSheet(u"QRadioButton {\n"
"	color: #7D3928;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"        width: 12px;\n"
"        height: 12px;\n"
"        border: 2px solid #C18484;\n"
"        border-radius: 8px;\n"
"        background: white;\n"
"    }\n"
"\n"
"QRadioButton::indicator:checked {\n"
"        background-color: #C18484;\n"
"        border: 2px solid #C18484;\n"
"    }\n"
"")

        self.horizontalLayout_22.addWidget(self.rbtnEfectivo)

        self.rbtnTransf = QRadioButton(self.widget_30)
        self.rbtnTransf.setObjectName(u"rbtnTransf")
        self.rbtnTransf.setFont(font1)
        self.rbtnTransf.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.rbtnTransf.setStyleSheet(u"QRadioButton {\n"
"	color: #7D3928;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"        width: 12px;\n"
"        height: 12px;\n"
"        border: 2px solid #C18484;\n"
"        border-radius: 8px;\n"
"        background: white;\n"
"    }\n"
"\n"
"QRadioButton::indicator:checked {\n"
"        background-color: #C18484;\n"
"        border: 2px solid #C18484;\n"
"    }\n"
"")
        self.rbtnTransf.setCheckable(True)
        self.rbtnTransf.setChecked(False)

        self.horizontalLayout_22.addWidget(self.rbtnTransf)

        self.rbtnTarjeta = QRadioButton(self.widget_30)
        self.rbtnTarjeta.setObjectName(u"rbtnTarjeta")
        self.rbtnTarjeta.setFont(font1)
        self.rbtnTarjeta.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.rbtnTarjeta.setStyleSheet(u"QRadioButton {\n"
"	color: #7D3928;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"        width: 12px;\n"
"        height: 12px;\n"
"        border: 2px solid #C18484;\n"
"        border-radius: 8px;\n"
"        background: white;\n"
"    }\n"
"\n"
"QRadioButton::indicator:checked {\n"
"        background-color: #C18484;\n"
"        border: 2px solid #C18484;\n"
"    }\n"
"")

        self.horizontalLayout_22.addWidget(self.rbtnTarjeta)


        self.horizontalLayout_21.addWidget(self.widget_30)


        self.verticalLayout_29.addWidget(self.widget_22)

        self.widget_26 = QWidget(self.widget_19)
        self.widget_26.setObjectName(u"widget_26")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.widget_31 = QWidget(self.widget_26)
        self.widget_31.setObjectName(u"widget_31")
        font11 = QFont()
        font11.setBold(False)
        self.widget_31.setFont(font11)
        self.gridLayout_28 = QGridLayout(self.widget_31)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setContentsMargins(4, 0, 0, 0)
        self.checkInteres = QCheckBox(self.widget_31)
        self.checkInteres.setObjectName(u"checkInteres")
        self.checkInteres.setFont(font7)
        self.checkInteres.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkInteres.setStyleSheet(u"QCheckBox {\n"
"	color: #7D3928;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"        width: 12px;\n"
"        height: 12px;\n"
"        border: 1px solid #C18484;\n"
"        border-radius: 8px;\n"
"        background: white;\n"
"    }\n"
"\n"
"QCheckBox::indicator:checked {\n"
"        background-color: #C18484;\n"
"        border: 1px solid #C18484;\n"
"    }\n"
"")

        self.gridLayout_28.addWidget(self.checkInteres, 0, 0, 1, 1)


        self.horizontalLayout_23.addWidget(self.widget_31)

        self.widget_32 = QWidget(self.widget_26)
        self.widget_32.setObjectName(u"widget_32")
        self.gridLayout_29 = QGridLayout(self.widget_32)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(8, -1, 120, -1)
        self.txtInteresVenta = QLineEdit(self.widget_32)
        self.txtInteresVenta.setObjectName(u"txtInteresVenta")
        self.txtInteresVenta.setMaximumSize(QSize(250, 16777215))
        self.txtInteresVenta.setFont(font1)
        self.txtInteresVenta.setStyleSheet(u"color: rgb(125, 57, 40);\n"
"border: 2px solid #C18484;\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"")

        self.gridLayout_29.addWidget(self.txtInteresVenta, 0, 0, 1, 1)


        self.horizontalLayout_23.addWidget(self.widget_32)


        self.verticalLayout_29.addWidget(self.widget_26)


        self.gridLayout_34.addWidget(self.widget_19, 1, 0, 1, 1)

        self.widget_20 = QWidget(self.cuerpoFinalizacionVenta)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setMinimumSize(QSize(400, 0))
        self.widget_20.setStyleSheet(u"border: 0px;")
        self.verticalLayout_30 = QVBoxLayout(self.widget_20)
        self.verticalLayout_30.setSpacing(13)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.widget_24 = QWidget(self.widget_20)
        self.widget_24.setObjectName(u"widget_24")
        self.verticalLayout_31 = QVBoxLayout(self.widget_24)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.widget_33 = QWidget(self.widget_24)
        self.widget_33.setObjectName(u"widget_33")
        sizePolicy1.setHeightForWidth(self.widget_33.sizePolicy().hasHeightForWidth())
        self.widget_33.setSizePolicy(sizePolicy1)
        self.widget_33.setMinimumSize(QSize(0, 0))
        self.widget_33.setMaximumSize(QSize(405, 16777215))
        self.gridLayout_31 = QGridLayout(self.widget_33)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setVerticalSpacing(10)
        self.gridLayout_31.setContentsMargins(-1, 0, -1, -1)
        self.lblTotalAbonar = QLabel(self.widget_33)
        self.lblTotalAbonar.setObjectName(u"lblTotalAbonar")
        sizePolicy1.setHeightForWidth(self.lblTotalAbonar.sizePolicy().hasHeightForWidth())
        self.lblTotalAbonar.setSizePolicy(sizePolicy1)
        self.lblTotalAbonar.setFont(font10)
        self.lblTotalAbonar.setStyleSheet(u"color: #7D3928;")
        self.lblTotalAbonar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_31.addWidget(self.lblTotalAbonar, 0, 0, 1, 1)


        self.verticalLayout_31.addWidget(self.widget_33)

        self.widget_34 = QWidget(self.widget_24)
        self.widget_34.setObjectName(u"widget_34")
        self.widget_34.setMinimumSize(QSize(0, 35))
        self.horizontalLayout_24 = QHBoxLayout(self.widget_34)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.widget_35 = QWidget(self.widget_34)
        self.widget_35.setObjectName(u"widget_35")
        self.gridLayout_32 = QGridLayout(self.widget_35)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setContentsMargins(0, 0, 0, 4)
        self.label_10 = QLabel(self.widget_35)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(150, 0))
        self.label_10.setFont(font7)
        self.label_10.setStyleSheet(u"color: #7D3928;")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_32.addWidget(self.label_10, 0, 0, 1, 1)


        self.horizontalLayout_24.addWidget(self.widget_35)

        self.widget_36 = QWidget(self.widget_34)
        self.widget_36.setObjectName(u"widget_36")
        self.widget_36.setMinimumSize(QSize(0, 0))
        self.widget_36.setMaximumSize(QSize(16777215, 150))
        self.gridLayout_33 = QGridLayout(self.widget_36)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_33.setContentsMargins(0, 0, 60, 0)
        self.txtEntrega = QLineEdit(self.widget_36)
        self.txtEntrega.setObjectName(u"txtEntrega")
        self.txtEntrega.setMaximumSize(QSize(150, 16777215))
        self.txtEntrega.setFont(font1)
        self.txtEntrega.setStyleSheet(u"color: rgb(125, 57, 40);\n"
"border: 2px solid #C18484;\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"")

        self.gridLayout_33.addWidget(self.txtEntrega, 0, 0, 1, 1)


        self.horizontalLayout_24.addWidget(self.widget_36)


        self.verticalLayout_31.addWidget(self.widget_34)


        self.verticalLayout_30.addWidget(self.widget_24)

        self.widget_25 = QWidget(self.widget_20)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setMaximumSize(QSize(16777215, 40))
        self.gridLayout_30 = QGridLayout(self.widget_25)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(-1, 0, -1, -1)
        self.btnFinalizarVenta = QPushButton(self.widget_25)
        self.btnFinalizarVenta.setObjectName(u"btnFinalizarVenta")
        self.btnFinalizarVenta.setMinimumSize(QSize(0, 35))
        self.btnFinalizarVenta.setMaximumSize(QSize(150, 16777215))
        self.btnFinalizarVenta.setFont(font1)
        self.btnFinalizarVenta.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnFinalizarVenta.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_30.addWidget(self.btnFinalizarVenta, 0, 0, 1, 1)


        self.verticalLayout_30.addWidget(self.widget_25)


        self.gridLayout_34.addWidget(self.widget_20, 1, 1, 1, 1)


        self.verticalLayout_26.addWidget(self.cuerpoFinalizacionVenta)


        self.verticalLayout_25.addWidget(self.cuerpoNuevaVenta)

        self.stackedVentas.addWidget(self.MenuNuevaVenta)

        self.gridLayout_9.addWidget(self.stackedVentas, 0, 0, 1, 1)

        self.StackedWidget.addWidget(self.MenuVentas)
        self.MenuCuentaCorriente = QWidget()
        self.MenuCuentaCorriente.setObjectName(u"MenuCuentaCorriente")
        self.verticalLayout_38 = QVBoxLayout(self.MenuCuentaCorriente)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.encabezadoCCorriente = QWidget(self.MenuCuentaCorriente)
        self.encabezadoCCorriente.setObjectName(u"encabezadoCCorriente")
        self.encabezadoCCorriente.setMaximumSize(QSize(16777215, 100))
        self.encabezadoCCorriente.setStyleSheet(u"background-color: #F7E7DC;\n"
"border: 2px solid #DCBCA6;\n"
"border-radius: 10px\n"
"")
        self.horizontalLayout_25 = QHBoxLayout(self.encabezadoCCorriente)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(4, 4, 4, 4)
        self.widget_23 = QWidget(self.encabezadoCCorriente)
        self.widget_23.setObjectName(u"widget_23")
        self.widget_23.setMaximumSize(QSize(300, 16777215))
        self.widget_23.setStyleSheet(u"border: 0")
        self.gridLayout_36 = QGridLayout(self.widget_23)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.label_13 = QLabel(self.widget_23)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font6)
        self.label_13.setStyleSheet(u"color: rgb(125, 57, 40);")
        self.label_13.setWordWrap(True)

        self.gridLayout_36.addWidget(self.label_13, 0, 0, 1, 1)


        self.horizontalLayout_25.addWidget(self.widget_23)

        self.widget_47 = QWidget(self.encabezadoCCorriente)
        self.widget_47.setObjectName(u"widget_47")
        self.widget_47.setMaximumSize(QSize(100, 16777215))
        self.widget_47.setStyleSheet(u"border: 0")
        self.gridLayout_38 = QGridLayout(self.widget_47)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.label_14 = QLabel(self.widget_47)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font10)
        self.label_14.setStyleSheet(u"color: rgb(125, 57, 40);")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_38.addWidget(self.label_14, 0, 0, 1, 1)


        self.horizontalLayout_25.addWidget(self.widget_47)

        self.frame = QFrame(self.encabezadoCCorriente)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(200, 16777215))
        self.frame.setStyleSheet(u"border: 0;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_39 = QGridLayout(self.frame)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_39.setContentsMargins(0, -1, -1, -1)
        self.cmbClienteCC = QComboBox(self.frame)
        self.cmbClienteCC.setObjectName(u"cmbClienteCC")
        self.cmbClienteCC.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cmbClienteCC.setStyleSheet(u"QComboBox {\n"
"    font-family: \"Century Gothic\";\n"
"    font-size: 12px;\n"
"    color: #7D3928;\n"
"	padding: 3px;\n"
"	border: 2px solid #C18484;;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    font-family: \"Century Gothic\";\n"
"    font-size: 12px;\n"
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
        self.cmbClienteCC.setEditable(False)
        self.cmbClienteCC.setMaxVisibleItems(5)

        self.gridLayout_39.addWidget(self.cmbClienteCC, 0, 0, 1, 1)


        self.horizontalLayout_25.addWidget(self.frame)

        self.widget_48 = QWidget(self.encabezadoCCorriente)
        self.widget_48.setObjectName(u"widget_48")
        self.widget_48.setStyleSheet(u"border: 0")
        self.gridLayout_40 = QGridLayout(self.widget_48)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_40.setContentsMargins(0, -1, 50, -1)

        self.horizontalLayout_25.addWidget(self.widget_48)


        self.verticalLayout_38.addWidget(self.encabezadoCCorriente)

        self.widgetTablaCC = QWidget(self.MenuCuentaCorriente)
        self.widgetTablaCC.setObjectName(u"widgetTablaCC")
        self.widgetTablaCC.setMaximumSize(QSize(16777215, 350))
        self.gridLayout_41 = QGridLayout(self.widgetTablaCC)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.gridLayout_41.setContentsMargins(0, 0, 0, 0)
        self.tablaCuentaCorriente = QTableView(self.widgetTablaCC)
        self.tablaCuentaCorriente.setObjectName(u"tablaCuentaCorriente")
        self.tablaCuentaCorriente.setStyleSheet(u"\n"
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
        self.tablaCuentaCorriente.horizontalHeader().setStretchLastSection(True)
        self.tablaCuentaCorriente.verticalHeader().setVisible(False)

        self.gridLayout_41.addWidget(self.tablaCuentaCorriente, 0, 0, 1, 1)


        self.verticalLayout_38.addWidget(self.widgetTablaCC)

        self.widgetTotalCC = QWidget(self.MenuCuentaCorriente)
        self.widgetTotalCC.setObjectName(u"widgetTotalCC")
        self.widgetTotalCC.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_27 = QHBoxLayout(self.widgetTotalCC)
        self.horizontalLayout_27.setSpacing(4)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(2, 0, -1, -1)
        self.btnEliminarUltimaCC = QPushButton(self.widgetTotalCC)
        self.btnEliminarUltimaCC.setObjectName(u"btnEliminarUltimaCC")
        self.btnEliminarUltimaCC.setMinimumSize(QSize(0, 30))
        self.btnEliminarUltimaCC.setMaximumSize(QSize(200, 16777215))
        self.btnEliminarUltimaCC.setFont(font1)
        self.btnEliminarUltimaCC.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnEliminarUltimaCC.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_27.addWidget(self.btnEliminarUltimaCC)

        self.lblDeudaTotalCC = QLabel(self.widgetTotalCC)
        self.lblDeudaTotalCC.setObjectName(u"lblDeudaTotalCC")
        self.lblDeudaTotalCC.setFont(font10)
        self.lblDeudaTotalCC.setStyleSheet(u"color: rgb(125, 57, 40);")
        self.lblDeudaTotalCC.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_27.addWidget(self.lblDeudaTotalCC)


        self.verticalLayout_38.addWidget(self.widgetTotalCC)

        self.widgetActualicCC = QWidget(self.MenuCuentaCorriente)
        self.widgetActualicCC.setObjectName(u"widgetActualicCC")
        self.verticalLayout_39 = QVBoxLayout(self.widgetActualicCC)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.widget_46 = QWidget(self.widgetActualicCC)
        self.widget_46.setObjectName(u"widget_46")
        self.horizontalLayout_26 = QHBoxLayout(self.widget_46)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.widget_38 = QWidget(self.widget_46)
        self.widget_38.setObjectName(u"widget_38")
        self.widget_38.setMaximumSize(QSize(400, 16777215))
        self.gridLayout_43 = QGridLayout(self.widget_38)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.rbtnSaldarCC = QRadioButton(self.widget_38)
        self.rbtnSaldarCC.setObjectName(u"rbtnSaldarCC")
        self.rbtnSaldarCC.setFont(font1)
        self.rbtnSaldarCC.setStyleSheet(u"QRadioButton {\n"
"	color: #7D3928;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"        width: 12px;\n"
"        height: 12px;\n"
"        border: 2px solid #C18484;\n"
"        border-radius: 8px;\n"
"        background: white;\n"
"    }\n"
"\n"
"QRadioButton::indicator:checked {\n"
"        background-color: #C18484;\n"
"        border: 2px solid #C18484;\n"
"    }\n"
"")

        self.gridLayout_43.addWidget(self.rbtnSaldarCC, 0, 0, 1, 1)

        self.rbtnActualizarCC = QRadioButton(self.widget_38)
        self.rbtnActualizarCC.setObjectName(u"rbtnActualizarCC")
        self.rbtnActualizarCC.setFont(font1)
        self.rbtnActualizarCC.setStyleSheet(u"QRadioButton {\n"
"	color: #7D3928;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"        width: 12px;\n"
"        height: 12px;\n"
"        border: 2px solid #C18484;\n"
"        border-radius: 8px;\n"
"        background: white;\n"
"    }\n"
"\n"
"QRadioButton::indicator:checked {\n"
"        background-color: #C18484;\n"
"        border: 2px solid #C18484;\n"
"    }\n"
"")

        self.gridLayout_43.addWidget(self.rbtnActualizarCC, 0, 1, 1, 1)


        self.horizontalLayout_26.addWidget(self.widget_38)

        self.widget_49 = QWidget(self.widget_46)
        self.widget_49.setObjectName(u"widget_49")
        self.widget_49.setMaximumSize(QSize(250, 16777215))
        self.gridLayout_44 = QGridLayout(self.widget_49)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.label_16 = QLabel(self.widget_49)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font7)
        self.label_16.setStyleSheet(u"color: rgb(125, 57, 40);")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_44.addWidget(self.label_16, 0, 0, 1, 1)


        self.horizontalLayout_26.addWidget(self.widget_49)

        self.widget_50 = QWidget(self.widget_46)
        self.widget_50.setObjectName(u"widget_50")
        self.widget_50.setMaximumSize(QSize(200, 16777215))
        self.gridLayout_45 = QGridLayout(self.widget_50)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.txtMontoCC = QLineEdit(self.widget_50)
        self.txtMontoCC.setObjectName(u"txtMontoCC")
        self.txtMontoCC.setFont(font1)
        self.txtMontoCC.setStyleSheet(u"color: rgb(125, 57, 40);\n"
"border: 2px solid #C18484;\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"")

        self.gridLayout_45.addWidget(self.txtMontoCC, 0, 0, 1, 1)


        self.horizontalLayout_26.addWidget(self.widget_50)


        self.verticalLayout_39.addWidget(self.widget_46)

        self.widget_45 = QWidget(self.widgetActualicCC)
        self.widget_45.setObjectName(u"widget_45")
        self.gridLayout_46 = QGridLayout(self.widget_45)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.btnCargarCC = QPushButton(self.widget_45)
        self.btnCargarCC.setObjectName(u"btnCargarCC")
        self.btnCargarCC.setMinimumSize(QSize(0, 35))
        self.btnCargarCC.setMaximumSize(QSize(150, 16777215))
        self.btnCargarCC.setFont(font3)
        self.btnCargarCC.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnCargarCC.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_46.addWidget(self.btnCargarCC, 0, 0, 1, 1)


        self.verticalLayout_39.addWidget(self.widget_45)


        self.verticalLayout_38.addWidget(self.widgetActualicCC)

        self.StackedWidget.addWidget(self.MenuCuentaCorriente)
        self.MenuProductos = QWidget()
        self.MenuProductos.setObjectName(u"MenuProductos")
        self.verticalLayout_21 = QVBoxLayout(self.MenuProductos)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(2, 0, 2, 0)
        self.encabezadoProducto = QWidget(self.MenuProductos)
        self.encabezadoProducto.setObjectName(u"encabezadoProducto")
        sizePolicy.setHeightForWidth(self.encabezadoProducto.sizePolicy().hasHeightForWidth())
        self.encabezadoProducto.setSizePolicy(sizePolicy)
        self.encabezadoProducto.setMinimumSize(QSize(0, 150))
        self.encabezadoProducto.setMaximumSize(QSize(16777215, 150))
        self.encabezadoProducto.setStyleSheet(u"background-color: #F7E7DC;\n"
"border: 2px solid #DCBCA6;\n"
"border-radius: 10px\n"
"")
        self.horizontalLayout_10 = QHBoxLayout(self.encabezadoProducto)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.widgetEncabezado = QWidget(self.encabezadoProducto)
        self.widgetEncabezado.setObjectName(u"widgetEncabezado")
        self.widgetEncabezado.setStyleSheet(u"border: 0px;")
        self.gridLayout_7 = QGridLayout(self.widgetEncabezado)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.tituloProducto = QLabel(self.widgetEncabezado)
        self.tituloProducto.setObjectName(u"tituloProducto")
        self.tituloProducto.setFont(font2)
        self.tituloProducto.setStyleSheet(u"color: rgb(125, 57, 40);")

        self.gridLayout_7.addWidget(self.tituloProducto, 0, 0, 1, 1)


        self.horizontalLayout_10.addWidget(self.widgetEncabezado)

        self.labelsProducto = QWidget(self.encabezadoProducto)
        self.labelsProducto.setObjectName(u"labelsProducto")
        self.labelsProducto.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.labelsProducto.setStyleSheet(u"border: 0px;")
        self.verticalLayout_22 = QVBoxLayout(self.labelsProducto)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(30, -1, -1, -1)
        self.lblCodigo = QLabel(self.labelsProducto)
        self.lblCodigo.setObjectName(u"lblCodigo")
        self.lblCodigo.setFont(font10)
        self.lblCodigo.setStyleSheet(u"color: #7D3928;")
        self.lblCodigo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_22.addWidget(self.lblCodigo)

        self.lblDescripcion = QLabel(self.labelsProducto)
        self.lblDescripcion.setObjectName(u"lblDescripcion")
        self.lblDescripcion.setFont(font10)
        self.lblDescripcion.setStyleSheet(u"color: #7D3928;")
        self.lblDescripcion.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_22.addWidget(self.lblDescripcion)


        self.horizontalLayout_10.addWidget(self.labelsProducto)

        self.lineEditsProducto = QWidget(self.encabezadoProducto)
        self.lineEditsProducto.setObjectName(u"lineEditsProducto")
        self.lineEditsProducto.setMaximumSize(QSize(200, 16777215))
        self.lineEditsProducto.setStyleSheet(u"border: 0px;")
        self.verticalLayout_23 = QVBoxLayout(self.lineEditsProducto)
        self.verticalLayout_23.setSpacing(19)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, -1, -1, -1)
        self.txtCodigoProd = QLineEdit(self.lineEditsProducto)
        self.txtCodigoProd.setObjectName(u"txtCodigoProd")
        self.txtCodigoProd.setFont(font3)
        self.txtCodigoProd.setStyleSheet(u"color: rgb(125, 57, 40);\n"
"border: 2px solid #C18484;\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"")

        self.verticalLayout_23.addWidget(self.txtCodigoProd)

        self.txtDescripcionProd = QLineEdit(self.lineEditsProducto)
        self.txtDescripcionProd.setObjectName(u"txtDescripcionProd")
        self.txtDescripcionProd.setFont(font3)
        self.txtDescripcionProd.setStyleSheet(u"color: rgb(125, 57, 40);\n"
"border: 2px solid #C18484;\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"")

        self.verticalLayout_23.addWidget(self.txtDescripcionProd)


        self.horizontalLayout_10.addWidget(self.lineEditsProducto)

        self.widgetBtnFiltro = QWidget(self.encabezadoProducto)
        self.widgetBtnFiltro.setObjectName(u"widgetBtnFiltro")
        self.widgetBtnFiltro.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.widgetBtnFiltro.setStyleSheet(u"border: 0px;")
        self.gridLayout_8 = QGridLayout(self.widgetBtnFiltro)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, -1, -1, -1)
        self.btnFiltrarProductos = QPushButton(self.widgetBtnFiltro)
        self.btnFiltrarProductos.setObjectName(u"btnFiltrarProductos")
        self.btnFiltrarProductos.setMinimumSize(QSize(100, 30))
        self.btnFiltrarProductos.setMaximumSize(QSize(100, 16777215))
        self.btnFiltrarProductos.setFont(font3)
        self.btnFiltrarProductos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnFiltrarProductos.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnFiltrarProductos.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_8.addWidget(self.btnFiltrarProductos, 0, 0, 1, 1)


        self.horizontalLayout_10.addWidget(self.widgetBtnFiltro)

        self.widgetBtnProductos = QWidget(self.encabezadoProducto)
        self.widgetBtnProductos.setObjectName(u"widgetBtnProductos")
        self.widgetBtnProductos.setStyleSheet(u"border: 0px;")
        self.verticalLayout_24 = QVBoxLayout(self.widgetBtnProductos)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(10, -1, 10, -1)
        self.btnNuevoProducto = QPushButton(self.widgetBtnProductos)
        self.btnNuevoProducto.setObjectName(u"btnNuevoProducto")
        self.btnNuevoProducto.setMinimumSize(QSize(180, 40))
        self.btnNuevoProducto.setFont(font3)
        self.btnNuevoProducto.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnNuevoProducto.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_24.addWidget(self.btnNuevoProducto)

        self.btnEliminarProducto = QPushButton(self.widgetBtnProductos)
        self.btnEliminarProducto.setObjectName(u"btnEliminarProducto")
        self.btnEliminarProducto.setMinimumSize(QSize(180, 40))
        self.btnEliminarProducto.setFont(font3)
        self.btnEliminarProducto.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnEliminarProducto.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_24.addWidget(self.btnEliminarProducto)


        self.horizontalLayout_10.addWidget(self.widgetBtnProductos)


        self.verticalLayout_21.addWidget(self.encabezadoProducto)

        self.widgetTablaProducto = QWidget(self.MenuProductos)
        self.widgetTablaProducto.setObjectName(u"widgetTablaProducto")
        self.widgetTablaProducto.setMaximumSize(QSize(16777215, 16777215))
        self.widgetTablaProducto.setStyleSheet(u"border: 0px;")
        self.gridLayout_6 = QGridLayout(self.widgetTablaProducto)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.tablaProductos = QTableView(self.widgetTablaProducto)
        self.tablaProductos.setObjectName(u"tablaProductos")
        self.tablaProductos.setStyleSheet(u"\n"
"QTableView {\n"
"	border: 2px solid #DEC4AE;\n"
"	border-radius: 10px;\n"
"	color: rgb(125, 57, 40);\n"
"	font: 10pt \"Century Gothic\";\n"
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
        self.tablaProductos.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tablaProductos.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked)
        self.tablaProductos.setAlternatingRowColors(True)
        self.tablaProductos.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tablaProductos.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tablaProductos.horizontalHeader().setStretchLastSection(True)
        self.tablaProductos.verticalHeader().setVisible(False)

        self.gridLayout_6.addWidget(self.tablaProductos, 0, 0, 1, 1)


        self.verticalLayout_21.addWidget(self.widgetTablaProducto)

        self.StackedWidget.addWidget(self.MenuProductos)
        self.MenuHistorial = QWidget()
        self.MenuHistorial.setObjectName(u"MenuHistorial")
        self.verticalLayout_18 = QVBoxLayout(self.MenuHistorial)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(2, 0, 2, 0)
        self.encabezadoHistorial = QWidget(self.MenuHistorial)
        self.encabezadoHistorial.setObjectName(u"encabezadoHistorial")
        self.encabezadoHistorial.setMaximumSize(QSize(16777215, 150))
        self.encabezadoHistorial.setStyleSheet(u"background-color: #F7E7DC;\n"
"border: 2px solid #DCBCA6;\n"
"border-radius: 10px\n"
"")
        self.horizontalLayout_9 = QHBoxLayout(self.encabezadoHistorial)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(9, -1, -1, -1)
        self.encabezado = QWidget(self.encabezadoHistorial)
        self.encabezado.setObjectName(u"encabezado")
        sizePolicy.setHeightForWidth(self.encabezado.sizePolicy().hasHeightForWidth())
        self.encabezado.setSizePolicy(sizePolicy)
        self.encabezado.setMinimumSize(QSize(250, 0))
        self.encabezado.setMaximumSize(QSize(250, 16777215))
        self.encabezado.setStyleSheet(u"border: 0px;")
        self.gridLayout_3 = QGridLayout(self.encabezado)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tituloHistorial = QLabel(self.encabezado)
        self.tituloHistorial.setObjectName(u"tituloHistorial")
        self.tituloHistorial.setFont(font2)
        self.tituloHistorial.setStyleSheet(u"color: rgb(125, 57, 40);")
        self.tituloHistorial.setWordWrap(True)

        self.gridLayout_3.addWidget(self.tituloHistorial, 0, 0, 1, 1)


        self.horizontalLayout_9.addWidget(self.encabezado)

        self.widgetLabels = QWidget(self.encabezadoHistorial)
        self.widgetLabels.setObjectName(u"widgetLabels")
        self.widgetLabels.setMaximumSize(QSize(100, 16777215))
        self.widgetLabels.setStyleSheet(u"border: 0px;")
        self.verticalLayout_19 = QVBoxLayout(self.widgetLabels)
        self.verticalLayout_19.setSpacing(6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(10, 0, 0, 0)
        self.lblClienteHist = QLabel(self.widgetLabels)
        self.lblClienteHist.setObjectName(u"lblClienteHist")
        self.lblClienteHist.setFont(font10)
        self.lblClienteHist.setStyleSheet(u"color: #7D3928;")

        self.verticalLayout_19.addWidget(self.lblClienteHist)

        self.lblServicioHist = QLabel(self.widgetLabels)
        self.lblServicioHist.setObjectName(u"lblServicioHist")
        self.lblServicioHist.setFont(font10)
        self.lblServicioHist.setStyleSheet(u"color: #7D3928;")

        self.verticalLayout_19.addWidget(self.lblServicioHist)


        self.horizontalLayout_9.addWidget(self.widgetLabels)

        self.widget_4 = QWidget(self.encabezadoHistorial)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"border: 0px;")
        self.verticalLayout_20 = QVBoxLayout(self.widget_4)
        self.verticalLayout_20.setSpacing(24)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, -1, 0)
        self.cmbClienteHist = QComboBox(self.widget_4)
        self.cmbClienteHist.setObjectName(u"cmbClienteHist")
        self.cmbClienteHist.setFont(font8)
        self.cmbClienteHist.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cmbClienteHist.setStyleSheet(u"QComboBox {\n"
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
        self.cmbClienteHist.setEditable(True)
        self.cmbClienteHist.setMaxVisibleItems(5)

        self.verticalLayout_20.addWidget(self.cmbClienteHist)

        self.cmbServicioHist = QComboBox(self.widget_4)
        self.cmbServicioHist.setObjectName(u"cmbServicioHist")
        self.cmbServicioHist.setFont(font8)
        self.cmbServicioHist.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cmbServicioHist.setStyleSheet(u"QComboBox {\n"
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
        self.cmbServicioHist.setMaxVisibleItems(5)

        self.verticalLayout_20.addWidget(self.cmbServicioHist)


        self.horizontalLayout_9.addWidget(self.widget_4)

        self.botoneraHist = QWidget(self.encabezadoHistorial)
        self.botoneraHist.setObjectName(u"botoneraHist")
        self.botoneraHist.setStyleSheet(u"border: 0px;")
        self.gridLayout_4 = QGridLayout(self.botoneraHist)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btnBuscarHist = QPushButton(self.botoneraHist)
        self.btnBuscarHist.setObjectName(u"btnBuscarHist")
        self.btnBuscarHist.setMinimumSize(QSize(0, 40))
        self.btnBuscarHist.setMaximumSize(QSize(150, 16777215))
        self.btnBuscarHist.setFont(font3)
        self.btnBuscarHist.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnBuscarHist.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_4.addWidget(self.btnBuscarHist, 0, 0, 1, 1)


        self.horizontalLayout_9.addWidget(self.botoneraHist)


        self.verticalLayout_18.addWidget(self.encabezadoHistorial)

        self.widgetTablaHist = QWidget(self.MenuHistorial)
        self.widgetTablaHist.setObjectName(u"widgetTablaHist")
        self.widgetTablaHist.setStyleSheet(u"border: 0px;")
        self.gridLayout_5 = QGridLayout(self.widgetTablaHist)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.tablaHistorial = QTableView(self.widgetTablaHist)
        self.tablaHistorial.setObjectName(u"tablaHistorial")
        self.tablaHistorial.setStyleSheet(u"\n"
"QTableView {\n"
"	border: 2px solid #DEC4AE;\n"
"	border-radius: 10px;\n"
"	color: rgb(125, 57, 40);\n"
"	font: 10pt \"Century Gothic\";\n"
"	gridline-color: rgb(125, 57, 40);\n"
"	selection-background-color: #D3B9B4;\n"
"	selection-color: rgb(0, 0, 0);\n"
"	background-color: #FDF5EE;\n"
"}\n"
"\n"
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
"	color: rgb(125, 57, 40);\n"
"}\n"
"")
        self.tablaHistorial.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tablaHistorial.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked)
        self.tablaHistorial.setAlternatingRowColors(True)
        self.tablaHistorial.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tablaHistorial.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tablaHistorial.horizontalHeader().setStretchLastSection(True)
        self.tablaHistorial.verticalHeader().setVisible(False)

        self.gridLayout_5.addWidget(self.tablaHistorial, 0, 0, 1, 1)


        self.verticalLayout_18.addWidget(self.widgetTablaHist)

        self.StackedWidget.addWidget(self.MenuHistorial)
        self.IntroPage = QWidget()
        self.IntroPage.setObjectName(u"IntroPage")
        self.IntroPage.setMinimumSize(QSize(0, 0))
        self.IntroPage.setMaximumSize(QSize(16777215, 16777215))
        self.IntroPage.setStyleSheet(u"background-color: rgb(249, 244, 244);")
        self.verticalLayout_13 = QVBoxLayout(self.IntroPage)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.imagenLogo = QWidget(self.IntroPage)
        self.imagenLogo.setObjectName(u"imagenLogo")
        sizePolicy.setHeightForWidth(self.imagenLogo.sizePolicy().hasHeightForWidth())
        self.imagenLogo.setSizePolicy(sizePolicy)
        self.imagenLogo.setSizeIncrement(QSize(0, 0))
        self.imagenLogo.setBaseSize(QSize(0, 0))
        self.imagenLogo.setAutoFillBackground(False)
        self.imagenLogo.setStyleSheet(u"image: url(:/images/images/logo_sin_fondo.png);\n"
"background-color: #F7E7DC;\n"
"\n"
"border: 2px solid #DCBCA6;\n"
"border-radius: 10px")

        self.verticalLayout_13.addWidget(self.imagenLogo)

        self.StackedWidget.addWidget(self.IntroPage)
        self.MenuClientes = QWidget()
        self.MenuClientes.setObjectName(u"MenuClientes")
        self.verticalLayout_5 = QVBoxLayout(self.MenuClientes)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(2, 0, 2, 0)
        self.encabezadoClientes = QWidget(self.MenuClientes)
        self.encabezadoClientes.setObjectName(u"encabezadoClientes")
        sizePolicy.setHeightForWidth(self.encabezadoClientes.sizePolicy().hasHeightForWidth())
        self.encabezadoClientes.setSizePolicy(sizePolicy)
        self.encabezadoClientes.setMinimumSize(QSize(0, 150))
        self.encabezadoClientes.setMaximumSize(QSize(16777215, 150))
        self.encabezadoClientes.setStyleSheet(u"background-color: #F7E7DC;\n"
"border: 2px solid #DCBCA6;\n"
"border-radius: 10px\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(self.encabezadoClientes)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.widgetTituloCliente = QWidget(self.encabezadoClientes)
        self.widgetTituloCliente.setObjectName(u"widgetTituloCliente")
        sizePolicy3.setHeightForWidth(self.widgetTituloCliente.sizePolicy().hasHeightForWidth())
        self.widgetTituloCliente.setSizePolicy(sizePolicy3)
        self.widgetTituloCliente.setMinimumSize(QSize(150, 0))
        self.widgetTituloCliente.setMaximumSize(QSize(200, 300))
        self.widgetTituloCliente.setStyleSheet(u"border: 0px")
        self.verticalLayout_7 = QVBoxLayout(self.widgetTituloCliente)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, -1, -1, -1)
        self.tituloClientes = QLabel(self.widgetTituloCliente)
        self.tituloClientes.setObjectName(u"tituloClientes")
        self.tituloClientes.setFont(font2)
        self.tituloClientes.setStyleSheet(u"color: rgb(125, 57, 40);")
        self.tituloClientes.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.tituloClientes.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.tituloClientes)


        self.horizontalLayout_2.addWidget(self.widgetTituloCliente)

        self.widgetAccionesCliente = QWidget(self.encabezadoClientes)
        self.widgetAccionesCliente.setObjectName(u"widgetAccionesCliente")
        self.widgetAccionesCliente.setStyleSheet(u"border: 0px")
        self.horizontalLayout_7 = QHBoxLayout(self.widgetAccionesCliente)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.widgetLineEdit = QWidget(self.widgetAccionesCliente)
        self.widgetLineEdit.setObjectName(u"widgetLineEdit")
        sizePolicy9.setHeightForWidth(self.widgetLineEdit.sizePolicy().hasHeightForWidth())
        self.widgetLineEdit.setSizePolicy(sizePolicy9)
        self.widgetLineEdit.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_10 = QVBoxLayout(self.widgetLineEdit)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.lineEditCliente = QLineEdit(self.widgetLineEdit)
        self.lineEditCliente.setObjectName(u"lineEditCliente")
        self.lineEditCliente.setMaximumSize(QSize(16777215, 30))
        self.lineEditCliente.setFont(font1)
        self.lineEditCliente.setStyleSheet(u"color: rgb(125, 57, 40);\n"
"border: 2px solid #C18484;\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"")

        self.verticalLayout_10.addWidget(self.lineEditCliente)


        self.horizontalLayout_7.addWidget(self.widgetLineEdit)

        self.widgetFiltrar = QWidget(self.widgetAccionesCliente)
        self.widgetFiltrar.setObjectName(u"widgetFiltrar")
        sizePolicy6.setHeightForWidth(self.widgetFiltrar.sizePolicy().hasHeightForWidth())
        self.widgetFiltrar.setSizePolicy(sizePolicy6)
        self.widgetFiltrar.setMinimumSize(QSize(200, 0))
        self.verticalLayout_11 = QVBoxLayout(self.widgetFiltrar)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, -1, -1, -1)
        self.btnFiltrarCliente = QPushButton(self.widgetFiltrar)
        self.btnFiltrarCliente.setObjectName(u"btnFiltrarCliente")
        sizePolicy3.setHeightForWidth(self.btnFiltrarCliente.sizePolicy().hasHeightForWidth())
        self.btnFiltrarCliente.setSizePolicy(sizePolicy3)
        self.btnFiltrarCliente.setMinimumSize(QSize(100, 30))
        self.btnFiltrarCliente.setFont(font1)
        self.btnFiltrarCliente.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnFiltrarCliente.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_11.addWidget(self.btnFiltrarCliente)


        self.horizontalLayout_7.addWidget(self.widgetFiltrar)

        self.botoneraCliente = QWidget(self.widgetAccionesCliente)
        self.botoneraCliente.setObjectName(u"botoneraCliente")
        self.botoneraCliente.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalLayout_12 = QVBoxLayout(self.botoneraCliente)
        self.verticalLayout_12.setSpacing(4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.btnNuevoCliente = QPushButton(self.botoneraCliente)
        self.btnNuevoCliente.setObjectName(u"btnNuevoCliente")
        sizePolicy3.setHeightForWidth(self.btnNuevoCliente.sizePolicy().hasHeightForWidth())
        self.btnNuevoCliente.setSizePolicy(sizePolicy3)
        self.btnNuevoCliente.setMinimumSize(QSize(150, 40))
        self.btnNuevoCliente.setMaximumSize(QSize(150, 40))
        self.btnNuevoCliente.setFont(font3)
        self.btnNuevoCliente.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnNuevoCliente.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_12.addWidget(self.btnNuevoCliente)

        self.btnEliminarCliente = QPushButton(self.botoneraCliente)
        self.btnEliminarCliente.setObjectName(u"btnEliminarCliente")
        self.btnEliminarCliente.setMinimumSize(QSize(150, 40))
        self.btnEliminarCliente.setMaximumSize(QSize(150, 40))
        self.btnEliminarCliente.setFont(font3)
        self.btnEliminarCliente.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnEliminarCliente.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_12.addWidget(self.btnEliminarCliente)


        self.horizontalLayout_7.addWidget(self.botoneraCliente)


        self.horizontalLayout_2.addWidget(self.widgetAccionesCliente)


        self.verticalLayout_5.addWidget(self.encabezadoClientes)

        self.widgetTabla = QWidget(self.MenuClientes)
        self.widgetTabla.setObjectName(u"widgetTabla")
        self.widgetTabla.setStyleSheet(u"border: 0px")
        self.gridLayout = QGridLayout(self.widgetTabla)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tablaClientes = QTableWidget(self.widgetTabla)
        self.tablaClientes.setObjectName(u"tablaClientes")
        self.tablaClientes.setStyleSheet(u"QTableWidget {\n"
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
"}")
        self.tablaClientes.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tablaClientes.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked)
        self.tablaClientes.setAlternatingRowColors(True)
        self.tablaClientes.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tablaClientes.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tablaClientes.horizontalHeader().setStretchLastSection(True)
        self.tablaClientes.verticalHeader().setVisible(False)

        self.gridLayout.addWidget(self.tablaClientes, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.widgetTabla)

        self.StackedWidget.addWidget(self.MenuClientes)

        self.verticalLayout_4.addWidget(self.StackedWidget)


        self.horizontalLayout.addWidget(self.MainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.StackedWidget.setCurrentIndex(7)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Turnero BLA", None))
        self.btnMenu.setText(QCoreApplication.translate("MainWindow", u"Men\u00fa", None))
        self.btnMenuProductos.setText(QCoreApplication.translate("MainWindow", u"Productos", None))
        self.btnMenuVentas.setText(QCoreApplication.translate("MainWindow", u"Ventas", None))
        self.btnMenuServicios.setText(QCoreApplication.translate("MainWindow", u"Servicios", None))
        self.btnMenuTurnos.setText(QCoreApplication.translate("MainWindow", u"Turnos", None))
        self.btnMenuClientes.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.btnMenuHistorial.setText(QCoreApplication.translate("MainWindow", u"Historial Clientes", None))
        self.btnMenuCCorriente.setText(QCoreApplication.translate("MainWindow", u"Cuentas Corrientes", None))
        self.tituloServicios.setText(QCoreApplication.translate("MainWindow", u"SERVICIOS DISPONIBLES", None))
        self.btnNuevoServicio.setText(QCoreApplication.translate("MainWindow", u"Nuevo Servicio", None))
        self.tituloTurnos.setText(QCoreApplication.translate("MainWindow", u"GESTI\u00d3N DE TURNOS", None))
        self.btnNuevoTurno.setText(QCoreApplication.translate("MainWindow", u"Nuevo Turno", None))
        self.btnVolverAVenta.setText(QCoreApplication.translate("MainWindow", u"Volver", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"CONSULTA DE VENTAS", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Desde", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Hasta", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.btnConsultarVenta.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.btnEliminarVenta.setText(QCoreApplication.translate("MainWindow", u"Eliminar venta", None))
        self.tituloNuevaVenta.setText(QCoreApplication.translate("MainWindow", u"NUEVA VENTA", None))
        self.btnConsultaVentas.setText(QCoreApplication.translate("MainWindow", u"Consulta de ventas", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.lblDescripProdVenta.setText(QCoreApplication.translate("MainWindow", u"Producto: ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Vencimiento:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Cantidad:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Precio unitario:", None))
        self.btnAgregarCarrito.setText(QCoreApplication.translate("MainWindow", u"Agregar al carrito", None))
        self.btnQuitarCarrito.setText(QCoreApplication.translate("MainWindow", u"Quitar del carrito", None))
        self.btnVaciarCarrito.setText(QCoreApplication.translate("MainWindow", u"Vaciar carrito", None))
        self.lblTotalEnCarrito.setText(QCoreApplication.translate("MainWindow", u"Total en carrito: $ 0.0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Datos de facturaci\u00f3n", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Modo pago", None))
        self.rbtnEfectivo.setText(QCoreApplication.translate("MainWindow", u"Efectivo", None))
        self.rbtnTransf.setText(QCoreApplication.translate("MainWindow", u"Transferencia", None))
        self.rbtnTarjeta.setText(QCoreApplication.translate("MainWindow", u"D\u00e9bito/Cr\u00e9dito", None))
        self.checkInteres.setText(QCoreApplication.translate("MainWindow", u"Interes ($)", None))
        self.lblTotalAbonar.setText(QCoreApplication.translate("MainWindow", u"Total a abonar: $ 0.0", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Entrega ($)", None))
        self.btnFinalizarVenta.setText(QCoreApplication.translate("MainWindow", u"Finalizar venta", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"CUENTAS CORRIENTES", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.cmbClienteCC.setPlaceholderText("")
        self.btnEliminarUltimaCC.setText(QCoreApplication.translate("MainWindow", u"Eliminar \u00faltimo registro", None))
        self.lblDeudaTotalCC.setText(QCoreApplication.translate("MainWindow", u"Deuda total: $ x", None))
        self.rbtnSaldarCC.setText(QCoreApplication.translate("MainWindow", u"Saldar deuda", None))
        self.rbtnActualizarCC.setText(QCoreApplication.translate("MainWindow", u"Actualizar deuda", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Monto ($)", None))
        self.btnCargarCC.setText(QCoreApplication.translate("MainWindow", u"Cargar", None))
        self.tituloProducto.setText(QCoreApplication.translate("MainWindow", u"PRODUCTOS", None))
        self.lblCodigo.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None))
        self.lblDescripcion.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n", None))
        self.btnFiltrarProductos.setText(QCoreApplication.translate("MainWindow", u"Filtrar", None))
        self.btnNuevoProducto.setText(QCoreApplication.translate("MainWindow", u"Nuevo Producto", None))
        self.btnEliminarProducto.setText(QCoreApplication.translate("MainWindow", u"Eliminar Producto", None))
        self.tituloHistorial.setText(QCoreApplication.translate("MainWindow", u"HISTORIAL DE TRATAMIENTOS", None))
        self.lblClienteHist.setText(QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.lblServicioHist.setText(QCoreApplication.translate("MainWindow", u"Servicio", None))
        self.btnBuscarHist.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.tituloClientes.setText(QCoreApplication.translate("MainWindow", u"GESTI\u00d3N DE CLIENTES", None))
        self.btnFiltrarCliente.setText(QCoreApplication.translate("MainWindow", u"Filtrar", None))
        self.btnNuevoCliente.setText(QCoreApplication.translate("MainWindow", u"Nuevo cliente", None))
        self.btnEliminarCliente.setText(QCoreApplication.translate("MainWindow", u"Eliminar Cliente", None))
    # retranslateUi

