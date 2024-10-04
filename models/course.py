import re 


class ChooseLesson:
    def __init__(self, id, username, password, teacher, lesson):
        self._id = id
        self._username = username
        self._password = password
        self._teacher = teacher
        self._lesson = lesson

        def __str__(self):
            return f"Id: {self._id}-Name: {self._name}-Family: {self._family}-Username: {self._username}-Teacher: {self._teacher}-Lesson:
            {self._lesson}"

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

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        if re.match(r"^(?=.*[a-zA-Z]{2}.*)[a-zA-Z0-9]{6,12}$", value):
            self._password = value
            print("Set", self._username)


    @property
    def teacher(self):
        return self._teacher
    
    @teacher.setter
    def teacher(self, value):
        if re.match(r"^[a-zA-Z]{3,20}$", value):
            self._teacher = value
            print("Set", self._username)

    @property
    def lesson(self):
        return self._lesson
    
    @lesson.setter
    def lesson(self, value):
        if re.match(r"^[a-zA-Z0-9]{3,20}$", value):
            self._lesson = value
            print("Set", self._username)
