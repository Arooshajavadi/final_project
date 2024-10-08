import mariadb

from models.teacher import Teacher

class TeacherDa:
    def __init__(self):
        self.connect = None
        self.cursor = None

    def connect(self):
        self.connect = mariadb.connect(host='127.0.0.1', user='root', port='3306', password='root123', database='teacher')
        self.cursor = self.connect.cursor()


    def disconnect(self,commit=True):
        if commit:
            self.connect.commit()
        self.cursor.close()
        self.connect.close()

    def save(self, teacher):
        self.connect()
        self.cursor.execute('INSERT INTO teacher.profile (name, family, username, password, phone, skill) VALUES (%s,%s,%s,%s,%s,%s)',
                            [teacher.name, teacher.family, teacher.username, teacher.password, teacher.phone])
        self.disconnect(True)

    def edit(self, teacher):
        self.connect()
        self.cursor.execute('UPDATE teacher.profile SET name = %s, family = %s, username = %s, password = %s, phone = %s, skill = %s WHERE id=%s',
                            [teacher.name, teacher.family, teacher.username, teacher.password, teacher.phone, teacher.skill])
        self.disconnect(True)

    def remove(self, id):
        self.connect()
        self.cursor.execute('DELETE FROM teacher.profile WHERE id = %s', [id])
        self.disconnect(True)

    def find_all(self):
        self.connect()
        self.cursor.execute('SELECT * FROM teacher.profile')
        teachers = self.cursor.fetchall()
        if teachers:
            teacher_list = []
            for teacher in teachers:
                teacher_list.append(Teacher(*teacher))
            return teacher_list
        self.disconnect(False)


    def find_by_id(self, id):
        self.connect()
        self.cursor.execute('SELECT * FROM teacher.profile WHERE id = %s', [id])
        teacher = self.cursor.fetchone()
        if teacher:
            teachers = Teacher(*teacher)
            return teachers
        self.disconnect(False)

    def find_by_username(self, username):
        self.connect()
        self.cursor.execute('SELECT * FROM teacher.profile WHERE username = %s', [username])
        teacher = self.cursor.fetchone()
        if teacher:
            teachers = Teacher(*teacher)
            return teachers
        self.disconnect(False)

    def find_by_username_and_pass(self, username, password):
        self.connect()
        self.cursor.execute('SELECT * FROM teacher.profile WHERE username = %s AND password = %s', [username, password])
        teacher = self.cursor.fetchone()
        if teacher:
            teachers = Teacher(*teacher)
            return teachers
        self.disconnect(False)

    def find_by_skill(self, skill):
        self.connect()
        self.cursor.execute('SELECT * FROM teacher.profile WHERE skill = %s', [skill])
        teacher = self.cursor.fetchone()
        if teacher:
            teachers = Teacher(*teacher)
            return teachers
        self.disconnect(False)


