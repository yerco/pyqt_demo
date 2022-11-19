import datetime

from abc import ABC, abstractmethod
from interface_customer import ICustomer


class CustomerBase(ICustomer, ABC):
    def __init__(self, customer_name: str = None, phone_number: str = None, bill_amount: str = None,
                 bill_date: str = None, address: str = None):
        self.customer_name: str = customer_name
        self.phone_number: str = phone_number
        self.bill_amount: str = bill_amount
        self.bill_date: str = bill_date
        self.address: str = address

    @abstractmethod
    def validate(self) -> None:
        raise NotImplementedError


class Customer(CustomerBase):

    def __init__(self, *args, **kwargs):
        super(CustomerBase, self).__init__(*args, **kwargs)

    def validate(self) -> None:
        if len(self.customer_name) == 0:
            raise Exception("Customer name is required")
        if len(self.phone_number) == 0:
            raise Exception("Phone number is required")
        if len(self.bill_amount) == 0:
            raise Exception("Bill amount is required")
        if datetime.datetime.strptime(self.bill_date, '%d-%m-%Y') > datetime.datetime.now():
            raise Exception("Bill date is not proper")
        if len(self.address) == 0:
            raise Exception("Address is required")


class Lead(CustomerBase):

    def __init__(self, *args, **kwargs):
        super(CustomerBase, self).__init__(*args, **kwargs)

    def validate(self) -> None:
        if len(self.customer_name) == 0:
            raise Exception("Customer name is required")
        if len(self.phone_number) == 0:
            raise Exception("Phone number is required")
