from faker import Faker

fake = Faker()


class Student:
    def __init__(self):
        self.__name = fake.name()
        self.__learnings: list[str] = []

    def remember(self, learning: str):
        self.__learnings.append(learning)

    def __str__(self):
        return f'{self.__name},{self.__learnings}'

    @property
    def name(self):
        return self.__name
