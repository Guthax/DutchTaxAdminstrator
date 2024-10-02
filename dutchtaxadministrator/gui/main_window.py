import json
import os.path
from zipfile import ZipFile

from PyQt6.QtGui import QShortcut, QKeySequence

from dutchtaxadministrator.classes.Administration import Administration, administration_from_json
from dutchtaxadministrator.gui.add_administration_dialog import AddAdministrationDialog
from dutchtaxadministrator.gui.gui_files.main_window_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QFileDialog, QMessageBox


class DutchTaxAdministrator(QMainWindow):
    """Create the main window that stores all of the widgets necessary for the application."""
    current_administration: Administration
    def __init__(self, parent=None):
        """Initialize the components of the main window."""
        super(DutchTaxAdministrator, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('DutchTaxAdministrator')
        self.current_administration = Administration("Template")
        self.save_shortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        self.load_shortcut = QShortcut(QKeySequence("Ctrl+O"), self)

        self.connect_signals()

    def connect_signals(self):
        """
        Connects signals
        """
        self.ui.new_adminitration_action.triggered.connect(self._show_add_administration_dialog)
        self.ui.administration_save_action.triggered.connect(self.save_administration)
        self.ui.add_income_button.clicked.connect(self.ui.income_table.add_blank_row)
        self.load_shortcut.activated.connect(self.load_administration)
        self.ui.administration_open_action.triggered.connect(self.load_administration)
        self.save_shortcut.activated.connect(self.save_administration)

    def _show_add_administration_dialog(self):
        """
        Shows add administration dialog
        """
        dialog = AddAdministrationDialog()
        dialog.created_administration.connect(self._configure_administration)
        dialog.exec()

    def _configure_administration(self, administration: Administration):
        """
        Configures main window with the given administration

        Args:
            administration (Administration): Administration to configure
        """
        self.current_administration = administration

        if not os.path.exists(self.current_administration.save_location):
            os.mkdir(self.current_administration.save_location)


        self.ui.current_administration_value_label.setText(
            f"{self.current_administration.name} "
            f"({self.current_administration.year})")
        self.ui.overview_tab_widget.setCurrentIndex(0)
        self.ui.income_table.fill_table_from_income_list(self.current_administration.incomes)

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
                    administration = administration_from_json(data)
                    self._configure_administration(administration)
            except Exception as e:
                # Handle any errors that occur during file opening or parsing
                QMessageBox.critical(self, "Error", f"Failed to open or parse the file:\n{e}")

    def save_administration(self):
        """
        Opens save dialog if administration has no save file and saves administration as json
        """
        self.current_administration.incomes = self.ui.income_table.get_incomes_as_object()

        folder = self.current_administration.save_location
        data_json_loc = f"{folder}/{self.current_administration.name}_data.json"

        try:
            with open(data_json_loc, 'w') as json_file:
                json_to_save = self.current_administration.to_json()
                json.dump(json_to_save, json_file, indent=4)

        except Exception as e:
            print(f"Error saving file: {e}")



    def closeEvent(self, event):
        """
        Overrides the close event to show a dialog asking if the user saved their work.
        """
        if not self.current_administration.save_location:
            reply = QMessageBox.question(
                self,
                'File not saved',
                'You have not saved this file before, do you want to do so?',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Cancel,
                QMessageBox.StandardButton.Cancel
            )

            if reply == QMessageBox.StandardButton.Yes:
                self.save_administration()

            if reply == QMessageBox.StandardButton.Cancel:
                event.ignore()

        event.accept()
