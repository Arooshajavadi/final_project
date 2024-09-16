from entity.person import Person
import re
class Student(Person):
    def __init__(self,name,family,username,password,phone,grade):
        Person.__init__(self,name,family,username,password,phone)
        self.grade= grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self,grade):
        if re.match(r"^[0-9]{,2}$",grade):
            self._grade = grade

