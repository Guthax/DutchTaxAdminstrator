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
        self.setColumnCount(10)

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

    def clear(self):

        self.clearContents()
        self.setRowCount(0)

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
            self.setItem(i, 9, QTableWidgetItem(income.attachment))
            


    def get_incomes_as_object(self):
        """
        Converts data within rows to Income objects
        Returns:
            List[Income]: Income object list
        """
        incomes = []
        for i in range(0, self.rowCount()):
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
            attachments = ""

            income = Income()
            income.invoice_id = invoice_id
            income.name = name
            income.client = client
            income.description = description
            income.amount_ex_vat = amount_ex_vat
            income.amount_inc_vat = amount_inc_vat
            income.vat_percentage =  vat_percentage
            income.total_hours = hours
            income.total_costs = costs
            income.attachment = attachments

            incomes.append(income)
        return incomes

