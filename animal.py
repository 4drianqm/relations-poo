from abc import ABCMeta, abstractmethod


class IAnimal(metaclass=ABCMeta):  # Interfaz
    @abstractmethod
    def walk(self):
        raise NotImplementedError

    @abstractmethod
    def run(self):
        raise NotImplementedError

