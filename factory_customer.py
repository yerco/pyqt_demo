from middle_layer import Customer, Lead, CustomerBase


# Simple factory design pattern
class FactoryCustomer:

    _customers: dict = dict()

    def create(self, customer_type: str) -> CustomerBase:
        # Lazy loading design pattern
        if not self._customers:
            self._customers["Customer"] = Customer()
            self._customers["Lead"] = Lead()

        # RIP design pattern
        return self._customers[customer_type]
