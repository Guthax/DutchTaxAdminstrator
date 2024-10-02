from sys import orig_argv

from PyQt6.QtCore import QAbstractTableModel, Qt, pyqtSignal, QModelIndex

from dutchtaxadministrator.classes.Income import Income

class IncomeTableModel(QAbstractTableModel):
    """
        A model representing a table of incomes, used in a Qt-based GUI.
        Inherits from QAbstractTableModel and provides the necessary methods to interact with the table view.
        """
    incomes_changed = pyqtSignal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.incomes: list[Income] = []

    def rowCount(self, parent=None):
        return len(self.incomes)

    def columnCount(self, parent=None):
        return 10

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
        income = self.incomes[index.row()]
        column = index.column()
        if role == Qt.ItemDataRole.DisplayRole or role == Qt.ItemDataRole.EditRole:
            if column == 0:
                return income.invoice_id
            elif column == 1:
                return income.name
            elif column == 2:
                return income.client
            elif column == 3:
                return income.description
            elif column == 4:
                return income.amount_ex_vat
            elif column == 5:
                return income.vat_percentage
            elif column == 6:
                return income.amount_inc_vat
            elif column == 7:
                return income.total_hours
            elif column == 8:
                return income.attachments[len(income.attachments) - 1] if income.attachments else "No attachments"
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
        income = self.incomes[index.row()]
        column = index.column()
        if column == 0:
            income.invoice_id = value
        elif column == 1:
            income.name = value
        elif column == 2:
            income.client = value
        elif column == 3:
            income.description = value
        elif column == 4:
            income.amount_ex_vat = value
        elif column == 5:
            income.vat_percentage = value
        elif column == 6:
            income.amount_inc_vat = value
        elif column == 7:
            income.total_hours = value
        elif column == 9:
            income.attachments.append(value)
        self.incomes[index.row()] = income
        self.incomes_changed.emit(self.incomes)
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
                headers = ["Invoice ID", "Name", "Client", "Description",
                           "Amount (EX VAT)", "Vat Percentage", "Amount (inc vat)",
                           "Total hours", "Attachments", "Actions"]
                return headers[section]
        return None

    def add_empty_income(self):
        """
        Creates a new empty Income instance and adds it to the list of incomes.

        This method initializes a new Income object with default values and appends it
        to the 'incomes' list. After successfully adding the new Income object, it emits
        the 'layoutChanged' signal to indicate that the layout of the data has changed.

        Raises:
            None
        """
        income = Income()
        self.incomes.append(Income())
        self.layoutChanged.emit()

    def flags(self, index):
        """

        Returns the item flags for the given index.

        args:
        index (QModelIndex): The index for which the flags are returned.

        Returns:
        Qt.ItemFlag: The item flags applicable for the given index. If the column of the index is 8, it returns NoItemFlags, indicating no item interaction is possible. Otherwise, it returns a combination of flags indicating the item is enabled, selectable, and editable.
        """
        if index.column() == 8:
            return Qt.ItemFlag.NoItemFlags

        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEditable