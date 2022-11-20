import typing
from multipledispatch import dispatch
import copy

from interface_customer import ICustomer
from sqlite_dal import TemplateSqlite


class CustomerDAL(TemplateSqlite):

    def __init__(self, connection_string: str):
        super().__init__(connection_string)

    @dispatch(ICustomer)
    def _execute_command(self, obj: typing.Any) -> None:
        self.cursor.execute('begin')
        query = 'INSERT INTO customer(customer_type, customer_name, ' \
                'bill_amount, bill_date, phone_number, address) VALUES ("' + \
                obj.customer_type + '","' + obj.customer_name + '","' + \
                obj.bill_amount + '","' + obj.bill_date + '","' + \
                obj.phone_number + '","' + obj.address + '")'
        self.cursor.execute(query)
        self.cursor.execute('commit')

    @dispatch()
    def _execute_command(self) -> None:
        pass


