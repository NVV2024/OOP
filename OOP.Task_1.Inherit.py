class Student:
  def __init__(self, name, surname, gender):
      self.name = name
      self.surname = surname
      self.gender = gender
      self.finished_courses = []
      self.courses_in_progress = []
      self.grades = {}

class Mentor:
  def __init__(self, name, surname):
      self.name = name
      self.surname = surname
      self.courses_attached = []

  def rate_hw(self, student, course, grade):
      if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
          if course in student.grades:
              student.grades[course] += [grade]
          else:
              student.grades[course] = [grade]
      else:
          return 'Ошибка'

class Lecturer(Mentor):  #Lectors, persons who teach students
  def __init__(self, name, surname):
    #Mentor.__init__(self,name, surname)
    super().__init__(name, surname)
    self.lector_atr = 'Лектор читает лекции'

class Reviewer(Mentor):  #Persons, who check homework
  def __init__(self, name, surname):
    #Mentor.__init__(self,name, surname)
    super().__init__(name, surname)
    self.reviewer_atr = 'Проверяющие проверяют домашние задания'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)

#Create lecture object and print his and parent attributes
lecturer = Lecturer('Ivan', 'Petrov')
print(lecturer.lector_atr)
print(lecturer.name)
print(lecturer.surname)
print() #Отступ строки

#Create reviewer object and print his and parent attributes
reviewer = Reviewer('Tom', 'Kruze')
print(reviewer.reviewer_atr)
print(reviewer.name)
print(reviewer.surname)

