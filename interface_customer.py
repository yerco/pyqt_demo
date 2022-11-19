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
