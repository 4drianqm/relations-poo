from abc import ABCMeta, abstractmethod


class ICat(metaclass=ABCMeta):

    @abstractmethod
    def climb(self):
        raise NotImplementedError
