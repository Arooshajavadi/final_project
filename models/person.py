import re


class Person:
    def __init__(self, id, name, family, username, password, phone):
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
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if re.match(r"^[a-z A-Z/s]{3,30}$", name):
            self._name = name

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        if re.match(r"^[a-z A-Z/s]{3,30}$", family):
            self._family = family

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if re.match(r"^[a-z A-Z/s]{3,30}$", username):
            self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        if re.match(r"^(?=.*[a-zA-Z]{2}.*)[a-zA-Z0-9]{6,12}$", password):
            self._password = password

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        if re.match(r"^[0-9]{11}$", phone):
            self._phone = phone

    def __str__(self):
        return f"{self.id} {self.name} {self.family} {self.username} {self.phone}"
