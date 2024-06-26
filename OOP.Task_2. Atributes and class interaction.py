class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):  # Lectors, persons who teach students
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lector_atr = 'Лектор читает лекции'

class Reviewer(Mentor):  # Persons, who check homework
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.reviewer_atr = 'Проверяющие проверяют домашние задания'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

