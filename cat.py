from animal import IAnimal
from i_cat import ICat


class Cat(IAnimal, ICat):
    def __init__(self, name: str):
        super().__init__(name)

    def climb(self):
        print('Estoy escalando...')

    def walk(self):
        print('Estoy caminando...')

    def run(self):
        print('Estoy corriendo...')
