# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QGroupBox,
    QPushButton,
    QRadioButton,
    QSizePolicy,
    QSplitter,
    QVBoxLayout,
    QWidget,
)


class Ui_View(object):
    def setupUi(self, View):
        if not View.objectName():
            View.setObjectName('View')
        View.resize(934, 520)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(View.sizePolicy().hasHeightForWidth())
        View.setSizePolicy(sizePolicy)
        View.setMinimumSize(QSize(934, 520))
        View.setMaximumSize(QSize(934, 520))
        View.setStyleSheet('')
        self.splitter_2 = QSplitter(View)
        self.splitter_2.setObjectName('splitter_2')
        self.splitter_2.setGeometry(QRect(9, 9, 840, 500))
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy1)
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.left_aside = QWidget(self.splitter_2)
        self.left_aside.setObjectName('left_aside')
        sizePolicy.setHeightForWidth(self.left_aside.sizePolicy().hasHeightForWidth())
        self.left_aside.setSizePolicy(sizePolicy)
        self.left_aside.setMinimumSize(QSize(500, 500))
        self.left_aside.setMaximumSize(QSize(500, 500))
        self.left_aside.setStyleSheet(
            'QWidget#left_aside {\n' '	background-color: rgb(0, 0, 0);\n' '}'
        )
        self.splitter_2.addWidget(self.left_aside)
        self.groupBox = QGroupBox(self.splitter_2)
        self.groupBox.setObjectName('groupBox')
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )
        sizePolicy2.setHorizontalStretch(40)
        sizePolicy2.setVerticalStretch(40)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName('verticalLayout')
        self.splitter = QSplitter(self.groupBox)
        self.splitter.setObjectName('splitter')
        self.splitter.setOrientation(Qt.Horizontal)
        self.maze_radio_button = QRadioButton(self.splitter)
        self.maze_radio_button.setObjectName('maze_radio_button')
        self.splitter.addWidget(self.maze_radio_button)
        self.cava_radio_button = QRadioButton(self.splitter)
        self.cava_radio_button.setObjectName('cava_radio_button')
        self.splitter.addWidget(self.cava_radio_button)

        self.verticalLayout.addWidget(self.splitter)

        self.load_button = QPushButton(self.groupBox)
        self.load_button.setObjectName('load_button')
        sizePolicy3 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.load_button.sizePolicy().hasHeightForWidth())
        self.load_button.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.load_button)

        self.splitter_2.addWidget(self.groupBox)

        self.retranslateUi(View)

        QMetaObject.connectSlotsByName(View)

    # setupUi

    def retranslateUi(self, View):
        View.setWindowTitle(QCoreApplication.translate('View', 'View', None))
        self.groupBox.setTitle('')
        self.maze_radio_button.setText(
            QCoreApplication.translate('View', 'RadioButton', None)
        )
        self.cava_radio_button.setText(
            QCoreApplication.translate('View', 'RadioButton', None)
        )
        self.load_button.setText(QCoreApplication.translate('View', 'Load', None))

    # retranslateUi
