import typing
import sqlite3
from abc import abstractmethod, ABC
from multipledispatch import dispatch

from interface_dal import IDal
from interface_customer import ICustomer


class TemplateSqlite(IDal, ABC):

    _any_types: list = list()

    def __init__(self):
        self._connection_string = "data.db"

    def add(self, obj: typing.Any) -> None:
        if obj not in self._any_types:
            obj.validate()
            self._any_types.append(obj)

    def update(self, obj: typing.Any) -> None:
        pass

    def search(self) -> list[typing.Any]:
        return self.execute()

    def save(self) -> None:
        # only the last in memory
        self.execute(self._any_types[-1])
        self._any_types.clear()

    # Fixed sequence, Template design pattern
    @dispatch(ICustomer)
    def execute(self, obj: typing.Any) -> None:  # insert
        self._open()
        self._execute_command(obj)
        self._close()

    @dispatch()
    def execute(self) -> list[typing.Any]:  # select
        self._open()
        obj_types: list = self._execute_command()
        self._close()
        return obj_types

    def _open(self) -> None:
        self.con = sqlite3.connect(self._connection_string)
        self.con.isolation_level = None
        self.cursor = self.con.cursor()

    @dispatch(ICustomer)
    @abstractmethod
    def _execute_command(self, obj: typing.Any) -> None:
        pass

    @dispatch()
    @abstractmethod
    def _execute_command(self) -> list[typing.Any]:
        pass

    def _close(self):
        self.con.close()

    # in memory
    def get_data(self) -> list[typing.Any]:
        return self._any_types
