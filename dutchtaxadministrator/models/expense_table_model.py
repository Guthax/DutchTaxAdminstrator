from datetime import datetime
from enum import Enum
from sys import orig_argv

from PyQt6.QtCore import QAbstractTableModel, Qt, pyqtSignal, QModelIndex

from dutchtaxadministrator.classes.expense import Expense

class FieldToColumn(Enum):
    INVOICE_ID = (0, "Invoice id")
    DATE = (1, "Date")
    NAME = (2, "Name")
    SELLER = (3, "Seller")
    DESCRIPTION = (4, "Description")
    AMOUNT_EX_VAT = (5, "Amount (Ex VAT)")
    VAT_PERCENTAGE = (6, "VAT Percentage")
    AMOUNT_INC_VAT = (7, "Amount (Inc VAT)")
    PERCENTAGE_DEDUCTABLE = (8, "Percentage Deductible")
    ATTACHEMENTS = (9, "Attachments")
    ACTIONS = (10, "Actions")



class ExpenseTableModel(QAbstractTableModel):
    """
        A model representing a table of incomes, used in a Qt-based GUI.
        Inherits from QAbstractTableModel and provides the necessary methods to interact with the table view.
        """
    expenses_changed = pyqtSignal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.expenses: list[Expense] = []

    def rowCount(self, parent=None):
        return len(self.expenses)

    def columnCount(self, parent=None):
        return len(FieldToColumn)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        """
        Retrieves data to be displayed in the model, based on the given index and role.

        args:
         index: QModelIndex - The index of the item in the model.
         role: int - The role for which the data is required (default is Qt.ItemDataRole.DisplayRole).

        Returns:
         The data for the specified index and role. If the index is not valid or the role is not recognized, it returns None.
         Depending on the column specified by the index, it returns different attributes of the income object:
          - Column 0: invoice_id
          - Column 1: name
          - Column 2: client
          - Column 3: description
          - Column 4: amount_ex_vat
          - Column 5: vat_percentage
          - Column 6: amount_inc_vat
          - Column 7: total_hours
          - Column 8: The last attachment in the list or "No attachments" if there are no attachments.
        """
        if not index.isValid():
            return None
        expense = self.expenses[index.row()]
        column = index.column()
        if role == Qt.ItemDataRole.DisplayRole or role == Qt.ItemDataRole.EditRole:
            if column == FieldToColumn.INVOICE_ID.value[0]:
                return expense.invoice_id
            elif column == FieldToColumn.DATE.value[0]:
                return expense.date.strftime("%d/%m/%Y")
            elif column == FieldToColumn.NAME.value[0]:
                return expense.name
            elif column == FieldToColumn.SELLER.value[0]:
                return expense.seller
            elif column == FieldToColumn.DESCRIPTION.value[0]:
                return expense.description
            elif column == FieldToColumn.AMOUNT_EX_VAT.value[0]:
                return expense.amount_ex_vat
            elif column == FieldToColumn.VAT_PERCENTAGE.value[0]:
                return expense.vat_percentage
            elif column == FieldToColumn.AMOUNT_INC_VAT.value[0]:
                return expense.amount_inc_vat
            elif column == FieldToColumn.PERCENTAGE_DEDUCTABLE.value[0]:
                return expense.percentage_deductable
            elif column == FieldToColumn.ATTACHEMENTS.value[0]:
                return expense.attachments[len(expense.attachments) - 1] if expense.attachments else "No attachments"
        return None

    def setData(self, index, value, role = ...):
        """
        Updates the data of an income entry at the specified index with the provided value.

        args:
        index: The index of the income entry to be updated.
        value: The new value to be set for the income entry.
        role: Optional role parameter (default is ...).

        Returns:
        True if the data was successfully updated, False otherwise.
        """
        if value is None:
            return False
        expense = self.expenses[index.row()]
        column = index.column()
        if column == FieldToColumn.INVOICE_ID.value[0]:
            expense.invoice_id = value
        elif column == FieldToColumn.DATE.value[0]:
            expense.date = datetime.strptime(value, "%d/%m/%Y")
        elif column == FieldToColumn.NAME.value[0]:
            expense.name = value
        elif column == FieldToColumn.SELLER.value[0]:
            expense.seller = value
        elif column == FieldToColumn.DESCRIPTION.value[0]:
            expense.description = value
        elif column == FieldToColumn.AMOUNT_EX_VAT.value[0]:
            expense.amount_ex_vat = value
        elif column == FieldToColumn.VAT_PERCENTAGE.value[0]:
            expense.vat_percentage = value
        elif column == FieldToColumn.AMOUNT_INC_VAT.value[0]:
            expense.amount_inc_vat = value
        elif column == FieldToColumn.PERCENTAGE_DEDUCTABLE.value[0]:
            expense.percentage_deductable = value
        elif column == FieldToColumn.ATTACHEMENTS.value[0]:
            expense.attachments.append(value)
        self.expenses[index.row()] = expense
        self.expenses_changed.emit(self.expenses)
        return True

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        """

        Args:
            section (int): The section index of the header.
            orientation (Qt.Orientation): The orientation of the header (horizontal or vertical).
            role (Qt.ItemDataRole, optional): The role for which the data is requested. Default is Qt.ItemDataRole.DisplayRole.

        Returns:
            str or None: The header label for the given section and orientation if the role is Qt.ItemDataRole.DisplayRole and the orientation is horizontal. Otherwise, returns None.
        """
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:  # Column headers
                headers = [field.value[1] for field in FieldToColumn]
                return headers[section]
        return None

    def add_empty_expense(self):
        """
        Creates a new empty Income instance and adds it to the list of incomes.

        This method initializes a new Income object with default values and appends it
        to the 'incomes' list. After successfully adding the new Income object, it emits
        the 'layoutChanged' signal to indicate that the layout of the data has changed.

        Raises:
            None
        """
        expense = Expense()
        self.expenses.append(expense)
        self.layoutChanged.emit()

    def flags(self, index):
        """

        Returns the item flags for the given index.

        args:
        index (QModelIndex): The index for which the flags are returned.

        Returns:
        Qt.ItemFlag: The item flags applicable for the given index. If the column of the index is 8, it returns NoItemFlags, indicating no item interaction is possible. Otherwise, it returns a combination of flags indicating the item is enabled, selectable, and editable.
        """
        if index.column() == [FieldToColumn.ATTACHEMENTS.value[0]]:
            return Qt.ItemFlag.NoItemFlags

        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEditable