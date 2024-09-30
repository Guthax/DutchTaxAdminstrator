# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PyQt6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

from dutchtaxadministrator.gui.widgets.income_table import IncomeTable

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1400, 632)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.new_adminitration_action = QAction(MainWindow)
        self.new_adminitration_action.setObjectName(u"new_adminitration_action")
        self.administration_open_action = QAction(MainWindow)
        self.administration_open_action.setObjectName(u"administration_open_action")
        self.administration_save_action = QAction(MainWindow)
        self.administration_save_action.setObjectName(u"administration_save_action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.current_administration_label = QLabel(self.centralwidget)
        self.current_administration_label.setObjectName(u"current_administration_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.current_administration_label.sizePolicy().hasHeightForWidth())
        self.current_administration_label.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.current_administration_label)

        self.current_administration_value_label = QLabel(self.centralwidget)
        self.current_administration_value_label.setObjectName(u"current_administration_value_label")
        sizePolicy1.setHeightForWidth(self.current_administration_value_label.sizePolicy().hasHeightForWidth())
        self.current_administration_value_label.setSizePolicy(sizePolicy1)
        self.current_administration_value_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.current_administration_value_label)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.overview_tab_widget = QTabWidget(self.centralwidget)
        self.overview_tab_widget.setObjectName(u"overview_tab_widget")
        sizePolicy1.setHeightForWidth(self.overview_tab_widget.sizePolicy().hasHeightForWidth())
        self.overview_tab_widget.setSizePolicy(sizePolicy1)
        self.income_tab = QWidget()
        self.income_tab.setObjectName(u"income_tab")
        sizePolicy1.setHeightForWidth(self.income_tab.sizePolicy().hasHeightForWidth())
        self.income_tab.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.income_tab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.add_income_button = QPushButton(self.income_tab)
        self.add_income_button.setObjectName(u"add_income_button")

        self.verticalLayout_3.addWidget(self.add_income_button)

        self.income_table = IncomeTable()
        self.income_table.setObjectName(u"income_table")

        self.verticalLayout_3.addWidget(self.income_table)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.overview_tab_widget.addTab(self.income_tab, "")
        self.expense_tab = QWidget()
        self.expense_tab.setObjectName(u"expense_tab")
        sizePolicy1.setHeightForWidth(self.expense_tab.sizePolicy().hasHeightForWidth())
        self.expense_tab.setSizePolicy(sizePolicy1)
        self.overview_tab_widget.addTab(self.expense_tab, "")
        self.quarter_overview_tab = QWidget()
        self.quarter_overview_tab.setObjectName(u"quarter_overview_tab")
        sizePolicy1.setHeightForWidth(self.quarter_overview_tab.sizePolicy().hasHeightForWidth())
        self.quarter_overview_tab.setSizePolicy(sizePolicy1)
        self.overview_tab_widget.addTab(self.quarter_overview_tab, "")
        self.year_overview_tab = QWidget()
        self.year_overview_tab.setObjectName(u"year_overview_tab")
        sizePolicy1.setHeightForWidth(self.year_overview_tab.sizePolicy().hasHeightForWidth())
        self.year_overview_tab.setSizePolicy(sizePolicy1)
        self.overview_tab_widget.addTab(self.year_overview_tab, "")

        self.verticalLayout_2.addWidget(self.overview_tab_widget)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 9)

        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1400, 23))
        self.menuAdministration = QMenu(self.menubar)
        self.menuAdministration.setObjectName(u"menuAdministration")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAdministration.menuAction())
        self.menuAdministration.addAction(self.new_adminitration_action)
        self.menuAdministration.addAction(self.administration_open_action)
        self.menuAdministration.addAction(self.administration_save_action)

        self.retranslateUi(MainWindow)

        self.overview_tab_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.new_adminitration_action.setText(QCoreApplication.translate("MainWindow", u"New Administration", None))
        self.administration_open_action.setText(QCoreApplication.translate("MainWindow", u"Open Administration", None))
        self.administration_save_action.setText(QCoreApplication.translate("MainWindow", u"Save Administration", None))
        self.current_administration_label.setText(QCoreApplication.translate("MainWindow", u"Current Administration", None))
        self.current_administration_value_label.setText(QCoreApplication.translate("MainWindow", u"test", None))
        self.add_income_button.setText(QCoreApplication.translate("MainWindow", u"Add Income", None))
        self.overview_tab_widget.setTabText(self.overview_tab_widget.indexOf(self.income_tab), QCoreApplication.translate("MainWindow", u"Income", None))
        self.overview_tab_widget.setTabText(self.overview_tab_widget.indexOf(self.expense_tab), QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.overview_tab_widget.setTabText(self.overview_tab_widget.indexOf(self.quarter_overview_tab), QCoreApplication.translate("MainWindow", u"Quarter Overview", None))
        self.overview_tab_widget.setTabText(self.overview_tab_widget.indexOf(self.year_overview_tab), QCoreApplication.translate("MainWindow", u"Yearly Overview", None))
        self.menuAdministration.setTitle(QCoreApplication.translate("MainWindow", u"Administration", None))
    # retranslateUi

