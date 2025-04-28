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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCalendarWidget, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QStackedWidget, QTableView, QVBoxLayout,
    QWidget)
from view import recursos_rc

class VentanaPrincipal(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.WindowModal)
        MainWindow.resize(1100, 650)
        MainWindow.setMinimumSize(QSize(1100, 650))
        MainWindow.setMaximumSize(QSize(1100, 650))
        MainWindow.setStyleSheet(u"border-radius: 10px;")
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
        self.centralwidget.setStyleSheet(u"background-color: white;")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 0, 2)
        self.LeftMenu = QWidget(self.centralwidget)
        self.LeftMenu.setObjectName(u"LeftMenu")
        self.LeftMenu.setMinimumSize(QSize(200, 0))
        self.LeftMenu.setMaximumSize(QSize(200, 16777215))
        self.LeftMenu.setStyleSheet(u"background-color:  #C18484;\n"
"border-radius: 10px;")
        self.verticalLayout = QVBoxLayout(self.LeftMenu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.LogoNegocio = QWidget(self.LeftMenu)
        self.LogoNegocio.setObjectName(u"LogoNegocio")
        sizePolicy.setHeightForWidth(self.LogoNegocio.sizePolicy().hasHeightForWidth())
        self.LogoNegocio.setSizePolicy(sizePolicy)
        self.LogoNegocio.setMaximumSize(QSize(16777215, 200))
        self.LogoNegocio.setStyleSheet(u"image: url(:/images/images/logo_fondo.png);\n"
"")
        self.verticalLayout_14 = QVBoxLayout(self.LogoNegocio)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")

        self.verticalLayout.addWidget(self.LogoNegocio)

        self.MenuBotones = QWidget(self.LeftMenu)
        self.MenuBotones.setObjectName(u"MenuBotones")
        self.MenuBotones.setMaximumSize(QSize(16777215, 400))
        self.verticalLayout_2 = QVBoxLayout(self.MenuBotones)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.MenuBotones)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(22)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.label)

        self.btn_clientes = QPushButton(self.MenuBotones)
        self.btn_clientes.setObjectName(u"btn_clientes")
        self.btn_clientes.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setFamilies([u"Century Gothic"])
        font1.setPointSize(14)
        self.btn_clientes.setFont(font1)
        self.btn_clientes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_clientes.setStyleSheet(u"QPushButton {\n"
"	 color: rgb(255, 255, 255);;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	font-weight: bold;\n"
"	border-bottom: 2px solid;\n"
"	border-radius: 5px;\n"
"	border-color: rgb(255, 255, 255);\n"
"}")
        self.btn_clientes.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.btn_clientes)

        self.btn_servicios = QPushButton(self.MenuBotones)
        self.btn_servicios.setObjectName(u"btn_servicios")
        self.btn_servicios.setMaximumSize(QSize(16777215, 50))
        self.btn_servicios.setFont(font1)
        self.btn_servicios.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_servicios.setStyleSheet(u"QPushButton {\n"
"	 color: rgb(255, 255, 255);;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	font-weight: bold;\n"
"	border-bottom: 2px solid;\n"
"	border-radius: 5px;\n"
"	border-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_servicios)

        self.btn_turnos = QPushButton(self.MenuBotones)
        self.btn_turnos.setObjectName(u"btn_turnos")
        self.btn_turnos.setMaximumSize(QSize(16777215, 50))
        self.btn_turnos.setFont(font1)
        self.btn_turnos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_turnos.setStyleSheet(u"QPushButton {\n"
"	 color: rgb(255, 255, 255);;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	font-weight: bold;\n"
"	border-bottom: 2px solid;\n"
"	border-radius: 5px;\n"
"	border-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_turnos)


        self.verticalLayout.addWidget(self.MenuBotones)


        self.horizontalLayout.addWidget(self.LeftMenu)

        self.MainBody = QWidget(self.centralwidget)
        self.MainBody.setObjectName(u"MainBody")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.MainBody.sizePolicy().hasHeightForWidth())
        self.MainBody.setSizePolicy(sizePolicy1)
        self.MainBody.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.MainBody)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout_4.setContentsMargins(0, 0, 2, 0)
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
        self.encabezadoServicios.setMinimumSize(QSize(0, 150))
        self.encabezadoServicios.setMaximumSize(QSize(16777215, 150))
        self.encabezadoServicios.setStyleSheet(u"background-color:  #C18484;\n"
"border-radius: 10px;")
        self.horizontalLayout_3 = QHBoxLayout(self.encabezadoServicios)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 9, -1, -1)
        self.widgetTituloServicios = QWidget(self.encabezadoServicios)
        self.widgetTituloServicios.setObjectName(u"widgetTituloServicios")
        sizePolicy.setHeightForWidth(self.widgetTituloServicios.sizePolicy().hasHeightForWidth())
        self.widgetTituloServicios.setSizePolicy(sizePolicy)
        self.widgetTituloServicios.setMinimumSize(QSize(250, 0))
        self.widgetTituloServicios.setMaximumSize(QSize(200, 150))
        self.verticalLayout_17 = QVBoxLayout(self.widgetTituloServicios)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(9, 9, 9, 9)
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
        self.tituloServicios.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tituloServicios.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.tituloServicios)


        self.horizontalLayout_3.addWidget(self.widgetTituloServicios)

        self.widgetBotones = QWidget(self.encabezadoServicios)
        self.widgetBotones.setObjectName(u"widgetBotones")
        sizePolicy.setHeightForWidth(self.widgetBotones.sizePolicy().hasHeightForWidth())
        self.widgetBotones.setSizePolicy(sizePolicy)
        self.widgetBotones.setMinimumSize(QSize(400, 140))
        self.widgetBotones.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout_4 = QHBoxLayout(self.widgetBotones)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.espaciador = QWidget(self.widgetBotones)
        self.espaciador.setObjectName(u"espaciador")

        self.horizontalLayout_4.addWidget(self.espaciador)

        self.botoneraServicios = QWidget(self.widgetBotones)
        self.botoneraServicios.setObjectName(u"botoneraServicios")
        self.botoneraServicios.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.verticalLayout_15 = QVBoxLayout(self.botoneraServicios)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, 0, -1, 0)
        self.btnNuevoServicio = QPushButton(self.botoneraServicios)
        self.btnNuevoServicio.setObjectName(u"btnNuevoServicio")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnNuevoServicio.sizePolicy().hasHeightForWidth())
        self.btnNuevoServicio.setSizePolicy(sizePolicy2)
        self.btnNuevoServicio.setMaximumSize(QSize(150, 50))
        self.btnNuevoServicio.setFont(font1)
        self.btnNuevoServicio.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnNuevoServicio.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.btnNuevoServicio.setAutoFillBackground(False)
        self.btnNuevoServicio.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid;\n"
