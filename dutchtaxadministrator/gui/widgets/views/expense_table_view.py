from PyQt6.QtWidgets import QTableView, QPushButton

from dutchtaxadministrator.gui.delegates.float_delegate import FloatDelegate
from dutchtaxadministrator.gui.delegates.upload_file_delegate import FileUploadDelegate


class ExpenseTableView(QTableView):
    """
    IncomeTableView is a custom QTableView that sets custom delegates for specific columns to handle data display and editing
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.float_delegate = FloatDelegate()
        self.file_upload_delegate = FileUploadDelegate()

    def set_delegates(self):
        self.setItemDelegateForColumn(4, self.float_delegate)
        self.setItemDelegateForColumn(5, self.float_delegate)
        self.setItemDelegateForColumn(6, self.float_delegate)
        self.setItemDelegateForColumn(8, self.file_upload_delegate)

