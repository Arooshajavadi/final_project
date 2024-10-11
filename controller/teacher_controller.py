from models.teacher_da import TeacherDa
from models.teacher import Teacher


class TeacherController:
    teacher_da = TeacherDa()

    @classmethod
    def save(cls, id , name, family, username, password, phone, skill):
        try:
            teacher = Teacher(id, name, family, username, password, phone, skill)
            cls.teacher_da.save(teacher)
            return True, "saved successfully"
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, name, family, username, password, phone, skill):
        try:
            teacher = Teacher(id, name, family, username, password, phone, skill)
            cls.teacher_da.edit(teacher)
            return True, "edited successfully"
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            cls.teacher_da.remove(id)
            return True, "removed successfully"
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            return True, cls.teacher_da.find_all()
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            return True, cls.teacher_da.find_by_id(id)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_username(cls, username):
        try:
            return True, cls.teacher_da.find_by_username(username)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_username_and_password(cls, username, password):
        try:
            return True, cls.teacher_da.find_by_username_and_pass(username, password)
        except Exception as e:
            return False, str(e)
