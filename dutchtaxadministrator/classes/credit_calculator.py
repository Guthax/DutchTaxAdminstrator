import configparser
import os
from abc import ABC, abstractmethod
from enum import Enum

from dutchtaxadministrator.classes.administration import Administration

config = configparser.ConfigParser()
file = os.path.join(os.path.dirname(__file__), '../config/tax_service_configurations.ini')
config.read(file)

def get_subsection_config(year, subsection):
    section = f"{year}.{subsection}" if subsection else f"{year}"
    if section in config:
        return dict(config[section])  # Convert section to a dictionary
    else:
        raise ValueError(f"No configuration found for section {section}")


class CreditCalculator:
    def __init__(self, administration: Administration):
        self.administration = administration
        self.gross_income_ex_vat = sum([income.amount_ex_vat for income in self.administration.incomes])
        self.gross_expenses_ex_vat = sum([expense.amount_ex_vat * expense.percentage_deductable for expense in self.administration.expenses])

        self.independent_deductions = 0 #self.calculate_independent_deductions()
        self.starter_deductions = 0#self.calculate_starter_deductions()
        self.investment_deductions = 0#self.calculate_investment_deductions()
        deductions = sum([self.independent_deductions, self.starter_deductions, self.investment_deductions])

        self.gross_profit = self.gross_income_ex_vat - self.gross_expenses_ex_vat - deductions

        self.mkb_regulation = 0#self.calculate_mkb_regulation()

        self.taxable_profit = self.gross_profit - self.mkb_regulation

        self.full_tax = self.calculate_full_tax()

        self.general_tax_discount = self.calculate_general_tax_discount()
        self.labour_discount = self.calculate_labour_discount()
        discounts = self.general_tax_discount + self.labour_discount

        self.tax = max(0,self.full_tax - discounts)

    def calculate_full_tax(self):
        income_tax_boxes = get_subsection_config(self.administration.year, 'income_tax_boxes')
        num_disks = int(income_tax_boxes['income_discs'])

        to_tax = self.taxable_profit
        total_tax = 0

        for disk in range(num_disks - 1,0,-1):
            lower = float(income_tax_boxes[f"disc_{disk + 1}_lower"])
            if to_tax > lower:
                diff = to_tax - lower

                total_tax +=  diff * float(income_tax_boxes[f"disc_{disk + 1}_tax_percentage"])
                to_tax -= diff
        total_tax += to_tax * float(income_tax_boxes[f"disc_1_tax_percentage"])
        return total_tax

    def calculate_independent_deductions(self) -> float:
        id_dict = get_subsection_config(self.administration.year, 'independent_deductions')
        id_amount = float(id_dict['independent_deduction_amount'])
        return id_amount

    def calculate_starter_deductions(self) -> float:
        return 0

    def calculate_mkb_regulation(self) -> float:
        mkb_dict = get_subsection_config(self.administration.year, 'mkb')
        mkb_percentage = float(mkb_dict['mkb_discount_percentage'])
        return max(0, mkb_percentage * self.gross_profit)

    def calculate_investment_deductions(self) -> float:
        return 0

    def calculate_general_tax_discount(self) -> float:
        gtd_dict = get_subsection_config(self.administration.year, 'general_tax_discount')
        num_disks = int(gtd_dict['num_disks'])
        for disk in range(num_disks - 1,0,-1):
            if self.gross_profit > float(gtd_dict[f"general_tax_discount_disk_{disk + 1}_lower"]):
                amount_for_calculation = self.gross_profit - float(gtd_dict[f"general_tax_discount_disk_{disk + 1}_lower"])
                percentage =  amount_for_calculation * float(gtd_dict[f"general_tax_discount_disk_{disk + 1}_percentage"])
                return float(gtd_dict[f"general_tax_discount_disk_{disk + 1}_base"]) + percentage
        return float(gtd_dict[f"general_tax_discount_disk_1_base"])


        gtd_dict = get_subsection_config(self.administration.year, 'general_tax_discount')
        gtd_upper_bound = float(gtd_dict['general_tax_discount_upper_bound'])
        gtd_lower_bound = float(gtd_dict['general_tax_discount_lower_bound'])
        gtd_percentage = float(gtd_dict['general_tax_discount_percentage'])
        subtraction = max(0, (self.taxable_profit - gtd_upper_bound) * gtd_percentage)
        return gtd_lower_bound - subtraction

    def calculate_labour_discount(self) -> float:
        labour_discount_dict = get_subsection_config(self.administration.year, 'labour_discount')
        num_disks = int(labour_discount_dict['num_discs'])
        for disk in range(num_disks - 1,0,-1):
            if self.gross_profit > float(labour_discount_dict[f"labour_discount_disc_{disk + 1}_lower"]):
                amount_for_calculation = self.gross_profit - float(labour_discount_dict[f"labour_discount_disc_{disk + 1}_lower"])
                percentage =  amount_for_calculation * float(labour_discount_dict[f"labour_discount_disc_{disk + 1}_percentage"])
                return float(labour_discount_dict[f"labour_discount_disc_{disk + 1}_base"]) + percentage
        return self.gross_profit * float(labour_discount_dict[f"labour_discount_disc_1_percentage"])

        ld_dict = get_subsection_config(self.administration.year, 'labour_discount')
        ld_upper_bound = float(ld_dict['labour_discount_upper_bound'])
        ld_lower_bound = float(ld_dict['labour_discount_lower_bound'])
        ld_percentage = float(ld_dict['labour_discount_percentage'])
        subtraction = (self.gross_profit - ld_upper_bound) * ld_percentage
        return ld_lower_bound - subtraction

    def calculate_zvw(self) -> float:
        zvw_dict =  get_subsection_config(self.administration.year, 'zvw')
        zvw_percentage = float(zvw_dict['zvw_percentage'])
        return self.gross_profit * zvw_percentage

    def calculate_final_tax(self) -> float:
        pass