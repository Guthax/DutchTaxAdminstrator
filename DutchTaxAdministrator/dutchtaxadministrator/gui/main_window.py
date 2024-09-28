from dutchtaxadministrator.gui.gui_files.main_window_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout


class DutchTaxAdministrator(QMainWindow):
    """Create the main window that stores all of the widgets necessary for the application."""

    def __init__(self, parent=None):
        """Initialize the components of the main window."""
        super(DutchTaxAdministrator, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resize(1024, 768)
        self.setWindowTitle('DutchTaxAdministrator')
