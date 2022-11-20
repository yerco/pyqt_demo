import typing
from customer_dal import CustomerDAL
from sqlalchemy_dal import SQLAlchemyDAL


class FactoryDAL:

    _objs: dict = dict()

    def create(self, _type: str) -> typing.Any:
        # Lazy loading design pattern
        if not self._objs:
            self._objs = {
                "CustomerDAL": CustomerDAL(),
                "SQLAlchemyDAL": SQLAlchemyDAL()
            }

        # RIP design pattern
        return self._objs[_type]
