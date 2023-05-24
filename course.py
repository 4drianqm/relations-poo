import random

from faker import Faker

fake = Faker()
content = [
    'Programacion orientada a objetos',
    'Diagramas UML',
    'Metodologias de desarrollo',
    'SCRUM',
    'Clusters',
    'Triggers',
    'Conexiones a base de datos',
    'NoSQL'
]


class Course:
    def __init__(self, name: str):
        self.__name = name
        self.__syllabus = content[random.randint(0, 8)]

    @property
    def syllabus(self):
        return self.__syllabus.upper()

    def __str__(self):
        return f'{self.__name} - {self.__syllabus}'

