from dataclasses import dataclass

from dutchtaxadministrator.classes.administration import Administration

@dataclass
class SingleQuarterOverview:
    incomes_total_inc_vat: float
    incomes_total_ex_vat: float

    expenses_total_inc_vat: float
    expenses_total_ex_vat: float

    total_vat_received:float
    total_vat_paid: float
    vat_payback: float

class QuarterOverview:
    QUARTER_1_MONTHS = [1,2,3]
    QUARTER_2_MONTHS = [4,5,6]
    QUARTER_3_MONTHS = [7,8,9]
    QUARTER_4_MONTHS = [10,11,12]
    def __init__(self, administration: Administration):
        self.administration = administration
        self.incomes_total_inc_vat: float = 0
        self.incomes_total_ex_vat: float= 0

        self.expenses_total:float  = 0

        self.total_vat_received:float = 0
        self.total_vat_paid:float = 0
        self.total_vat_payback:float = 0

        self.overview_q1 = self._get_quarter_overview_for_quarter(1)
        self.overview_q2 = self._get_quarter_overview_for_quarter(2)
        self.overview_q3 = self._get_quarter_overview_for_quarter(3)
        self.overview_q4 = self._get_quarter_overview_for_quarter(4)


    def _get_quarter_overview_for_quarter(self, quarter: int):
        incomes, expenses = self._get_incomes_and_expanses_for_quarter(quarter)

        self.incomes_total_inc_vat = sum([i.amount_inc_vat for i in incomes])
        self.incomes_total_ex_vat = sum([i.amount_ex_vat for i in incomes])

        incomes_vat = sum([i.amount_inc_vat - i.amount_ex_vat for i in incomes])
        expenses_vat = sum([e.amount_inc_vat - e.amount_ex_vat for e in expenses])

        self.expenses_total_inc_vat = sum([e.amount_inc_vat for e in expenses])
        self.expenses_total_ex_vat = sum([e.amount_ex_vat for e in expenses])

        self.total_vat_received = incomes_vat
        self.total_vat_paid = expenses_vat
        self.total_vat_payback = self.total_vat_received - self.total_vat_paid

        return SingleQuarterOverview(self.incomes_total_inc_vat,
                                     self.incomes_total_ex_vat,
                                     self.expenses_total_inc_vat,
                                     self.expenses_total_ex_vat,
                                     self.total_vat_received,
                                     self.total_vat_paid,
                                     self.total_vat_payback)

    def _get_incomes_and_expanses_for_quarter(self, quarter: int) -> tuple:
        if quarter == 1:
            incomes = [income for income in self.administration.incomes if income.date.month in self.QUARTER_1_MONTHS]
            expenses = [expense for expense in self.administration.expenses if expense.date.month in self.QUARTER_1_MONTHS]

        if quarter == 2:
            incomes = [income for income in self.administration.incomes if income.date.month in self.QUARTER_2_MONTHS]
            expenses = [expense for expense in self.administration.expenses if expense.date.month in self.QUARTER_2_MONTHS]

        if quarter == 3:
            incomes = [income for income in self.administration.incomes if income.date.month in self.QUARTER_3_MONTHS]
            expenses = [expense for expense in self.administration.expenses if expense.date.month in self.QUARTER_3_MONTHS]

        if quarter == 4:
            incomes = [income for income in self.administration.incomes if income.date.month in self.QUARTER_4_MONTHS]
            expenses = [expense for expense in self.administration.expenses if expense.date.month in self.QUARTER_4_MONTHS]

        return incomes, expenses