import json
import os.path
from zipfile import ZipFile

from PyQt6.QtGui import QShortcut, QKeySequence

from dutchtaxadministrator.classes.Administration import Administration, administration_from_json
from dutchtaxadministrator.classes.AdministrationManager import AdministrationManager
from dutchtaxadministrator.gui.add_administration_dialog import AddAdministrationDialog
from dutchtaxadministrator.gui.gui_files.main_window_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QFileDialog, QMessageBox

from dutchtaxadministrator.models.income_table_model import IncomeTableModel


class DutchTaxAdministrator(QMainWindow):
    """Create the main window that stores all of the widgets necessary for the application."""
    administration_manager: AdministrationManager
    def __init__(self, parent=None):
        """Initialize the components of the main window."""
        super(DutchTaxAdministrator, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('DutchTaxAdministrator')
        self.administration_manager = AdministrationManager()
        self.save_shortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        self.load_shortcut = QShortcut(QKeySequence("Ctrl+O"), self)


        self.income_model = IncomeTableModel()
        self.ui.income_table_view.setModel(self.income_model)
        self.ui.income_table_view.set_delegates()
        self.connect_signals()

    def connect_signals(self):
        """
        Connects signals
        """
        self.ui.new_adminitration_action.triggered.connect(self._show_add_administration_dialog)
        self.ui.administration_save_action.triggered.connect(self.administration_manager.save_administration)
        self.load_shortcut.activated.connect(self.load_administration)
        self.ui.administration_open_action.triggered.connect(self.load_administration)
        self.save_shortcut.activated.connect(self.administration_manager.save_administration)
        self.income_model.incomes_changed.connect(self.administration_manager.update_administration_incomes)
        self.administration_manager.administration_changed.connect(self._configure_administration)
        self.ui.add_income_button.clicked.connect(self.income_model.add_empty_income)
    def _show_add_administration_dialog(self):
        """
        Shows add administration dialog
        """
        dialog = AddAdministrationDialog()
        dialog.created_administration.connect(self.administration_manager.new_administration)
        dialog.exec()

    def _configure_administration(self):
        """
        Configures main window with the given administration

        Args:
            administration (Administration): Administration to configure
        """
        self.ui.current_administration_value_label.setText(
            f"{self.administration_manager.administration.name} "
            f"({self.administration_manager.administration.year})")
        self.ui.overview_tab_widget.setCurrentIndex(0)
        self.income_model.incomes = self.administration_manager.administration.incomes
        self.income_model.layoutChanged.emit()

    def load_administration(self):
        """
        Loads an administration from an existing file chosen by the user.
        """
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Json Files (*.json);;All Files (*)")

        if file_name:
            try:
                # Read the JSON file and parse it into a dictionary
                with open(file_name, 'r') as json_file:
                    data = json.load(json_file)
                    self.administration_manager.load_administration_from_json(data)
            except Exception as e:
                # Handle any errors that occur during file opening or parsing
                QMessageBox.critical(self, "Error", f"Failed to open or parse the file:\n{e}")


    def closeEvent(self, event):
        """
        Overrides the close event to show a dialog asking if the user saved their work.
        """
        reply = QMessageBox.question(
            self,
            'File not saved',
            'You have not saved this file before, do you want to do so?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Cancel,
            QMessageBox.StandardButton.Cancel
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.administration_manager.save_administration()

        if reply == QMessageBox.StandardButton.Cancel:
            event.ignore()

        event.accept()
