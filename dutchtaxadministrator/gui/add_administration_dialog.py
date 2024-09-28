from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QDialog

from dutchtaxadministrator.classes.Administration import Administration
from dutchtaxadministrator.gui.gui_files.add_administration_dialog_ui import Ui_add_administration_dialog

class AddAdministrationDialog(QDialog):
    created_administration: pyqtSignal =  pyqtSignal(Administration)

    def __init__(self, parent=None):
        """Initialize the components of the administration dialog."""
        super().__init__(parent)
        self.ui = Ui_add_administration_dialog()
        self.ui.setupUi(self)

        self.ui.button_box.accepted.connect(self.add_administration)

    def add_administration(self):
        """
        Emits new administration from values
        """
        new_administration = Administration()
        new_administration.name = self.ui.name_line_edit.text()
        new_administration.year = self.ui.year_spin_box.value()
        self.created_administration.emit(new_administration)