import re 


class ChooseLesson:
    def __init__(self, id, username, password, title, teacher, code):
        self._id = id
        self._username = username
        self._password = password
        self._title = title
        self._teacher = teacher
        self._code = code

        def __str__(self):
            return f"{self._id}, {self._username}, {self._title}, {self._teacher}, {self._code}"

    def save(self):
        print("Save", self._username)

    def edit(self):
        print("Edit", self._username)

    def remove(self):
        print("Remove", self._username)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
        print("Set", self._username)
        
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if re.match(r"^[a-zA-Z0-9]{3,20}$", value):
            self._username = value
            print("Set", self._username)
        else:
            print("Invalid")

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        if re.match(r"^(?=.*[a-zA-Z]{2}.*)[a-zA-Z0-9]{6,12}$", value):
            self._password = value
            print("Set", self._username)
        else:
            print("Invalid")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if re.match(r"^[a-zA-Z0-9]{3,20}$", value):
            self._title = value
            print("Set", self._username)
        else:
            print("Invalid")


    @property
    def teacher(self):
        return self._teacher
    
    @teacher.setter
    def teacher(self, value):
        if re.match(r"^[a-zA-Z]{3,20}$", value):
            self._teacher = value
            print("Set", self._username)
        else:
            print("Invalid")

    @property
    def code(self):
        return self._code
    
    @code.setter
    def code(self, value):
        if re.match(r"^[0-9]{9,20}$", value):
            self._code = value
            print("Set", self._username)
        else:
            print("Invalid")
