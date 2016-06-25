from abc import ABCMeta, abstractmethod
from server import Components


class Component(metaclass=ABCMeta):
    def __init__(self, name):
        Components.register(name, self)

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def destroy(self):
        pass
