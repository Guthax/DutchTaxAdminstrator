from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QApplication, QMessageBox, QPushButton
import sys

class IncomeTable(QTableWidget):
    def __init__(self):
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
            "Description",
            "Amount (Ex. VAT)",
            "Amount (Inc. VAT)",
            "VAT Percentage",
            "Total Hours",
            "Costs",
            "Attachment",
        ])

    # Method to add a blank row
    def add_blank_row(self):
        row_position = self.rowCount()
        self.insertRow(row_position)

    def delete_row(self, row):
        self.removeRow(row)
