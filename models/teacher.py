from models.person import Person


class Teacher(Person):
    def __init__(self, name, family, username, password, skill):
        Person.__init__(self, name, family, username, password)
        self._skill = skill

    @property
    def skill(self):
        return self._skill

    @skill.setter
    def skill(self, skill):
        self._skill = skill
