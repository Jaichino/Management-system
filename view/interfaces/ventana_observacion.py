# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_observacion.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QPlainTextEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class VentanaObservacion(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(430, 320)
        Dialog.setMinimumSize(QSize(430, 320))
        Dialog.setMaximumSize(QSize(430, 320))
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.cuerpoDialog = QWidget(Dialog)
        self.cuerpoDialog.setObjectName(u"cuerpoDialog")
        self.cuerpoDialog.setStyleSheet(u"\n"
"\n"
"background-color: #F7E7DC;\n"
"border: 2px solid #DCBCA6;\n"
"border-radius: 10px\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.cuerpoDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(self.cuerpoDialog)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 50))
        self.widget_2.setMaximumSize(QSize(16777215, 50))
        self.widget_2.setStyleSheet(u"border: 0")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(4, 4, 0, -1)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #7D3928")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.cuerpoDialog)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 200))
        self.gridLayout_3 = QGridLayout(self.widget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.editObservacion = QPlainTextEdit(self.widget_3)
        self.editObservacion.setObjectName(u"editObservacion")
        self.editObservacion.setStyleSheet(u"color: rgb(125, 57, 40);\n"
"border: 2px solid #C18484;\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"")
        self.editObservacion.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.gridLayout_3.addWidget(self.editObservacion, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.cuerpoDialog)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 40))
        self.widget_4.setStyleSheet(u"border:0px")
        self.gridLayout_4 = QGridLayout(self.widget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btnGuardarObs = QPushButton(self.widget_4)
        self.btnGuardarObs.setObjectName(u"btnGuardarObs")
        self.btnGuardarObs.setMinimumSize(QSize(100, 30))
        self.btnGuardarObs.setMaximumSize(QSize(100, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Century Gothic"])
        font1.setPointSize(12)
        self.btnGuardarObs.setFont(font1)
        self.btnGuardarObs.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_4.addWidget(self.btnGuardarObs, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_4)


        self.gridLayout.addWidget(self.cuerpoDialog, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"BLA - Observaci\u00f3n de tratamiento", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Observaci\u00f3n del tratamiento", None))
        self.btnGuardarObs.setText(QCoreApplication.translate("Dialog", u"Guardar", None))
    # retranslateUi

