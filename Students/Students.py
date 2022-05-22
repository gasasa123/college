class Student:
    def __init__(self,id,name,age,grade1,grade2,grade3):
        self.id = id
        self.name = name
        self.age = age
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3

    def get_id(self):
        return self.id

    def set_id(self,id):
        self.id = id

    def get_nane(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_grade(self):
        return self.grade1

    def set_grade(self, grade1):
        self.grade1 = grade1

    def get_grade2(self):
        return self.grade2

    def set_grade2(self, grade2):
        self.grade2 = grade2

    def get_grade3(self):
        return self.grade3

    def set_grade3(self, grade3):
        self.grade3 = grade3

    def grade_avg(self):
        return self.grade1 + self.grade2 + self.grade3 / 3

    def pass_or_not(self):
        a = self.grade_avg()
        if a < 60:
            return "not pass"
        if a > 90:
            return "Successfully passed"
        else:
            return "pass"

    def __str__(self):
        return str(self.name)+' '+str(self.age)+' '+str(self.grade1)+' '+str(self.grade2)+' '+str(self.grade3)+' '+str((self.id))
