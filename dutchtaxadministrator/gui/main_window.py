import json

from PyQt6.QtGui import QShortcut, QKeySequence

from dutchtaxadministrator.classes.Administration import Administration
from dutchtaxadministrator.gui.add_administration_dialog import AddAdministrationDialog
from dutchtaxadministrator.gui.gui_files.main_window_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QFileDialog


class DutchTaxAdministrator(QMainWindow):
    """Create the main window that stores all of the widgets necessary for the application."""
    current_administration: Administration
    def __init__(self, parent=None):
        """Initialize the components of the main window."""
        super(DutchTaxAdministrator, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resize(1024, 768)
        self.setWindowTitle('DutchTaxAdministrator')
        self.current_administration = Administration("Template")
        self.save_shortcut = QShortcut(QKeySequence("Ctrl+S"), self)

        self.connect_signals()

    def connect_signals(self):
        """
        Connects signals
        """
        self.ui.new_adminitration_action.triggered.connect(self._show_add_administration_dialog)
        self.ui.administration_save_action.triggered.connect(self.save_administration)
        self.ui.add_income_button.clicked.connect(self.ui.income_table.add_blank_row)
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
        self.ui.current_administration_value_label.setText(
            f"{self.current_administration.name} "
            f"({self.current_administration.year})")
        self.ui.overview_tab_widget.setCurrentIndex(0)
        self.ui.income_table.clearContents()

    def save_administration(self):
        """
        Opens save dialog if administration has no save file and saves administration as json
        """
        self.current_administration.incomes = self.ui.income_table.get_incomes_as_object()

        if not self.current_administration.save_location:
            file_name, _ = QFileDialog.getSaveFileName(self,
                                                       "Save JSON File",
                                                       "",
                                                       "JSON Files (*.json);;All Files (*)")
        else:
            file_name = self.current_administration.save_location
        # If the user selects a file name
        if file_name:
            # Ensure the file has the .json extension
            if not file_name.endswith('.json'):
                file_name += '.json'

            # Save the data as a JSON file
            try:
                with open(file_name, 'w') as json_file:
                    self.current_administration.save_location = file_name
                    json_to_save = self.current_administration.to_json()
                    json.dump(json_to_save, json_file, indent=4)

            except Exception as e:
                print(f"Error saving file: {e}")