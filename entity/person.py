import re


class Person:
    def __init__(self,id,name,family,username,password,phone):
        self.id = id
        self.name = name
        self.family = family
        self.username = username
        self.password = password
        self.phone = phone

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self,id):
        self._id = id

    @property
    def name(self):
        if re.match(r"^[a-z A-Z/s]{3,30}$", self._name):
            return self._name

    @name.setter
    def name(self,name):
        self._name = name

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self,family):
        self._family = family

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self,username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,password):
        self._password = password

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self,phone):
        self._phone = phone





