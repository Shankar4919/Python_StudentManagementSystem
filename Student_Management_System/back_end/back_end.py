
import mysql.connector   # mysql-connector-python model to connect with database


class Connection:
    def __init__(self):
        self.con=mysql.connector.connect(host='localhost',user='mamba',
                                         password='Edu@1234',database='model')
        self.cursor=self.con.cursor()

    def insert(self,query,values):   # insert information to database
        self.cursor.execute(query,values)
        self.con.commit()

    def update(self,query,values):   # update information of database
        self.cursor.execute(query,values)
        self.con.commit()

    def delete(self,query,values):  # delete information from database
        self.cursor.execute(query,values)
        self.con.commit()

    def select(self,query):    # select existing information from database
        self.cursor.execute(query)
        record=self.cursor.fetchall()
        self.con.commit()
        return record

    def user_login(self,query,values): # select existing information from database
        self.cursor.execute(query,values)
        record=self.cursor.fetchall()
        self.con.commit()
        return record







