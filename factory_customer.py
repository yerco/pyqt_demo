import typing

from middle_layer import Customer, Lead
from validation_algorithms import CustomerValidationAll, LeadValidation
from customer_dal import CustomerDAL


# Simple factory design pattern
class FactoryCustomer:

    _objs: dict = dict()

    def create(self, _type: str) -> typing.Any:
        # Lazy loading design pattern
        if not self._objs:
            self._objs = {
                "Customer": Customer(validation=CustomerValidationAll()),
                "Lead": Lead(validation=LeadValidation()),
                "CustomerDAL": CustomerDAL("data.db")
            }

        # RIP design pattern
        return self._objs[_type]
