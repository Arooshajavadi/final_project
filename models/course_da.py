import mysql.connector
from models.course import ChooseCourse, Course


class CourseDa:

    def connect(self):
        self.connection = mysql.connector.connect(database='course')
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=True):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save(self, person):
        self.connect()
        self.cursor.execute('INSERT INTO course (id, username, password, title, teacher, code) VALUES (%s,%s,%s,%s,%s,%s)',
                            [person.id, person.username, person.password, person.title, person.teacher, person.code])
        self.disconnect(True)

    def edit(self, person):
        self.connect()
        self.cursor.execute('UPDATE course SET username = %s, password = %s, title = %s, teacher = %s, code = %s WHERE id=%s',
                            [person.username, person.password, person.title, person.teacher, person.code, person.id])
        self.disconnect(True)

    def remove(self, id):
        self.connect()
        self.cursor.execute('DELETE FROM course WHERE id = %s', [id])
        self.disconnect(True)

    def find_all(self):
        self.connect()
        self.cursor.execute('SELECT * FROM course')
        courses = self.cursor.fetchall()
        if courses:
            course_list = []
            for course in courses:
                course_list.append(Course(*course))
            return course_list
        self.disconnect(False)

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute('SELECT * FROM course WHERE id = %s', [id])
        course = self.cursor.fetchone()
        if course:
            courses = Course(*course)
            return courses
        self.disconnect(False)

    def find_by_username(self, username):
        self.connect()
        self.cursor.execute('SELECT * FROM teacher WHERE username = %s', [username])
        course = self.cursor.fetchone()
        if course:
            courses = Course(*course)
            return courses
        self.disconnect(False)


    def find_by_code(self, code):
        self.connect()
        self.cursor.execute('SELECT * FROM course WHERE code = %s', [code])
        course = self.cursor.fetchone()
        if course:
            courses = Course(*course)
            return courses
        self.disconnect(False)