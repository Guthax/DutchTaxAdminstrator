class Income:
    invoice_id: str = ""
    name: str = ""
    description: str = ""
    client: str  = ""
    amount_ex_vat: float = 0
    vat_percentage: float = 0
    amount_inc_vat: float = 0
    total_hours: float  = 0

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
            "client": self.client,
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
    income.client=income_json_dict["client"]
    income.description=income_json_dict["description"]
    income.amount_ex_vat=income_json_dict["amount_ex_vat"]
    income.amount_inc_vat=income_json_dict["amount_inc_vat"]
    income.vat_percentage=income_json_dict["vat_percentage"]
    income.total_hours=income_json_dict["total_hours"]
    income.attachments=income_json_dict["attachments"]
    return income
