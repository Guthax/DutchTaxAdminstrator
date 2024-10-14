from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView

from dutchtaxadministrator.classes.quarter_overview import QuarterOverview


class QuarterOverviewTableWidget(QTableWidget):
    def __init__(self, parent):
        super().__init__()
        self.setColumnCount(4)
        self.setRowCount(7)

        self.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        self.setHorizontalHeaderLabels(["Quarter 1", "Quarter 2", "Quarter 3", "Quarter 4"])
        self.setVerticalHeaderLabels(
            ["Total Income Inc VAT", "Total Income Ex VAT", "Total Expense Inc VAT", "Total Expense Ex VAT", "Total VAT received", "Total VAT paid", "Total VAT Payback"])
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    def fill(self, overview: QuarterOverview):
        self.setItem(0, 0, self.show_as_euro(overview.overview_q1.incomes_total_inc_vat))
        self.setItem(0, 1, self.show_as_euro(overview.overview_q2.incomes_total_inc_vat))
        self.setItem(0, 2, self.show_as_euro(overview.overview_q3.incomes_total_inc_vat))
        self.setItem(0, 3, self.show_as_euro(overview.overview_q4.incomes_total_inc_vat))

        self.setItem(1, 0, self.show_as_euro(overview.overview_q1.incomes_total_ex_vat))
        self.setItem(1, 1, self.show_as_euro(overview.overview_q2.incomes_total_ex_vat))
        self.setItem(1, 2, self.show_as_euro(overview.overview_q3.incomes_total_ex_vat))
        self.setItem(1, 3, self.show_as_euro(overview.overview_q4.incomes_total_ex_vat))

        self.setItem(2, 0, self.show_as_euro(overview.overview_q1.expenses_total_inc_vat))
        self.setItem(2, 1, self.show_as_euro(overview.overview_q2.expenses_total_inc_vat))
        self.setItem(2, 2, self.show_as_euro(overview.overview_q3.expenses_total_inc_vat))
        self.setItem(2, 3, self.show_as_euro(overview.overview_q4.expenses_total_inc_vat))

        self.setItem(3, 0, self.show_as_euro(overview.overview_q1.expenses_total_ex_vat))
        self.setItem(3, 1, self.show_as_euro(overview.overview_q2.expenses_total_ex_vat))
        self.setItem(3, 2, self.show_as_euro(overview.overview_q3.expenses_total_ex_vat))
        self.setItem(3, 3, self.show_as_euro(overview.overview_q4.expenses_total_ex_vat))

        self.setItem(4, 0, self.show_as_euro(overview.overview_q1.total_vat_received))
        self.setItem(4, 1, self.show_as_euro(overview.overview_q2.total_vat_received))
        self.setItem(4, 2, self.show_as_euro(overview.overview_q3.total_vat_received))
        self.setItem(4, 3, self.show_as_euro(overview.overview_q4.total_vat_received))

        self.setItem(5, 0, self.show_as_euro(overview.overview_q1.total_vat_paid))
        self.setItem(5, 1, self.show_as_euro(overview.overview_q2.total_vat_paid))
        self.setItem(5, 2, self.show_as_euro(overview.overview_q3.total_vat_paid))
        self.setItem(5, 3, self.show_as_euro(overview.overview_q4.total_vat_paid))

        self.setItem(6, 0, self.show_as_euro(overview.overview_q1.vat_payback))
        self.setItem(6, 1, self.show_as_euro(overview.overview_q2.vat_payback))
        self.setItem(6, 2, self.show_as_euro(overview.overview_q3.vat_payback))
        self.setItem(6, 3, self.show_as_euro(overview.overview_q4.vat_payback))

    def show_as_euro(self, value) -> QTableWidgetItem:
        return QTableWidgetItem(f"€ {value}")