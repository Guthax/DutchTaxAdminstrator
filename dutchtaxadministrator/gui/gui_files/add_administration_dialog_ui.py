# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_administration.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QLabel, QLineEdit, QSizePolicy,
    QSpinBox, QWidget)

class Ui_add_administration_dialog(object):
    def setupUi(self, add_administration_dialog):
        if not add_administration_dialog.objectName():
            add_administration_dialog.setObjectName(u"add_administration_dialog")
        add_administration_dialog.resize(400, 300)
        self.formLayout_2 = QFormLayout(add_administration_dialog)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.name_label = QLabel(add_administration_dialog)
        self.name_label.setObjectName(u"name_label")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.name_label)

        self.year_label = QLabel(add_administration_dialog)
        self.year_label.setObjectName(u"year_label")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.year_label)

        self.name_line_edit = QLineEdit(add_administration_dialog)
        self.name_line_edit.setObjectName(u"name_line_edit")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.name_line_edit)

        self.year_spin_box = QSpinBox(add_administration_dialog)
        self.year_spin_box.setObjectName(u"year_spin_box")
        self.year_spin_box.setMinimum(2010)
        self.year_spin_box.setMaximum(2025)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.year_spin_box)

        self.button_box = QDialogButtonBox(add_administration_dialog)
        self.button_box.setObjectName(u"button_box")
        self.button_box.setOrientation(Qt.Orientation.Horizontal)
        self.button_box.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.button_box)


        self.retranslateUi(add_administration_dialog)
        self.button_box.accepted.connect(add_administration_dialog.accept)
        self.button_box.rejected.connect(add_administration_dialog.reject)

        QMetaObject.connectSlotsByName(add_administration_dialog)
    # setupUi

    def retranslateUi(self, add_administration_dialog):
        add_administration_dialog.setWindowTitle(QCoreApplication.translate("add_administration_dialog", u"Add new administration", None))
        self.name_label.setText(QCoreApplication.translate("add_administration_dialog", u"Name", None))
        self.year_label.setText(QCoreApplication.translate("add_administration_dialog", u"Year", None))
    # retranslateUi

