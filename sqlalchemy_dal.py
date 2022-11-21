import typing
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

from interface_dal import IDal


# Adapter design pattern
class SQLAlchemyDAL(IDal):

    def __init__(self):
        self.connection_string = "sqlite:///data.db"

    def _mapping(self):
        base = automap_base()
        # reflect the tables
        base.prepare(autoload_with=self._obj_connection)
        self.customer = base.classes.customer

    def _open(self) -> None:
        self._obj_connection = create_engine(self.connection_string)
        self._mapping()
        self._session = Session(self._obj_connection)
        self._conn = self._obj_connection.connect()

    def _close(self) -> None:
        self._conn.close()
        self._obj_connection.dispose()

    def add(self, obj: typing.Any) -> None:
        self._open()
        self._session.add(self.customer(customer_type=obj.customer_type, customer_name=obj.customer_name,
                                        phone_number=obj.phone_number, bill_amount=obj.bill_amount,
                                        bill_date=obj.bill_date, address=obj.address))

    def update(self, obj: typing.Any) -> None:
        pass

    def search(self) -> list[typing.Any]:
        return self._session.query(self.customer).all()

    def save(self) -> None:
        self._session.commit()

    def get_data(self) -> list[typing.Any]:
        data = self._session.identity_map.values()
        # appending data just for showing them at the grid purposes
        data.append(self.search())
        return data[0]
