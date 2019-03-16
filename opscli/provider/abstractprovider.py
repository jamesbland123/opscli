""" Abstract Class for service providers """
from abc import ABC, abstractmethod

class AbstractProvider(ABC):
    """
    Abstract class to be used as a base class for
    additional service providers to implement.

    Inherit from class AbstractProvider and implement 
    its interface.

    Example: 
        class Myclass(AbstractProvider):
            pass

            def get():
                pass

    """

    @abstractmethod
    def get(self):
        pass
