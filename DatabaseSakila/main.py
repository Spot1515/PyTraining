import mysql.connector
from mysql.connector import Error
from datetime import datetime

HOSTNAME = 'localhost'
DATABASE = 'sakila'
USER = 'test'
PASSWORD = 'Test123'

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



class ActorDAO:
    def __init__(self, db_connection) -> None:
        self.db_connection = db_connection

    def get_actor(self, actor_id):
        with self.db_connection:
            cursor = self.db_connection.connection.cursor()
            query = """
                    SELECT 
                        actor_id,
                        first_name,
                        last_name,
                        last_update
                    FROM 
                        actor 
                    WHERE 
                        actor_id = %s"""
            cursor.execute(query, (actor_id,))
            result = cursor.fetchone()
            cursor.close()
        return result
    
    def get_all_actors(self):
        with self.db_connection:
            cursor = self.db_connection.connection.cursor()
            query = """
                    SELECT 
                        actor_id,
                        first_name,
                        last_name,
                        last_update
                    FROM 
                        actor 
                    """
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
        return result

    def update_actor(self, actor_id: int, first_name: str, last_name: str, last_update: datetime):
        with self.db_connection:
            cursor = self.db_connection.connection.cursor()
            query = """
                    UPDATE
                        actor
                    SET 
                        first_name = %s,
                        last_name = %s,
                        last_update = %s
                    WHERE 
                        actor_id = %s"""
            
            current_time = datetime.now()
            cursor.execute(query, (first_name, last_name, current_time, actor_id))

            updated_actor = self.get_actor(actor_id)
            if updated_actor:
                is_updated_correctly = (
                    updated_actor[1] == first_name and
                    updated_actor[2] == last_name and
                    updated_actor[3] == current_time
                )
                self.db_connection.connection.commit()
                return is_updated_correctly, updated_actor
            else:
                return False, None

            result = cursor.fetchone()
            cursor.close()
        return result   

#hold the data on the local system.
class Actor:
    def __init__(self, actor_id: int, first_name: str, last_name: str, last_update: datetime) -> None:
        self.actor_id = actor_id
        self.first_name = first_name
        self.last_name = last_name
        self.last_update = last_update

    def update_first_name(self, first_name: str):
        self.first_name = first_name

    def update_last_name(self, last_name: str):
        self.last_name = self.last_name

    def return_actor(self):
        return [self.actor_id, self.first_name, self.last_name, self.last_update]
    
    def __str__(self) -> str:
        return f"Actor(actor_id: {self.actor_id}, first_name: {self.first_name}, last_name: {self.last_name}, last_update: {self.last_update})"
    
    


def get_actor(db: DatabaseConnection, actor_id: int):
    actor = ActorDAO(db).get_actor(actor_id)
    actor = Actor(*actor)
    return actor

def get_all_actor(db: DatabaseConnection):
    actor_dao = ActorDAO(db)
    actors = actor_dao.get_all_actors()
    actor_out = []
    for actor_data in actors:
        actor_out.append(Actor(*actor_data))
        
    return actor_out


#main starting point
def main():
    print('\nstarting program\n')
    db = DatabaseConnection('localhost', 'sakila', 'test', 'Test123')

    #shows a actor on the screen
        #but does not return an object
    actor = get_actor(db, 10)

    print("\n" + str(actor) + "\n")
    actor.update_first_name("Cole")
    actor_dao = ActorDAO(db)
    print("test1")
    ans = actor_dao.update_actor(actor.actor_id, actor.first_name, actor.last_name, actor.last_update)
    for x in ans:
        print(x)



    # gets all records that are return conver to objects
        # then all object where put into a list that is returned to main
    actors = get_all_actor(db)

    for actor in actors:
        if str(actor.last_name).lower() == 'wood':
            print(str(actor))
    print()












# this tells the program to run main if the program is called
    #if it is called as a method then it will not do this
if __name__ == "__main__":
    main()