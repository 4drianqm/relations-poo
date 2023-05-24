from student import Student
from faker import Faker
from course import Course

fake = Faker()


class Teacher:
    def __init__(self, student: Student):
        self.__name: str = fake.name()
        self.__profession: str = fake.job()
        self.__student = student  # Asociacion de relaclión

    def teach(self, course: Course):  # Asociacion de dependencia (debil) y que solo es a nivel de metodos
        print(f'{self.__name}: Bienvenido {self.__student.name}')
        print(f'{self.__name}: Vamos a estudiar:  {course.syllabus}')
        self.__student.remember(course.syllabus)

    def __str__(self):
        return f'Nombre: {self.__name},Profesion: {self.__profession}'
