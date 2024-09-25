import mysql.connector
from models.person import Person


class PersonDa:
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
        self.cursor.execute('INSERT INTO person (name, family, username, password, phone) VALUES (%s,%s,%s,%s,%s)',
                            [person.name, person.family, person.username, person.password, person.phone])
        self.disconnect(True)

    def edit(self, person):
        self.connect()
        self.cursor.execute('UPDATE person SET name = %s, family = %s, username = %s, password = %s, phone = %s WHERE id=%s',
                            [person.name, person.family, person.username, person.password, person.phone])
        self.disconnect(True)

    def remove(self, id):
        self.connect()
        self.cursor.execute('DELETE FROM person WHERE id = %s', [id])
        self.disconnect(True)

    def find_all(self):
        self.connect()
        self.cursor.execute('SELECT * FROM person')
        persons = self.cursor.fetchall()
        if persons:
            person_list = []
            for person in persons:
                person_list.append(Person(*person))
            return person_list
        self.disconnect(False)


    def find_by_id(self, id):
        self.connect()
        self.cursor.execute('SELECT * FROM person WHERE id = %s', [id])
        person = self.cursor.fetchone()
        if person:
            persons = Person(*person)
            return persons
        self.disconnect(False)

    def find_by_username(self, username):
        self.connect()
        self.cursor.execute('SELECT * FROM person WHERE username = %s', [username])
        person = self.cursor.fetchone()
        if person:
            persons = Person(*person)
            return persons
        self.disconnect(False)

    def find_by_username_and_pass(self, username, password):
        self.connect()
        self.cursor.execute('SELECT * FROM person WHERE username = %s AND password = %s', [username, password])
        person = self.cursor.fetchone()
        if person:
            persons = Person(*person)
            return persons
        self.disconnect(False)

# connect database
