import typing
import datetime

from interface_customer import IValidation, ICustomer


class CustomerValidationAll(IValidation):
    def validate(self, obj: ICustomer) -> None:
        if len(obj.customer_name) == 0:
            raise Exception("Customer name is required")
        if len(obj.phone_number) == 0:
            raise Exception("Phone number is required")
        if len(obj.bill_amount) == 0:
            raise Exception("Bill amount is required")
        if datetime.datetime.strptime(obj.bill_date, '%d-%m-%Y') > datetime.datetime.now():
            raise Exception("Bill date is not proper")
        if len(obj.address) == 0:
            raise Exception("Address is required")


class LeadValidation(IValidation):
    def validate(self, obj: typing.Any) -> None:
        if len(obj.customer_name) == 0:
            raise Exception("Customer name is required")
        if len(obj.phone_number) == 0:
            raise Exception("Phone number is required")
