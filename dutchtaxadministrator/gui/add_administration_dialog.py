from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QDialog
from PyQt6.QtWidgets import QFileDialog

from dutchtaxadministrator.classes.Administration import Administration
from dutchtaxadministrator.gui.gui_files.add_administration_dialog_ui import Ui_add_administration_dialog

class AddAdministrationDialog(QDialog):
    created_administration: pyqtSignal =  pyqtSignal(Administration)

    def __init__(self, parent=None):
        """Initialize the components of the administration dialog."""
        super().__init__(parent)
        self.ui = Ui_add_administration_dialog()
        self.ui.setupUi(self)
        self.connect_signals()


    def connect_signals(self):
        self.ui.button_box.accepted.connect(self.add_administration)
        self.ui.storage_location_push_button.clicked.connect(self.open_file_location_browser)

    def open_file_location_browser(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        if dialog.exec():
            directory = dialog.selectedFiles()[0]
            self.ui.storage_location_path_edit.setText(directory)

    def add_administration(self):
        """
        Emits new administration from values
        """
        new_administration = Administration(self.ui.name_line_edit.text())
        new_administration.year = self.ui.year_spin_box.value()
        new_administration.save_location = f"{self.ui.storage_location_path_edit.text()}/{new_administration.name}"
        self.created_administration.emit(new_administration)