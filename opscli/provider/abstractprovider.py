from abc import ABC, abstractmethod

class AbstractProvider(ABC):

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def help(self):
        pass