from models import person_da
from models.person import Person
from models.person_da import *


class PersonController:

    def __init__(self):
        person_da = PersonDa()

    def save(self, id, name, family, username, password, phone):
        try:
            person = Person(id, name, family, username, password, phone)
            self.person_da.save(person)
            return True, "saved successfully"
        except Exception as e:
            return False, str(e)

    def edit(self, id, name, family, username, password, phone):
        try:
            person = Person(id, name, family, username, password, phone)
            self.person_da.edit(person)
            return True, "edited successfully"
        except Exception as e:
            return False, str(e)

    def remove(self, id):
        try:
            self.person_da.remove(id)
            return True, "removed successfully"
        except Exception as e:
            return False, str(e)

    def find_all(self):
        try:
            return True, self.person_da.find_all()
        except Exception as e:
            return False, str(e)

    def find_by_id(self, id):
        try:
            return True, self.person_da.find_by_id(id)
        except Exception as e:
            return False, str(e)

    def find_by_username(self, username):
        try:
            return True, self.person_da.find_by_username(username)
        except Exception as e:
            return False, str(e)

    def find_by_username_and_pass(self, username, password):
        try:
            return True, self.person_da.find_by_username_and_pass(username, password)
        except Exception as e:
            return False, str(e)
