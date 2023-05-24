from abc import ABCMeta, abstractmethod


class ICanFly(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        raise NotImplementedError
