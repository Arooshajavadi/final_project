import mariadb
from models.student import Student

class StudentDa:
    def __init__(self):
        self.connection = mariadb.connect()
        self.cursor = self.connection.cursor()


    def connect(self):
        self.connection = mariadb.connect(database='student', user='root', password='root123', host='127.0.0.1', port=3306)
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=True):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save(self, student):
        self.connect()
        self.cursor.execute('INSERT INTO student.profile (name, family, username, password, phone, grade) VALUES (%s,%s,%s,%s,%s,%s)',
                            [student.name, student.family, student.username, student.password, student.phone, student.grade])
        self.disconnect(True)

    def edit(self, student):
        self.connect()
        self.cursor.execute('UPDATE student.profile SET name = %s, family = %s, username = %s, password = %s, phone = %s, grade = %s WHERE id=%s',
                            [student.name, student.family, student.username, student.password, student.phone, student.grade, student.id])
        self.disconnect(True)

    def remove(self, id):
        self.connect()
        self.cursor.execute('DELETE FROM student.profile WHERE id = %s', [id])
        self.disconnect(True)

    def find_all(self):
        self.connect()
        self.cursor.execute('SELECT * FROM student.profile')
        students = self.cursor.fetchall()
        if students:
            student_list = []
            for student in students:
                student.append(Student(*student))
            return student_list
        self.disconnect(False)


    def find_by_id(self, id):
        self.connect()
        self.cursor.execute('SELECT * FROM student.profile WHERE id = %s', [id])
        student = self.cursor.fetchone()
        if student:
            students = Student(*student)
            return students
        self.disconnect(False)

    def find_by_username(self, username):
        self.connect()
        self.cursor.execute('SELECT * FROM student.profile WHERE username = %s', [username])
        student = self.cursor.fetchone()
        if student:
            students = Student(*student)
            return students
        self.disconnect(False)

    def find_by_username_and_pass(self, username, password):
        self.connect()
        self.cursor.execute('SELECT * FROM student.profile WHERE username = %s AND password = %s', [username, password])
        student = self.cursor.fetchone()
        if student:
            students = Student(*student)
            return students
        self.disconnect(False)

