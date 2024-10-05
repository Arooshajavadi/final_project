from models.course_da import CourseDa
from models.course import Course


class CourseController:
    course_da = CourseDa()

    @classmethod
    def save(cls, id, username, password, title, teacher, code):
        try:
            course = Course(id, username, password, title, teacher, code)
            cls.course_da.save(course)
            return True, "saved successfully"
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, username, password, title, teacher, code):
        try:
            course = Course(id, username, password, title, teacher, code)
            cls.course_da.edit(course)
            return True, "edited successfully"
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            cls.course_da.remove(id)
            return True, "removed successfully"
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            return True, cls.course_da.find_all()
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            return True, cls.course_da.find_by_id(id)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_username(cls, username):
        try:
            return True, cls.course_da.find_by_username(username)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_code(cls, code):
        try:
            return True, cls.course_da.find_by_code(code)
        except Exception as e:
            return False, str(e)


