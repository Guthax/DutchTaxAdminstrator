from dataclasses import dataclass


@dataclass
class Expense:
    invoice_id: str = ""
    name: str = ""
    seller: str = ""
    description: str = ""
    amount_ex_vat: float = 0
    vat_percentage: float = 0
    amount_inc_vat: float = 0

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
            "name": self.name,
            "seller": self.seller,
            "description": self.description,
            "amount_ex_vat": self.amount_ex_vat,
            "amount_inc_vat": self.amount_inc_vat,
            "vat_percentage": self.vat_percentage,
            "attachments": self.attachments,
        }

def from_json(income_json_dict: dict) -> Expense:
    """
    Converts a json object to an Income instance
    Args:
        income_json_dict (dict): Json object as dict
    Returns:
        Income: An instance of Income
    """
    expense = Expense()
    expense.invoice_id = income_json_dict["invoice_id"]
    expense.name = income_json_dict["name"]
    expense.seller = income_json_dict["seller"]
    expense.description = income_json_dict["description"]
    expense.amount_ex_vat = income_json_dict["amount_ex_vat"]
    expense.amount_inc_vat = income_json_dict["amount_inc_vat"]
    expense.vat_percentage = income_json_dict["vat_percentage"]
    expense.attachments = income_json_dict["attachments"]
    return expense
