import mysql.connector
from models.choose_lesson import ChooseLesson

class ChoosingDa:

    def connect(self):
        self.connection = mysql.connector.connect(database="TEST")
        self.cursor = self.connection.cursor()

    
    def disconnect(self, commit=True):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    
    def save(self, person):
        self.connect()
        self.cursor.execute('INSERT INTO lesson (id, username, password, teacher, lesson) VALUES (%s, %s, %s, %s, %s)',
                             [person.id, person.username, person.password, person.teacher, person.lesson])
        self.disconnect(True)

    
    def edit(self, person):
        self.connect()
        self.cursor.execute('UPDATE lesson SET username = %s, password = %s, teacher = %s, lesson = %s WHERE id=%s',
                            [person.username, person.password, person.teacher, person.lesson])
        self.disconnect(True)

    
    def remove(self, id):
        self.connect()
        self.cursor.execute('DELETE FROM lesson WHERE id = %s', [id])
        self.disconnect(True)

