import mysql.connector
from mysql.connector import Error

#class hold database connection and related propertys
class DatabaseConnection:
    def __init__(self, host, database, user, password) -> None:
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self) -> None:
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                print("MySQL database connection successful")
        except Error as e:
            print(f"Error_MySQL: {e}")

    def disconnect(self) -> None:
        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed")


#DAO will hold all sql items to run on the database conections


class UserDAO:
    def __init__(self, db_connection) -> None:
        self.db_connection = db_connection

    def get_user(self, user_id):
        cursor = self.db_connection.connection.cursor()
        query = """
                SELECT 
                    * 
                FROM 
                    User 
                WHERE 
                    user_id = %s"""
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        cursor.close()
        return result
    
    def update_user(self, user_id, name, email):
        cursor = self.db_connection.connection.cursor()
        query = """
                UPDATE 
                    User 
                SET 
                    name = %s, 
                    email = %s 
                WHERE 
                    user_id = %s
                """
        cursor.execute(query, (name, email, user_id))
        result = cursor.fetchone()
        cursor.close()
        return result

#hold the data on the local system.
class User:
    def __init__(self, user_id, name, email) -> None:
        self.user_id = user_id
        self.name = name
        self.email = email




def past_items():

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Cat5p0t~2525",
        database="testdatabase"
        )

    mycursor = db.cursor()
    print()
    #mycursor.execute("CREATE DATABASE testdatabase")
    #value = mycursor.execute("CREATE TABLE TEST1(ID INT, NOTE VARCHAR(MAX))")
    #print(f"value: {value}")

    #mycursor.execute("CREATE TABLE Test (name VARCHAR(50), age smallint UNSIGNED, persionID int PRIMARY KEY AUTO_INCREMENT)")

    #mycursor.execute("DESCRIBE Test")
    #for x in mycursor:
    #    print(x)

    mycursor.execute("INSERT INTO Test (name, age) VALUES (%s, %s)", ("tim", 19))
    db.commit()
    mycursor.execute("select * from test")

    for x in mycursor:
        print(x)


def main():
    print('\nstarting program\n')
    db = DatabaseConnection('localhost', 'testdatabase', 'test', 'Test123')
    db.connect()

    user_dao = UserDAO(db)

    user = user_dao.get_user(1)
    print(user)

    user_dao.update_user(1, 'update', 'update@test.com')

    user = user_dao.get_user(1)
    print(user)

    db.disconnect()

if __name__ == "__main__":
    main()



