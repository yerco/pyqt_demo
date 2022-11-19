class Customer:
    def __init__(self, customer_name: str = None, phone_number: str = None, bill_amount: str = None,
                 bill_date: str = None, address: str = None):
        self.customer_name: str = customer_name
        self.phone_number: str = phone_number
        self.bill_amount: str = bill_amount
        self.bill_date: str = bill_date
        self.address: str = address


# Lead is a Customer with fewer validations
class Lead:
    def __init__(self, customer_name: str = None, phone_number: str = None, bill_amount: str = None,
                 bill_date: str = None, address: str = None):
        self.customer_name: str = customer_name
        self.phone_number: str = phone_number
        self.bill_amount: str = bill_amount
        self.bill_date: str = bill_date
        self.address: str = address
