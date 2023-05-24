# from student import Student
# from teacher import Teacher
# from course import Course
# from department import Department
# from university import University
#
#
# student1 = Student()
# student2 = Student()
# teacher1 = Teacher(student1)
# teacher2 = Teacher(student2)
# course1 = Course('Analsis II')
# department = Department('Ingenieria')
# university = University('Universidad Rafael Landivar')

# print(teacher1.__str__())
# print(teacher2.__str__())
# print(course1.__str__())
# print(student1)
# teacher1.teach(course1)  # Relacion de dependencia
# print(student1)

# department.add_teacher(teacher1)  # Relacion por agregación
# department.add_teacher(teacher2)
# print(department)
#
# university.add_department('Economicas', [teacher1, teacher2])
# print(university.__str__())

from dog import Dog
from bird import Bird

bird1 = Bird('Paco')
dog1 = Dog('Firulais')
dog1.walk()
