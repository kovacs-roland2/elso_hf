from datetime import datetime

today = datetime.today()
year_today = today.year

class Person():
  def __init__(self, name, birth_year, gender):
    self.name = name
    self.birth_year = birth_year
    self.gender = gender

  def ask_year(self):
    return f"{self.name} is {year_today - self.birth_year} years old."

class Subject():
  def __init__(self, name, description, grade):
    self.name = name
    self.description = description
    self.grade = grade

class Student(Person):
  def __init__(self, name, birth_year, gender, average, parent_tel):
    super(Student, self).__init__(name, birth_year, gender)
    self.average = average
    self.parent_tel = parent_tel

class Teacher(Person):
    def __init__(self, name, birth_year, gender, subject, weekly_hour, wage_hour):
        super(Teacher, self).__init__(name, birth_year, gender)
        self.subject = subject
        self.weekly_hour = weekly_hour
        self.wage_hour = wage_hour

    def calculate_wage(self):
        return f"{self.name}'s monthly wage is {self.weekly_hour * self.wage_hour * 4}."

class HeadTeacher(Teacher):
  def __init__(self, name, birth_year, gender, subject, weekly_hour, wage_hour, classs):
    super(HeadTeacher, self).__init__(name, birth_year, gender, subject, weekly_hour, wage_hour)
    self.classs = classs

class Director(Teacher):
    def __init__(self, name, birth_year, gender, subject, weekly_hour, wage_hour, bonus):
        super(Director, self).__init__(name, birth_year, gender, subject, weekly_hour, wage_hour)
        self.bonus = bonus

    def calculate_wage(self):
         return f"{self.name}'s monthly wage is {self.weekly_hour * self.wage_hour * 4 + self.bonus}."


Pisti = Person('Pisti', 1996, 'Male')
print(Pisti.name)
print(Pisti.ask_year())

Józsi = Student('Józsi', 2000, 'Male', 3.6, 34435234322)
print(Józsi.name)
print(Józsi.gender)
print(Józsi.average)

Mari = Teacher('Mari', 1950, 'Female', 'Math', 10, 2000)
print(Mari.name)
print(Mari.subject)
print(Mari.wage_hour)
print(Mari.calculate_wage())

print(HeadTeacher.mro())

Kati = HeadTeacher('Kati', 1960, 'Female', 'PI', 5, 1000, '7a')
print(Kati.subject)
print(Kati.classs)
print(Kati.calculate_wage())

Roli = Director('Roli', 1970, 'Male', 'Physics', 3, 5000, 100000)
print(Roli.calculate_wage())