"	border-radius: 5px;\n"
"	border-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	font-weight: bold;\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid;\n"
"	border-radius: 5px;\n"
"	border-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_15.addWidget(self.btnNuevoServicio)


        self.horizontalLayout_4.addWidget(self.botoneraServicios)


        self.horizontalLayout_3.addWidget(self.widgetBotones)


        self.verticalLayout_6.addWidget(self.encabezadoServicios)

        self.scrollAreaServicio = QScrollArea(self.MenuServicios)
        self.scrollAreaServicio.setObjectName(u"scrollAreaServicio")
        self.scrollAreaServicio.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollAreaServicio.setWidgetResizable(True)
        self.scrollAreaServicio.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.contenedorServicios = QWidget()
        self.contenedorServicios.setObjectName(u"contenedorServicios")
        self.contenedorServicios.setGeometry(QRect(0, 0, 84, 16))
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
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.encabezadoTurnos.sizePolicy().hasHeightForWidth())
        self.encabezadoTurnos.setSizePolicy(sizePolicy3)
        self.encabezadoTurnos.setMaximumSize(QSize(16777215, 170))
        self.encabezadoTurnos.setStyleSheet(u"background-color:  #C18484;\n"
"border-radius: 10px;")
        self.horizontalLayout_5 = QHBoxLayout(self.encabezadoTurnos)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.contenedorTitulo = QWidget(self.encabezadoTurnos)
        self.contenedorTitulo.setObjectName(u"contenedorTitulo")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.contenedorTitulo.sizePolicy().hasHeightForWidth())
        self.contenedorTitulo.setSizePolicy(sizePolicy4)
        self.contenedorTitulo.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_6 = QHBoxLayout(self.contenedorTitulo)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tituloTurnos = QLabel(self.contenedorTitulo)
        self.tituloTurnos.setObjectName(u"tituloTurnos")
        self.tituloTurnos.setFont(font2)
        self.tituloTurnos.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tituloTurnos.setWordWrap(True)

        self.horizontalLayout_6.addWidget(self.tituloTurnos)


        self.horizontalLayout_5.addWidget(self.contenedorTitulo)

        self.contenedorCalendario = QWidget(self.encabezadoTurnos)
        self.contenedorCalendario.setObjectName(u"contenedorCalendario")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.contenedorCalendario.sizePolicy().hasHeightForWidth())
        self.contenedorCalendario.setSizePolicy(sizePolicy5)
        self.contenedorCalendario.setMaximumSize(QSize(400, 16777215))
        self.horizontalLayout_8 = QHBoxLayout(self.contenedorCalendario)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 2, 0, 2)
        self.calendarWidget = QCalendarWidget(self.contenedorCalendario)
        self.calendarWidget.setObjectName(u"calendarWidget")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy6)
        self.calendarWidget.setMinimumSize(QSize(0, 149))
        font3 = QFont()
        font3.setFamilies([u"Century Gothic"])
        font3.setPointSize(10)
        self.calendarWidget.setFont(font3)
        self.calendarWidget.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.calendarWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.calendarWidget.setStyleSheet(u"")
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
        sizePolicy4.setHeightForWidth(self.botoneraTurnos.sizePolicy().hasHeightForWidth())
        self.botoneraTurnos.setSizePolicy(sizePolicy4)
        self.botoneraTurnos.setMaximumSize(QSize(200, 19999))
        self.botoneraTurnos.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.verticalLayout_9 = QVBoxLayout(self.botoneraTurnos)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.btnNuevoTurno = QPushButton(self.botoneraTurnos)
        self.btnNuevoTurno.setObjectName(u"btnNuevoTurno")
        sizePolicy2.setHeightForWidth(self.btnNuevoTurno.sizePolicy().hasHeightForWidth())
        self.btnNuevoTurno.setSizePolicy(sizePolicy2)
        self.btnNuevoTurno.setMaximumSize(QSize(150, 50))
        self.btnNuevoTurno.setFont(font1)
        self.btnNuevoTurno.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnNuevoTurno.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.btnNuevoTurno.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid;\n"
