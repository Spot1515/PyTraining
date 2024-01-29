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

    def __enter__(self):
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

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed")


   
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
    
    def get_user_v2(self, user_id):
        print(f"db_connection: {self.db_connection}| user_id: {user_id}")

        with self.db_connection:
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
    
    def get_all_user(self):
        cursor = self.db_connection.connection.cursor()
        query = """
                SELECT 
                    * 
                FROM 
                    User 
                """
        cursor.execute(query)
        result = cursor.fetchall()
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

    def get_user(self, user_id):
        return [self.user_id, self.name, self.email]







#this is the main start when running the file ite self
def main():
    print('\nstarting program\n')
    db = DatabaseConnection('localhost', 'testdatabase', 'test', 'Test123')

    orginal_test = 1
    if orginal_test == 1:
    
        db.connect()

        user_dao = UserDAO(db)
    
        #holders the 
        user = user_dao.get_user(1)
        print(user)
        db.disconnect()

    test2 = 0
    if test2 == 1:
        db.connect()
        user_dao = UserDAO(db)
        users_data = user_dao.get_all_user()
        users = [User(*data) for data in users_data]
        #for user in users:

        for user in users:
            print(f"User_id: {user.user_id} | Name: {user.name} | Email: {user.email}")
        db.disconnect()

    test3 = 0
    if test3 == 1:

        user_data = UserDAO(db)
        user = user_data.get_user_v2(1)
        user = User(user[0], user[1], user[2])
        print(user.name)
        
    test4 = 1
    if test4 == 1:
        user = UserDAO(db).get_user_v2(1)
        user = User(user[0], user[1], user[2])
        print(user.name)

            


        #user_test = User(user[0], user[1], user[2])
        #print(f"test: {user_test.get_user()}")
        #user_dao.update_user(1, 'update', 'update@test.com')
        #user = user_dao.get_user(1)




# this tells the program to run main if the program is called
    #if it is called as a method then it will not do this
if __name__ == "__main__":
    main()



