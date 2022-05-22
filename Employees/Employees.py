class Employees:
    def __init__(self,name,age, seniority,salary=5600):
        self.name = name
        self.age = age
        self.seniority = seniority
        self.salary = salary


    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def get_seniorty(self):
        return self.seniority

    def set_seniority(self, seniority):
        self.seniority = seniority

    def __str__(self):
        return 'name:'+str(self.name)+'  age: '+str(self.age)+' salary: '+str(self.salary)+'  vetek: '+str(self.seniority)