"	border-radius: 5px;\n"
"	border-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	font-weight: bold;\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid;\n"
"	border-radius: 5px;\n"
"	border-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_9.addWidget(self.btnNuevoTurno)


        self.horizontalLayout_5.addWidget(self.botoneraTurnos)


        self.verticalLayout_8.addWidget(self.encabezadoTurnos)

        self.scrollAreaTurnos = QScrollArea(self.MenuTurnos)
        self.scrollAreaTurnos.setObjectName(u"scrollAreaTurnos")
        self.scrollAreaTurnos.setWidgetResizable(True)
        self.contenedorTurnos = QWidget()
        self.contenedorTurnos.setObjectName(u"contenedorTurnos")
        self.contenedorTurnos.setGeometry(QRect(0, 0, 100, 30))
        self.verticalLayout_16 = QVBoxLayout(self.contenedorTurnos)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.scrollAreaTurnos.setWidget(self.contenedorTurnos)

        self.verticalLayout_8.addWidget(self.scrollAreaTurnos)

        self.StackedWidget.addWidget(self.MenuTurnos)
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
        self.imagenLogo.setStyleSheet(u"image: url(:/images/images/logo_fondo.png);\n"
"border: 2px solid #C18484;\n"
"border-radius: 5px;")

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
        self.encabezadoClientes.setStyleSheet(u"background-color: #C18484;\n"
"border-radius: 10px;")
        self.horizontalLayout_2 = QHBoxLayout(self.encabezadoClientes)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widgetTituloCliente = QWidget(self.encabezadoClientes)
        self.widgetTituloCliente.setObjectName(u"widgetTituloCliente")
        sizePolicy2.setHeightForWidth(self.widgetTituloCliente.sizePolicy().hasHeightForWidth())
        self.widgetTituloCliente.setSizePolicy(sizePolicy2)
        self.widgetTituloCliente.setMinimumSize(QSize(150, 0))
        self.widgetTituloCliente.setMaximumSize(QSize(200, 300))
        self.verticalLayout_7 = QVBoxLayout(self.widgetTituloCliente)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tituloClientes = QLabel(self.widgetTituloCliente)
        self.tituloClientes.setObjectName(u"tituloClientes")
        self.tituloClientes.setFont(font2)
        self.tituloClientes.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tituloClientes.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.tituloClientes)


        self.horizontalLayout_2.addWidget(self.widgetTituloCliente)

        self.widgetAccionesCliente = QWidget(self.encabezadoClientes)
        self.widgetAccionesCliente.setObjectName(u"widgetAccionesCliente")
        self.horizontalLayout_7 = QHBoxLayout(self.widgetAccionesCliente)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.widgetLineEdit = QWidget(self.widgetAccionesCliente)
        self.widgetLineEdit.setObjectName(u"widgetLineEdit")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.widgetLineEdit.sizePolicy().hasHeightForWidth())
        self.widgetLineEdit.setSizePolicy(sizePolicy7)
        self.widgetLineEdit.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_10 = QVBoxLayout(self.widgetLineEdit)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.lineEditCliente = QLineEdit(self.widgetLineEdit)
        self.lineEditCliente.setObjectName(u"lineEditCliente")
        self.lineEditCliente.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setFamilies([u"Century Gothic"])
        font4.setPointSize(12)
        self.lineEditCliente.setFont(font4)
        self.lineEditCliente.setStyleSheet(u"color: black;\n"
"background-color: white;\n"
"border-radius: 5px;")

        self.verticalLayout_10.addWidget(self.lineEditCliente)


        self.horizontalLayout_7.addWidget(self.widgetLineEdit)

        self.widgetFiltrar = QWidget(self.widgetAccionesCliente)
        self.widgetFiltrar.setObjectName(u"widgetFiltrar")
        sizePolicy5.setHeightForWidth(self.widgetFiltrar.sizePolicy().hasHeightForWidth())
        self.widgetFiltrar.setSizePolicy(sizePolicy5)
        self.widgetFiltrar.setMinimumSize(QSize(120, 0))
        self.verticalLayout_11 = QVBoxLayout(self.widgetFiltrar)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.btnFiltrarCliente = QPushButton(self.widgetFiltrar)
        self.btnFiltrarCliente.setObjectName(u"btnFiltrarCliente")
        sizePolicy2.setHeightForWidth(self.btnFiltrarCliente.sizePolicy().hasHeightForWidth())
        self.btnFiltrarCliente.setSizePolicy(sizePolicy2)
        self.btnFiltrarCliente.setMinimumSize(QSize(100, 30))
        self.btnFiltrarCliente.setFont(font4)
        self.btnFiltrarCliente.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnFiltrarCliente.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid;\n"
