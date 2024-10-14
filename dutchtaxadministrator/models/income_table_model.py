from datetime import datetime
from enum import Enum
from sys import orig_argv

from PyQt6.QtCore import QAbstractTableModel, Qt, pyqtSignal, QModelIndex

from dutchtaxadministrator.classes.income import Income


class FieldToColumn(Enum):
    INVOICE_ID = (0, "Invoice id")
    DATE = (1, "Date")
    NAME = (2, "Name")
    SELLER = (3, "Client")
    DESCRIPTION = (4, "Description")
    AMOUNT_EX_VAT = (5, "Amount (Ex VAT)")
    VAT_PERCENTAGE = (6, "VAT Percentage")
    AMOUNT_INC_VAT = (7, "Amount (Inc VAT)")
    TOTAL_HOURS = (8, "Total hours")
    ATTACHEMENTS = (9, "Attachments")
    ACTIONS = (10, "Actions")



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
        return 11

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
            if column == FieldToColumn.INVOICE_ID.value[0]:
                return income.invoice_id
            elif column == FieldToColumn.DATE.value[0]:
                return income.date.strftime("%d/%m/%Y")
            elif column == FieldToColumn.NAME.value[0]:
                return income.name
            elif column == FieldToColumn.SELLER.value[0]:
                return income.client
            elif column == FieldToColumn.DESCRIPTION.value[0]:
                return income.description
            elif column == FieldToColumn.AMOUNT_EX_VAT.value[0]:
                return income.amount_ex_vat
            elif column == FieldToColumn.VAT_PERCENTAGE.value[0]:
                return income.vat_percentage
            elif column == FieldToColumn.AMOUNT_INC_VAT.value[0]:
                return income.amount_inc_vat
            elif column == FieldToColumn.TOTAL_HOURS.value[0]:
                return income.total_hours
            elif column == FieldToColumn.ATTACHEMENTS.value[0]:
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
        if column == FieldToColumn.INVOICE_ID.value[0]:
            income.invoice_id = value
        elif column == FieldToColumn.DATE.value[0]:
            income.date = datetime.strptime(value, "%d/%m/%Y")
        elif column == FieldToColumn.NAME.value[0]:
            income.name = value
        elif column == FieldToColumn.SELLER.value[0]:
            income.client = value
        elif column == FieldToColumn.DESCRIPTION.value[0]:
            income.description = value
        elif column == FieldToColumn.AMOUNT_EX_VAT.value[0]:
            income.amount_ex_vat = value
        elif column == FieldToColumn.VAT_PERCENTAGE.value[0]:
            income.vat_percentage = value
        elif column == FieldToColumn.AMOUNT_INC_VAT.value[0]:
            income.amount_inc_vat = value
        elif column == FieldToColumn.TOTAL_HOURS.value[0]:
            income.total_hours = value
        elif column == FieldToColumn.ATTACHEMENTS.value[0]:
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
                headers = [field.value[1] for field in FieldToColumn]
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
        self.incomes_changed.emit(self.incomes)
        self.layoutChanged.emit()

    def flags(self, index):
        """

        Returns the item flags for the given index.

        args:
        index (QModelIndex): The index for which the flags are returned.

        Returns:
        Qt.ItemFlag: The item flags applicable for the given index. If the column of the index is 8, it returns NoItemFlags, indicating no item interaction is possible. Otherwise, it returns a combination of flags indicating the item is enabled, selectable, and editable.
        """
        if index.column() in [7,9]:
            return Qt.ItemFlag.NoItemFlags

        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEditable