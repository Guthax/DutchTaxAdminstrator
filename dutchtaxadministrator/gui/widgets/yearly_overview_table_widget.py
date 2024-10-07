from PyQt6.QtWidgets import QTableWidget, QHeaderView, QTableWidgetItem

from dutchtaxadministrator.classes.yearly_overview import YearlyOverview
from dutchtaxadministrator.gui.gui_utilities import show_as_euro


class YearlyOverviewTableWidget(QTableWidget):
    def __init__(self, parent):
        super().__init__()
        self.setColumnCount(1)
        self.setRowCount(12)

        self.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        self.setHorizontalHeaderLabels(["2024"])
        self.setVerticalHeaderLabels(
            ["Total Income EX VAT", "Total Expense EX VAT",
             "Independent Deductions", "Starter Deductions", "Investment Deductions", "Gross Profit", "MKB Regulation",
             "Taxable Profit", "Full Tax", "General tax discount", "Labour discount", "Final Tax"])
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def fill(self, overview: YearlyOverview):
        self.setHorizontalHeaderLabels([str(overview.year)])
        self.setItem(0, 0, show_as_euro(overview.gross_income))
        self.setItem(1, 0, show_as_euro(overview.gross_expense))
        self.setItem(2, 0, show_as_euro(overview.independent_deductions))
        self.setItem(3, 0, show_as_euro(overview.starter_deductions))
        self.setItem(4, 0, show_as_euro(overview.investment_deductions))
        self.setItem(5, 0, show_as_euro(overview.gross_profit))
        self.setItem(6, 0, show_as_euro(overview.mkb_regulation))
        self.setItem(7, 0, show_as_euro(overview.taxable_profit))
        self.setItem(8, 0, show_as_euro(overview.full_tax))
        self.setItem(9, 0, show_as_euro(overview.general_tax_discount))
        self.setItem(10, 0, show_as_euro(overview.labour_discount))
        self.setItem(11, 0, show_as_euro(overview.tax))


