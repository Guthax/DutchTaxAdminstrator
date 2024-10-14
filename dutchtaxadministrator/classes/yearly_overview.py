from dutchtaxadministrator.classes.administration import Administration
from dutchtaxadministrator.classes.credit_calculator import CreditCalculator


class YearlyOverview:


    def __init__(self, administration: Administration):
        credit_calculator = CreditCalculator(administration)
        self.year = administration.year
        self.gross_income: float = credit_calculator.gross_income_ex_vat
        self.gross_expense: float = credit_calculator.gross_expenses_ex_vat
        self.gross_profit: float = credit_calculator.gross_profit

        self.independent_deductions: float = credit_calculator.independent_deductions
        self.starter_deductions: float = credit_calculator.starter_deductions
        self.investment_deductions: float = 0

        self.mkb_regulation: float = credit_calculator.mkb_regulation

        self.taxable_profit: float = credit_calculator.taxable_profit

        self.full_tax: float = credit_calculator.full_tax

        self.general_tax_discount: float = credit_calculator.general_tax_discount
        self.labour_discount: float = credit_calculator.labour_discount

        self.tax: float = credit_calculator.tax