from animal import IAnimal
from can_fly import ICanFly


class Bird(IAnimal, ICanFly):
    def __init__(self, name: str):
        super().__init__(name)

    def walk(self):
        print('Estoy caminando...')

    def run(self):
        print('Estoy corriendo...')

    def fly(self):
        print('Estoy volando...')