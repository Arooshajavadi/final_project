import mysql.connector
from models.choose_lesson import Chooselesson

class ChoosingDa:

     def connect(self):
        self.connection = mysql.connector.connect(database="TEST")
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=True):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()
