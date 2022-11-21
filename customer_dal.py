import typing
from multipledispatch import dispatch
import copy

from interface_customer import ICustomer
from sqlite_dal import TemplateSqlite
from factory_customer import FactoryCustomer


class CustomerDAL(TemplateSqlite):

    def __init__(self):
        super().__init__()

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
    def _execute_command(self) -> list[typing.Any]:
        query = 'SELECT * FROM customer'
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        cust = FactoryCustomer().create("Customer")
        for record in records:
            # mapping
            cust.id = record[0]
            cust.customer_type = record[1]
            cust.customer_name = record[2]
            cust.phone_number = record[3]
            cust.bill_amount = record[4]
            cust.bill_date = record[5]
            cust.address = record[6]
            self._any_types.append(copy.copy(cust))
        return self._any_types
