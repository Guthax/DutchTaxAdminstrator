from datetime import datetime
from enum import Enum

from dutchtaxadministrator.classes.sale import Sale

class IncomeType(Enum):
    MKB_WORK = 0
    SALARY = 1
    OTHER_INCOMES = 2
    RESIDENCE = 3
    MORGAGE = 4

class Income(Sale):
    client: str  = ""
    total_hours: float  = 0
    type: IncomeType = IncomeType.MKB_WORK

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
            "client": self.client,
            "type": self.type.value,
            "description": self.description,
            "amount_ex_vat": self.amount_ex_vat,
            "amount_inc_vat": self.amount_inc_vat,
            "vat_percentage": self.vat_percentage,
            "total_hours": self.total_hours,
            "attachments": self.attachments,
        }

def from_json(income_json_dict: dict) -> Income:
    """
    Converts a json object to an Income instance
    Args:
        income_json_dict (dict): Json object as dict
    Returns:
        Income: An instance of Income
    """
    income = Income()
    income.invoice_id = income_json_dict["invoice_id"]
    income.name=income_json_dict["name"]
    income.date = datetime.strptime(income_json_dict["date"], "%d/%m/%Y")
    income.client=income_json_dict["client"]
    income.type = IncomeType(income_json_dict["type"])
    income.description=income_json_dict["description"]
    income.amount_ex_vat=income_json_dict["amount_ex_vat"]
    income.amount_inc_vat=income_json_dict["amount_inc_vat"]
    income.vat_percentage=income_json_dict["vat_percentage"]
    income.total_hours=income_json_dict["total_hours"]
    income.attachments=income_json_dict["attachments"]
    return income
