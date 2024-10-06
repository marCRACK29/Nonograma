#from context import Context
from abc import ABC, abstractmethod

class State(ABC):
    @property
    def context(self) -> 'Context':
        return self._context

    @context.setter
    def context(self, context: 'Context') -> None:
        self._context = context

    @abstractmethod
    def go_to(self):
        pass

    @abstractmethod
    def back_to(self):
        pass