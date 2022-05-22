from Employees.Employees import Employees


class Tutors(Employees):
    def __init__(self, courses,name,age,seniority,salary=5600):
        super().__init__(name, age, seniority, salary)
        self.courses = courses

    def get_courses(self):
        return self.courses

    def set_courses(self, courses):
        self.courses = courses

    def __str__(self):
        return super().__str__()+' || ' + str(self.name)

