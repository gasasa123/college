from Employees.Employees import Employees

class Managers(Employees):
    def __init__(self,permission,name, age, seniority, salary=5600):
        self.permission = permission
        super().__init__(name, age, salary, seniority)

    def get_permission(self):
        return self.permission

    def set_permission(self, permission):
        self.permission = permission

    def __str__(self):
        return str(self.permission)+' '+str(self.name)+' '+str(self.age)+' '+str(self.salary)+' '+str(self.seniority)





