from animal import IAnimal
from i_dog import IDog


class Dog(IAnimal, IDog):
    def __init__(self, name: str):
        super().__init__(name)

    def bark(self):
        print('Estoy Ladrando')

    def walk(self):
        print('Estoy caminando')

    def run(self):
        print('Estoy corriendo')

    def bite(self):
        print('Estoy mordiendo...')