"	border-radius: 5px;\n"
"	border-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	font-weight: bold;\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid;\n"
"	border-radius: 5px;\n"
"	border-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_11.addWidget(self.btnFiltrarCliente)


        self.horizontalLayout_7.addWidget(self.widgetFiltrar)

        self.botoneraCliente = QWidget(self.widgetAccionesCliente)
        self.botoneraCliente.setObjectName(u"botoneraCliente")
        self.botoneraCliente.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.verticalLayout_12 = QVBoxLayout(self.botoneraCliente)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.btnNuevoCliente = QPushButton(self.botoneraCliente)
        self.btnNuevoCliente.setObjectName(u"btnNuevoCliente")
        sizePolicy2.setHeightForWidth(self.btnNuevoCliente.sizePolicy().hasHeightForWidth())
        self.btnNuevoCliente.setSizePolicy(sizePolicy2)
        self.btnNuevoCliente.setMinimumSize(QSize(150, 40))
        self.btnNuevoCliente.setMaximumSize(QSize(150, 40))
        self.btnNuevoCliente.setFont(font1)
        self.btnNuevoCliente.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnNuevoCliente.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid;\n"
"	border-radius: 5px;\n"
"	border-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	font-weight: bold;\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid;\n"
"	border-radius: 5px;\n"
"	border-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_12.addWidget(self.btnNuevoCliente)

        self.btnEliminarCliente = QPushButton(self.botoneraCliente)
        self.btnEliminarCliente.setObjectName(u"btnEliminarCliente")
        self.btnEliminarCliente.setMinimumSize(QSize(150, 40))
        self.btnEliminarCliente.setMaximumSize(QSize(150, 40))
        self.btnEliminarCliente.setFont(font1)
        self.btnEliminarCliente.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnEliminarCliente.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid;\n"
