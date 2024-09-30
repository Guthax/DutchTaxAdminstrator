from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QApplication, QMessageBox, QPushButton, QHeaderView
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
        self.setColumnCount(9)

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
            "Attachment",
        ])
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    # Method to add a blank row
    def add_blank_row(self):
        """
        At blank row after last index
        """
        row_position = self.rowCount()
        self.insertRow(row_position)

    def delete_row(self, row):
        """
        Deletes row at index
        Args:
            row:  Row index
        """
        self.removeRow(row)

    def get_value_at_row_and_column_or_none(self, row: int, column:int) -> str | None:
        """
        If there is a value at the specific position, return as str, else return None
        Args:
            row: row index
            column: column index

        Returns:
            str | None: Income or None

        """
        try:
            return self.item(row, column).text()
        except AttributeError:
            return None

    def get_incomes_as_object(self):
        """
        Converts data within rows to Income objects
        Returns:
            List[Income]: Income object list
        """
        incomes = []
        for i in range(0, self.rowCount()):
            invoice_id = self.get_value_at_row_and_column_or_none(i, 0)
            name = self.get_value_at_row_and_column_or_none(i, 1)
            description = self.get_value_at_row_and_column_or_none(i, 2)
            amount_ex_vat = self.get_value_at_row_and_column_or_none(i, 3)
            vat_percentage = self.get_value_at_row_and_column_or_none(i, 4)
            amount_inc_vat = self.get_value_at_row_and_column_or_none(i, 5)
            hours = self.get_value_at_row_and_column_or_none(i, 6)
            costs = self.get_value_at_row_and_column_or_none(i, 7)
            attachments = ""

            income = Income()
            income.invoice_id = invoice_id
            income.name = name
            income.description = description
            income.amount_ex_vat = amount_ex_vat
            income.amount_inc_vat = amount_inc_vat
            income.vat_rate =  vat_percentage
            income.total_hours = hours
            income.total_costs = costs
            income.attachment = attachments

            incomes.append(income)
        return incomes

