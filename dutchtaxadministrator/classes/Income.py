class Income:
    invoice_id: str
    name: str
    description: str
    client: str
    amount_ex_vat: float
    vat_percentage: float
    amount_inc_vat: float
    total_hours: float
    total_costs: float
    attachment: str

    def __init__(self, invoice_id: str = "", name: str = "", client: str = "", description: str = "",
                 amount_ex_vat: float = 0.0, vat_percentage: float = 21.0, amount_inc_vat: float = 0.0,
                 total_hours: float = 0.0, total_costs: float = 0.0, attachment: str = ""):
        self.invoice_id = invoice_id
        self.name = name
        self.client = client
        self.description = description
        self.amount_ex_vat = amount_ex_vat
        self.vat_percentage = vat_percentage
        self.amount_inc_vat = amount_inc_vat
        self.total_hours = total_hours
        self.total_costs = total_costs
        self.attachment = attachment

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
            "total_costs": self.total_costs,
            "attachment": self.attachment,
        }

    @classmethod
    def from_json(cls, income_json_dict: dict) -> 'Income':
        """
        Converts a json object to an Income instance
        Args:
            income_json_dict (dict): Json object as dict
        Returns:
            Income: An instance of Income
        """
        return cls(
            invoice_id=income_json_dict["invoice_id"],
            name=income_json_dict["name"],
            client=income_json_dict["client"],
            description=income_json_dict["description"],
            amount_ex_vat=income_json_dict["amount_ex_vat"],
            amount_inc_vat=income_json_dict["amount_inc_vat"],
            vat_percentage=income_json_dict["vat_percentage"],
            total_hours=income_json_dict["total_hours"],
            total_costs=income_json_dict["total_costs"],
            attachment=income_json_dict["attachment"],
        )
