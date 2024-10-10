import mariadb
from models.course import Course


class CourseDa:
    def __init__(self):
        self.connect = None
        self.cursor = None

    def connect(self):
        self.connect = mariadb.connect(database='course', user='root', password='root123', host='127.0.0.1')
        self.cursor = self.connect.cursor()

    def disconnect(self, commit=True):
        if commit:
            self.connect.commit()
        self.cursor.close()
        self.connect.close()

    def save(self, person):
        self.connect()
        self.cursor.execute('INSERT INTO course.choose (id, username, password, title, teacher, code) VALUES (%s,%s,%s,%s,%s,%s)',
                            [person.id, person.username, person.password, person.title, person.teacher, person.code])
        self.disconnect(True)

    def edit(self, person):
        self.connect()
        self.cursor.execute('UPDATE course.choose SET username = %s, password = %s, title = %s, teacher = %s, code = %s WHERE id=%s',
                            [person.username, person.password, person.title, person.teacher, person.code, person.id])
        self.disconnect(True)

    def remove(self, id):
        self.connect()
        self.cursor.execute('DELETE FROM course.choose WHERE id = %s', [id])
        self.disconnect(True)

    def find_all(self):
        self.connect()
        self.cursor.execute('SELECT * FROM course.choose')
        courses = self.cursor.fetchall()
        if courses:
            course_list = []
            for course in courses:
                course_list.append(Course(*course))
            return course_list
        self.disconnect(False)

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute('SELECT * FROM course.choose WHERE id = %s', [id])
        course = self.cursor.fetchone()
        if course:
            courses = Course(*course)
            return courses
        self.disconnect(False)

    def find_by_username(self, username):
        self.connect()
        self.cursor.execute('SELECT * FROM course.choose WHERE username = %s', [username])
        course = self.cursor.fetchone()
        if course:
            courses = Course(*course)
            return courses
        self.disconnect(False)


    def find_by_code(self, code):
        self.connect()
        self.cursor.execute('SELECT * FROM course.choose WHERE code = %s', [code])
        course = self.cursor.fetchone()
        if course:
            courses = Course(*course)
            return courses
        self.disconnect(False)