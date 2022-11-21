from abc import ABC, abstractmethod
import typing


# Strategy design pattern
class IValidation(ABC):
    @abstractmethod
    def validate(self, obj: typing.Any) -> None:
        raise NotImplementedError


class ICustomer(ABC):
    validation: IValidation
    customer_name: str
    phone_number: str
    bill_amount: str
    bill_date: str
    address: str

    @abstractmethod
    def validate(self) -> None:
        raise NotImplementedError


# moved here because it's not a final class
class CustomerBase(ICustomer, IValidation, ABC):
    def __init__(self, validation: IValidation = None, customer_type: str = None, pk: str = None,
                 customer_name: str = None, phone_number: str = None, bill_amount: str = None,
                 bill_date: str = None, address: str = None):
        self.validation: IValidation = validation
        self.id = pk
        self.customer_type = customer_type
        self.customer_name: str = customer_name
        self.phone_number: str = phone_number
        self.bill_amount: str = bill_amount
        self.bill_date: str = bill_date
        self.address: str = address

    def validate(self) -> None:
        self.validation.validate(self)