from models.student_da import StudentDa
from models.student import Student


class StudentController:
    student_da = StudentDa()

    @classmethod
    def save(cls, id, name, family, username, password, phone, grade):
        try:
            student = Student(id, name, family, username, password, phone, grade)
            cls.student_da.save(student)
            return True, "saved successfully"
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, name, family, username, password, phone, grade):
        try:
            student = Student(id, name, family, username, password, phone, grade)
            cls.student_da.edit(student)
            return True, "edited successfully"
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            cls.student_da.remove(id)
            return True, "removed successfully"
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            return True, cls.student_da.find_all()
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            return True, cls.student_da.find_by_id(id)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_username(cls, username):
        try:
            return True, cls.student_da.find_by_username(username)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_username_and_password(cls, username, password):
        try:
            return True, cls.student_da.find_by_username_and_pass(username, password)
        except Exception as e:
            return False, str(e)
