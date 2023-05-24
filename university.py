from department import Department
from teacher import Teacher


class University:  # Relacion de composición
    def __init__(self, name: str):
        self.__name = name
        self.__departaments: list[Department] = []

        #  Se cran los departamentos
        self.__departaments.append(Department('Ingenierira'))
        self.__departaments.append(Department('Derecho'))
        self.__departaments.append(Department('Salud'))

    def __str__(self):
        result = f'Universidad: {self.__name}  \n'
        for department in self.__departaments:
            result += str(department) + '\n'
        return result

    def add_department(self, name: str, teachers: list[Teacher]):
        department = Department(name)
        for teacher in teachers:
            department.add_teacher(teacher)
        self.__departaments.append(department)
