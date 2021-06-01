import mysql.connector

class Database:
    __db = None

    def __new__(self):
        if self.__db is None:
            self.__db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="unemployment_statistics"
            )
        return self.__db

