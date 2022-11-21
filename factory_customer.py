import typing

from middle_layer import Customer
from validation_algorithms import CustomerBasicValidation, PhoneValidation, AddressValidation, BillValidation
from interface_customer import IValidation


# Simple factory design pattern
class FactoryCustomer:

    _objs: dict = dict()

    def create(self, _type: str) -> typing.Any:
        lead_validation: IValidation = PhoneValidation(CustomerBasicValidation())
        self_service_validation: IValidation = CustomerBasicValidation()
        home_delivery_validation: IValidation = AddressValidation(CustomerBasicValidation())
        customer_validation: IValidation = PhoneValidation(BillValidation(AddressValidation(CustomerBasicValidation())))

        # Lazy loading design pattern
        if not self._objs:
            self._objs = {
                "Lead": Customer(validation=lead_validation, _customer_type="Lead"),
                "SelfService": Customer(validation=self_service_validation, _customer_type="SelfService"),
                "HomeDelivery": Customer(validation=home_delivery_validation, _customer_type="HomeDelivery"),
                "Customer": Customer(validation=customer_validation, _customer_type="Customer"),
            }

        # RIP design pattern
        return self._objs[_type]
