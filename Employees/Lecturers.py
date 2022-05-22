#from Employees import *
from Employees.Employees import Employees


class Lecturers(Employees):
    def __init__(self, type, name, age, seniority, salary=5600):
        super().__init__(name, age, seniority, salary)
        self.type = type

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def junior_type(self):
        if self.type == 'junior':
            return self.salary + 2000
        else:
            return self.salary + 3000

    def __str__(self):
        return super().__str__()+' || ' +str(self.junior_type())+' ' + str(self.type)

