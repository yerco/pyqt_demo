from interface_customer import CustomerBase, IValidation


class Customer(CustomerBase):
    def __init__(self, validation: IValidation, _customer_type, *args, **kwargs):
        super().__init__(validation=validation, customer_type=_customer_type, *args, **kwargs)
