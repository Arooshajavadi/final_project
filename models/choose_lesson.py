

class ChooseLesson:
    def __init__(self, name, family, username, password, teacher, lesson):
        self._name = name
        self._family = family
        self._username = username
        self._password = password
        self._teacher = teacher
        self._lesson = lesson

        def __str__(self):
            return f"Id: {self._id}-Name: {self._name}-Family: {self._family}-Username: {self._username}-Teacher: {self._teacher}-Lesson:
            {self._lesson}"

    def save(self):
        print("Save", self._name)

    def edit(self):
        print("Edit", self._name)

    def remove(self):
        print("Remove", self._name)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
        print("Set", self._name)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        print("Set", self._name)

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, value):
        self._family = value
        print("Set", self._name)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value
        print("Set", self._name)

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        self._password = value

    @property
    def teacher(self):
        return self._teacher
    
    @teacher.setter
    def teacher(self, value):
        self._teacher = value

    @property
    def lesson(self):
        return self._lesson
    
    @lesson.setter
    def lesson(self, value):
        self._lesson = value

#write valids
