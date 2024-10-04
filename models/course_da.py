import mysql.connector
from models.course import ChooseLesson


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
        self.cursor.execute('INSERT INTO lesson (name, family, username, password, phone) VALUES (%s,%s,%s,%s,%s)',
                            [person.name, person.family, person.username, person.password, person.phone])
        self.disconnect(True)

    def edit(self, person):
        self.connect()
        self.cursor.execute('UPDATE lesson SET name = %s, family = %s, username = %s, password = %s, phone = %s WHERE id=%s',
                            [person.name, person.family, person.username, person.password, person.phone])
        self.disconnect(True)

    def remove(self, id):
        self.connect()
        self.cursor.execute('DELETE FROM lesson WHERE id = %s', [id])
        self.disconnect(True)