"	border-radius: 5px;\n"
"	border-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	font-weight: bold;\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid;\n"
"	border-radius: 5px;\n"
"	border-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_12.addWidget(self.btnEliminarCliente)


        self.horizontalLayout_7.addWidget(self.botoneraCliente)


        self.horizontalLayout_2.addWidget(self.widgetAccionesCliente)


        self.verticalLayout_5.addWidget(self.encabezadoClientes)

        self.widgetTabla = QWidget(self.MenuClientes)
        self.widgetTabla.setObjectName(u"widgetTabla")
        self.widgetTabla.setStyleSheet(u"background-color: rgb(249, 244, 244);")
        self.gridLayout = QGridLayout(self.widgetTabla)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tablaClientes = QTableView(self.widgetTabla)
        self.tablaClientes.setObjectName(u"tablaClientes")
        font5 = QFont()
        font5.setFamilies([u"century-gothic"])
        font5.setPointSize(12)
        self.tablaClientes.setFont(font5)
        self.tablaClientes.setStyleSheet(u"QHeaderView::section {\n"
"	color: #C18484;\n"
"	background-color: #EDE2E0;\n"
"	font-weight: bold;\n"
"	font-family: century-gothic;\n"
"	font-size: 12pt;\n"
"	padding: 5px;\n"
"	gridline-color: #C18484;\n"
"}\n"
"\n"
"QTableView {\n"
"	color: black;\n"
"	font-family: century-gothic;\n"
"	font-size: 12pt;\n"
"	gridline-color: #C18484;\n"
"	selection-background-color: #D3B9B4;\n"
"	selection-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	color: black\n"
"}")
        self.tablaClientes.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tablaClientes.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked)
        self.tablaClientes.setAlternatingRowColors(True)
        self.tablaClientes.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tablaClientes.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tablaClientes.setShowGrid(True)
        self.tablaClientes.setCornerButtonEnabled(False)

        self.gridLayout.addWidget(self.tablaClientes, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.widgetTabla)

        self.StackedWidget.addWidget(self.MenuClientes)

        self.verticalLayout_4.addWidget(self.StackedWidget)


        self.horizontalLayout.addWidget(self.MainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.StackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Turnero BLA", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Men\u00fa", None))
        self.btn_clientes.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.btn_servicios.setText(QCoreApplication.translate("MainWindow", u"Servicios", None))
        self.btn_turnos.setText(QCoreApplication.translate("MainWindow", u"Turnos", None))
        self.tituloServicios.setText(QCoreApplication.translate("MainWindow", u"SERVICIOS DISPONIBLES", None))
        self.btnNuevoServicio.setText(QCoreApplication.translate("MainWindow", u"Nuevo Servicio", None))
        self.tituloTurnos.setText(QCoreApplication.translate("MainWindow", u"GESTI\u00d3N DE TURNOS", None))
        self.btnNuevoTurno.setText(QCoreApplication.translate("MainWindow", u"Nuevo Turno", None))
        self.tituloClientes.setText(QCoreApplication.translate("MainWindow", u"GESTI\u00d3N DE CLIENTES", None))
        self.btnFiltrarCliente.setText(QCoreApplication.translate("MainWindow", u"Filtrar", None))
        self.btnNuevoCliente.setText(QCoreApplication.translate("MainWindow", u"Nuevo cliente", None))
        self.btnEliminarCliente.setText(QCoreApplication.translate("MainWindow", u"Eliminar Cliente", None))
    # retranslateUi

