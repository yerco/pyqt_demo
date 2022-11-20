from middle_layer import Customer, Lead
from interface_customer import ICustomer
from validation_algorithms import CustomerValidationAll, LeadValidation


# Simple factory design pattern
class FactoryCustomer:

    _customers: dict = dict()

    def create(self, customer_type: str) -> ICustomer:
        # Lazy loading design pattern
        if not self._customers:
            self._customers = {
                "Customer": Customer(validation=CustomerValidationAll()),
                "Lead": Lead(validation=LeadValidation())
            }

        # RIP design pattern
        return self._customers[customer_type]
