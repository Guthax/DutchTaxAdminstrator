

class Income:
    invoice_id: str
    name: str
    description:str
    client: str
    amount_ex_vat: float
    vat_percentage: float
    amount_inc_vat: float
    total_hours: float
    total_costs: float
    attachment: str

    def __init__(self):
        self.invoice_id = ""
        self.name = ""
        self.client = ""
        self.description = ""
        self.amount_ex_vat = 0
        self.vat_percentage = 21
        self.amount_inc_vat = 0
        self.total_hours = 0
        self.total_costs = 0
        self.attachment = ""

    def to_json(self):
        """
        Converts income to json object
        Returns:
            dict: Json Object as dict
        """
        income_json = {
            "invoice_id" : self.invoice_id,
            "name": self.name,
            "client": self.client,
            "description": self.description,
            "amount_ex_vat": self.amount_ex_vat,
            "amount_inc_vat": self.amount_inc_vat,
            "vat_percentage": self.vat_percentage,
            "total_hours": self.total_hours,
            "total_costs": self.total_costs,
            "attachment": self.attachment,
        }

        return income_json