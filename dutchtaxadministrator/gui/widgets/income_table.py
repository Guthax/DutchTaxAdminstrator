from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QApplication, QMessageBox, QPushButton, QHeaderView, \
    QFileDialog, QWidget, QVBoxLayout, QHBoxLayout, QLabel
import sys

from dutchtaxadministrator.classes.Administration import Administration
from dutchtaxadministrator.classes.Income import Income


class IncomeTable(QTableWidget):
    changed: pyqtSignal = pyqtSignal()

    def __init__(self):
        """
        Initializes IncomeTable as a child of QTableWidget and sets up headers.
        """
        super().__init__()
        # Set up table dimensions (rows, columns)
        self.setRowCount(0)
        self.setColumnCount(11)

        # Enable cell editing (editable by default)
        self.setEditTriggers(QTableWidget.EditTrigger.AllEditTriggers)

        # Set column headers
        self.setHorizontalHeaderLabels([
            "Invoice ID",
            "Name",
            "Client",
            "Description",
            "Amount (Ex. VAT)",
            "VAT Percentage",
            "Amount (Inc. VAT)",
            "Total Hours",
            "Costs",
            "Attachments",
            "Actions"
        ])
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.cellClicked.connect(lambda:self.changed.emit())

    # Method to add a blank row
    def add_blank_row(self):
        """
        Add a blank row at the last index
        """
        row_position = self.rowCount()
        self.insertRow(row_position)

        # Add a button to the "Attachment" column of the new row
        self.create_attachment_button(row_position)

    def create_attachment_button(self, row_position):
        """
        Create a button in the 'Attachment' column to open a file dialog for selecting a file.
        Args:
            row_position: Position of the row where the button should be added.
        """
        button = QPushButton("Select File")
        button.clicked.connect(lambda: self.open_file_dialog(row_position))
        self.setCellWidget(row_position, 10, button)

    def open_file_dialog(self, row):
        """
        Opens a file dialog to pick a file and stores the selected file path in the respective row.
        Args:
            row: The row index where the file is being selected.
        """
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select Attachment", "", "All Files (*)")

        if file_path:
            # Store the file path in the cell
            self.setItem(row, 9, QTableWidgetItem(file_path))
    def delete_row(self, row):
        """
        Deletes row at index
        Args:
            row: Row index
        """
        self.removeRow(row)

    def clear(self):
        """
        Clear the table content and reset the row count.
        """
        self.clearContents()
        self.setRowCount(0)

    def get_value_at_row_and_column_or_none(self, row: int, column: int) -> str | None:
        """
        If there is a value at the specific position, return as str, else return None
        Args:
            row: row index
            column: column index

        Returns:
            str | None: Value at the cell or None
        """
        try:
            return self.item(row, column).text()
        except AttributeError:
            return None

    def fill_table_from_income_list(self, incomes):
        """
        Populates the table with income data.

        Parameters:
            incomes (list): A list of income objects. Each object should have
            attributes: invoice_id, name, client, description, amount_ex_vat,
            vat_percentage, amount_inc_vat, total_hours, costs, and attachment.
        """
        self.clear()
        self.setRowCount(len(incomes))
        for i, income in enumerate(incomes):
            self.setItem(i, 0, QTableWidgetItem(income.invoice_id))
            self.setItem(i, 1, QTableWidgetItem(income.name))
            self.setItem(i, 2, QTableWidgetItem(income.client))
            self.setItem(i, 3, QTableWidgetItem(income.description))
            self.setItem(i, 4, QTableWidgetItem(income.amount_ex_vat))
            self.setItem(i, 5, QTableWidgetItem(income.vat_percentage))
            self.setItem(i, 6, QTableWidgetItem(income.amount_inc_vat))
            self.setItem(i, 7, QTableWidgetItem(income.total_hours))
            self.setItem(i, 8, QTableWidgetItem(income.total_costs))

            # Add a button in the attachment column
            self.create_attachment_button(i)

            # Set the file path if it's already set in the income object
            if income.attachments:
                self.setItem(i, 9, QTableWidgetItem(income.attachments[0]))

    def get_incomes_as_object(self):
        """
        Converts data within rows to Income objects.
        Returns:
            List[Income]: Income object list
        """
        incomes = []
        for i in range(self.rowCount()):
            # Check if all columns in the row are empty
            if all(self.get_value_at_row_and_column_or_none(i, col) is None for col in range(self.columnCount())):
                continue
            invoice_id = self.get_value_at_row_and_column_or_none(i, 0)
            name = self.get_value_at_row_and_column_or_none(i, 1)
            client = self.get_value_at_row_and_column_or_none(i, 2)
            description = self.get_value_at_row_and_column_or_none(i, 3)
            amount_ex_vat = self.get_value_at_row_and_column_or_none(i, 4)
            vat_percentage = self.get_value_at_row_and_column_or_none(i, 5)
            amount_inc_vat = self.get_value_at_row_and_column_or_none(i, 6)
            hours = self.get_value_at_row_and_column_or_none(i, 7)
            costs = self.get_value_at_row_and_column_or_none(i, 8)
            attachment = self.get_value_at_row_and_column_or_none(i, 9)

            income = Income()
            income.invoice_id = invoice_id
            income.name = name
            income.client = client
            income.description = description
            income.amount_ex_vat = amount_ex_vat
            income.amount_inc_vat = amount_inc_vat
            income.vat_percentage = vat_percentage
            income.total_hours = hours
            income.total_costs = costs
            income.attachments = [attachment]

            incomes.append(income)
        return incomes


