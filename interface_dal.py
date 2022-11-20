import typing
from abc import ABC, abstractmethod


# CRUD
# Generic Repository pattern
class IDal(ABC):
    @abstractmethod
    def add(self, obj: typing.Any) -> None:  # in memory addition
        raise NotImplementedError

    @abstractmethod
    def update(self, obj: typing.Any) -> None:  # in memory addition
        raise NotImplementedError

    @abstractmethod
    def search(self) -> list[typing.Any]:
        raise NotImplementedError

    @abstractmethod
    def save(self) -> None:  # physical commit
        raise NotImplementedError
