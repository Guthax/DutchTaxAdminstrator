from dataclasses import dataclass
from datetime import datetime

from dutchtaxadministrator.classes.sale import Sale


@dataclass
class Expense(Sale):
    seller: str = ""
    percentage_deductable: float = 0

    def __init__(self):
        self.attachments = []

    def to_json(self) -> dict:
        """
        Converts income to json object
        Returns:
            dict: Json Object as dict
        """
        return {
            "invoice_id": self.invoice_id,
            "date": self.date.strftime("%d/%m/%Y"),
            "name": self.name,
            "seller": self.seller,
            "description": self.description,
            "amount_ex_vat": self.amount_ex_vat,
            "amount_inc_vat": self.amount_inc_vat,
            "vat_percentage": self.vat_percentage,
            "percentage_deductable": self.percentage_deductable,
            "attachments": self.attachments,
        }

def from_json(expanse_json_dict: dict) -> Expense:
    """
    Converts a json object to an Income instance
    Args:
        expanse_json_dict (dict): Json object as dict
    Returns:
        Income: An instance of Income
    """
    expense = Expense()
    expense.invoice_id = expanse_json_dict["invoice_id"]
    expense.date = datetime.strptime(expanse_json_dict["date"], "%d/%m/%Y")
    expense.name = expanse_json_dict["name"]
    expense.seller = expanse_json_dict["seller"]
    expense.description = expanse_json_dict["description"]
    expense.amount_ex_vat = expanse_json_dict["amount_ex_vat"]
    expense.amount_inc_vat = expanse_json_dict["amount_inc_vat"]
    expense.vat_percentage = expanse_json_dict["vat_percentage"]
    expense.percentage_deductable = expanse_json_dict["percentage_deductable"]
    expense.attachments = expanse_json_dict["attachments"]
    return expense
