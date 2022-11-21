import typing
import datetime
from abc import ABC, abstractmethod

from interface_customer import IValidation, ICustomer


class CustomerBasicValidation(IValidation):

    def validate(self, obj: typing.Any) -> None:
        if len(obj.customer_name) == 0:
            raise Exception("Customer name is required")


# Decorator design pattern
class ValidationLinker(IValidation, ABC):

    next_validator: IValidation = None

    def __init__(self, i_validation: IValidation):
        self.next_validator = i_validation

    @abstractmethod
    def validate(self, obj: typing.Any) -> None:
        self.next_validator.validate(obj)


class PhoneValidation(ValidationLinker):

    def __init__(self, cust_validate: IValidation):
        super().__init__(cust_validate)

    def validate(self, obj: typing.Any) -> None:
        super().validate(obj)  # this will call the top of the cake
        if len(obj.phone_number) == 0:
            raise Exception("Phone number is required")


class BillValidation(ValidationLinker):
    def __init__(self, cust_validate):
        super(BillValidation, self).__init__(cust_validate)

    def validate(self, obj: ICustomer) -> None:
        super().validate(obj)
        if datetime.datetime.strptime(obj.bill_date, '%d-%m-%Y') >= datetime.datetime.now():
            raise Exception("Bill date is not proper")
        if obj.bill_amount == '':
            raise Exception("Bill Amount is required")


class AddressValidation(ValidationLinker):
    def __init__(self, cust_validate):
        super(AddressValidation, self).__init__(cust_validate)

    def validate(self, obj: ICustomer) -> None:
        super().validate(obj)
        if obj.address == '':
            raise Exception("Address is required")
