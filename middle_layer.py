from interface_customer import CustomerBase


class Customer(CustomerBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Lead(CustomerBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
