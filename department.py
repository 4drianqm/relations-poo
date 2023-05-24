from teacher import Teacher


class Department:
    def __init__(self, name: str):
        self.__name = name
        self.__teachers: list[Teacher] = []  # Agregacion.

    def add_teacher(self, teacher: Teacher):  # Esta clase no crea profesores, los agrega.
        self.__teachers.append(teacher)

    def __str__(self):
        result = f'Departamento: {self.__name}\n'
        for teacher in self.__teachers:
            result += str(teacher) + '\n'
        return result
