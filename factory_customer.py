from middle_layer import Customer, Lead, CustomerBase


class FactoryCustomer:

    @classmethod
    def create(cls, customer_type: str) -> CustomerBase:
        if customer_type == "Customer":
            return Customer()
        if customer_type == "Lead":
            return Lead()
