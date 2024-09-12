# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_View(object):
    def setupUi(self, View):
        if not View.objectName():
            View.setObjectName(u"View")
        View.resize(520, 578)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(View.sizePolicy().hasHeightForWidth())
        View.setSizePolicy(sizePolicy)
        View.setMinimumSize(QSize(520, 578))
        View.setMaximumSize(QSize(520, 578))
        View.setStyleSheet(u"QWidget#View {\n"
"	background-color: #222324;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #222324;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"QFrame {\n"
"	background-color: #222324;\n"
"}\n"
"")
        self.verticalLayout_3 = QVBoxLayout(View)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.main_frame = QFrame(View)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setMinimumSize(QSize(500, 500))
        self.main_frame.setMaximumSize(QSize(500, 500))
        self.main_frame.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.main_frame)

        self.frame = QFrame(View)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.download_button = QPushButton(self.frame)
        self.download_button.setObjectName(u"download_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.download_button.sizePolicy().hasHeightForWidth())
        self.download_button.setSizePolicy(sizePolicy1)
        self.download_button.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.download_button)

        self.generate_button = QPushButton(self.frame)
        self.generate_button.setObjectName(u"generate_button")
        sizePolicy1.setHeightForWidth(self.generate_button.sizePolicy().hasHeightForWidth())
        self.generate_button.setSizePolicy(sizePolicy1)
        self.generate_button.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.generate_button)

        self.upload_button = QPushButton(self.frame)
        self.upload_button.setObjectName(u"upload_button")
        sizePolicy1.setHeightForWidth(self.upload_button.sizePolicy().hasHeightForWidth())
        self.upload_button.setSizePolicy(sizePolicy1)
        self.upload_button.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.upload_button)


        self.verticalLayout_3.addWidget(self.frame)


        self.retranslateUi(View)

        QMetaObject.connectSlotsByName(View)
    # setupUi

    def retranslateUi(self, View):
        View.setWindowTitle(QCoreApplication.translate("View", u"View", None))
        self.download_button.setText(QCoreApplication.translate("View", u"Downoad", None))
        self.generate_button.setText(QCoreApplication.translate("View", u"Generate", None))
        self.upload_button.setText(QCoreApplication.translate("View", u"Upload", None))
    # retranslateUi

