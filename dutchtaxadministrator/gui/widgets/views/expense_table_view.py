from PyQt6.QtWidgets import QTableView, QPushButton, QHeaderView

from dutchtaxadministrator.gui.delegates.date_delegate import DateDelegate
from dutchtaxadministrator.gui.delegates.float_delegate import FloatDelegate
from dutchtaxadministrator.gui.delegates.upload_file_delegate import FileUploadDelegate
from dutchtaxadministrator.models.expense_table_model import FieldToColumn


class ExpenseTableView(QTableView):
    """
    IncomeTableView is a custom QTableView that sets custom delegates for specific columns to handle data display and editing
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.float_delegate = FloatDelegate()
        self.file_upload_delegate = FileUploadDelegate()
        self.date_delegate = DateDelegate()
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)



    def set_delegates(self):
        self.setItemDelegateForColumn(FieldToColumn.DATE.value[0], self.date_delegate)
        self.setItemDelegateForColumn(FieldToColumn.AMOUNT_EX_VAT.value[0], self.float_delegate)
        self.setItemDelegateForColumn(FieldToColumn.VAT_PERCENTAGE.value[0], self.float_delegate)
        self.setItemDelegateForColumn(FieldToColumn.AMOUNT_INC_VAT.value[0], self.float_delegate)
        self.setItemDelegateForColumn(FieldToColumn.PERCENTAGE_DEDUCTABLE.value[0], self.float_delegate)
        self.setItemDelegateForColumn(FieldToColumn.ACTIONS.value[0], self.file_upload_delegate)

