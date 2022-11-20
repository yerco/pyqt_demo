from abc import ABC
from interface_customer import ICustomer, IValidation


class CustomerBase(ICustomer, IValidation, ABC):
    def __init__(self, validation: IValidation = None, customer_name: str = None, phone_number: str = None,
                 bill_amount: str = None, bill_date: str = None, address: str = None):
        self.validation: IValidation = validation
        self.customer_name: str = customer_name
        self.phone_number: str = phone_number
        self.bill_amount: str = bill_amount
        self.bill_date: str = bill_date
        self.address: str = address

    def validate(self) -> None:
        self.validation.validate(self)


class Customer(CustomerBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Lead(CustomerBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
