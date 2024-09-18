from models.person import Person
import re


class Teacher(Person):
    def __init__(self, id, name, family, username, password, phone, skill):
        self._id = id
        self._name = name
        self._family = family
        self._username = username
        self._password = password
        self._phone = phone
        self._skill = skill

    @property
    def skill(self):
        return self._skill

    @skill.setter
    def skill(self, skill):
        if re.match('^[A-Za-z]{3,30}$', skill):
            self._skill = skill
