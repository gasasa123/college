class Courses():
    def __init__(self,name,hours,exam):
        self.name = name
        self.hours = hours
        self.exam = exam

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_hours(self):
        return self.hours

    def set_hours(self, hours):
        self.hours = hours

    def get_exam(self):
        return self.exam

    def set_exam(self, exam):
        self.exam = exam

    def __str__(self):
        return str(self.name)+' '+str(self.hours)+' '+str(self.exam)


