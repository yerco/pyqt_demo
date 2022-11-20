import typing
from customer_dal import CustomerDAL


class FactoryDAL:

    _objs: dict = dict()

    def create(self, _type: str) -> typing.Any:
        # Lazy loading design pattern
        if not self._objs:
            self._objs = {
                "CustomerDAL": CustomerDAL("data.db")
            }

        # RIP design pattern
        return self._objs[_type]
