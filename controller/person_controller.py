from models.person_da import PersonDa
from models.person import Person


class PersonController:
    person_da = PersonDa()

    @classmethod
    def save(cls, id, name, family, username, password, phone):
        try:
            person = Person(id, name, family, username, password, phone)
            (cls.person_da.save(person))
            return True, "saved successfully"
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, name, family, username, password, phone):
        try:
            person = Person(id, name, family, username, password, phone)
            (cls.person_da.edit(person))
            return True, "edited successfully"
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            (cls.person_da.remove(id))
            return True, "removed successfully"
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            return (True, cls.person_da.find_all())
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            return (True, cls.person_da.find_by_id(id))
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_username(cls, username):
        try:
            return True, cls.person_da.find_by_username(username)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_username_and_pass(cls, username, password):
        try:
            return True, cls.person_da.find_by_username_and_pass(username, password)
        except Exception as e:
            return False, str(e)
