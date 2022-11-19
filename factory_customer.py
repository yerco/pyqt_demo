from middle_layer import Customer, Lead, CustomerBase


# Simple factory design pattern
class FactoryCustomer:

    _customers: dict = dict()

    def __init__(self):
        self._customers["Customer"] = Customer()
        self._customers["Lead"] = Lead()

    def create(self, customer_type: str) -> CustomerBase:
        # RIP design pattern
        return self._customers[customer_type]
