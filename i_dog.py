from abc import ABCMeta, abstractmethod


class IDog(metaclass=ABCMeta):
    @abstractmethod
    def bark(self):
        raise NotImplementedError

    def bite(self):
        raise NotImplementedError

