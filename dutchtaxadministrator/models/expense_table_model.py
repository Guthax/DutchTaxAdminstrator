from sys import orig_argv

from PyQt6.QtCore import QAbstractTableModel, Qt, pyqtSignal, QModelIndex

from dutchtaxadministrator.classes.Expense import Expense

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
        return 9

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
            if column == 0:
                return expense.invoice_id
            elif column == 1:
                return expense.name
            elif column == 2:
                return expense.seller
            elif column == 3:
                return expense.description
            elif column == 4:
                return expense.amount_ex_vat
            elif column == 5:
                return expense.vat_percentage
            elif column == 6:
                return expense.amount_inc_vat
            elif column == 7:
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
        if column == 0:
            expense.invoice_id = value
        elif column == 1:
            expense.name = value
        elif column == 2:
            expense.seller = value
        elif column == 3:
            expense.description = value
        elif column == 4:
            expense.amount_ex_vat = value
        elif column == 5:
            expense.vat_percentage = value
        elif column == 6:
            expense.amount_inc_vat = value
        elif column == 8:
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
                headers = ["Invoice ID", "Name", "Seller", "Description",
                           "Amount (EX VAT)", "Vat Percentage", "Amount (inc vat)",
                           "Attachments", "Actions"]
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
        if index.column() == 7:
            return Qt.ItemFlag.NoItemFlags

        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEditable