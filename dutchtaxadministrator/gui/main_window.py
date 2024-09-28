from dutchtaxadministrator.classes.Administration import Administration
from dutchtaxadministrator.gui.add_administration_dialog import AddAdministrationDialog
from dutchtaxadministrator.gui.gui_files.main_window_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout


class DutchTaxAdministrator(QMainWindow):
    """Create the main window that stores all of the widgets necessary for the application."""
    selected_administration: Administration
    def __init__(self, parent=None):
        """Initialize the components of the main window."""
        super(DutchTaxAdministrator, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resize(1024, 768)
        self.setWindowTitle('DutchTaxAdministrator')
        self.selected_administration = None
        self.connect_signals()

    def connect_signals(self):
        """
        Connects signals
        """
        self.ui.new_adminitration_action.triggered.connect(self._show_add_administration_dialog)
        self.ui.add_income_button.clicked.connect(self.ui.income_table.add_blank_row)

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
        self.selected_administration = administration
        self.ui.current_administration_value_label.setText(
            f"{self.selected_administration.name} ({self.selected_administration.year})")
        self.ui.overview_tab_widget.setCurrentIndex(0)