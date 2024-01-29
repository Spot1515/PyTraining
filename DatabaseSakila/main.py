import mysql.connector
from mysql.connector import Error
from datetime import datetime
from random import randint

HOSTNAME = 'localhost'
DATABASE = 'sakila'
USER = 'test'
PASSWORD = 'Test123'
global_connection_id = 0

# Error Class
class UpdateError(Exception):
    """Exception raised for errors in the update process."""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

#Main database idk mabey other thigns
class DatabaseConnection:
    def __init__(self) -> None:
        global global_connection_id
        self.host = HOSTNAME
        self.database = DATABASE
        self.user = USER
        self.password = PASSWORD
        self.connection = None
        global_connection_id += 1
        self.connection_id = global_connection_id
        

    def __enter__(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                print(f"MySQL database connection successful ID: {self.connection_id}")
        except Error as e:
            print(f"Error_MySQL ID: {self.connection_id}, Error: {e}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print(f"MySQL connection is closed ID: {self.connection_id}")




#DAO Class
class ActorDAO:
    def __init__(self) -> None:
        self.db_connection = DatabaseConnection()

    def get_actor(self, actor_id: int):
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
        #is setup to return error if it fails data write validateion
            #but this processs is not setup
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
            
            current_time = get_updated_time()
            cursor.execute(query, (first_name, last_name, current_time, actor_id))
            actor_dao = ActorDAO()
            val_actor = actor_dao.get_actor(actor_id)
            print(f"pulled actor: {val_actor}")
            print(f"first_name: {val_actor[1]} | {first_name}")
            print(f"last_name: {val_actor[2]} | {last_name}")
            print(f"current_time: {val_actor[3]} | {current_time}")
            
            #updated_actor = self.get_actor(actor_id)
            if val_actor:
                check = (
                    val_actor[1] == first_name and
                    val_actor[2] == last_name and
                    val_actor[3] == current_time
                )
                if check == True:
                    error = False
                    self.db_connection.connection.commit()
                else:
                    error = True
                    self.db_connection.connection.rollback()
                    #raise UpdateError(f"Update Canaled | Data validation failed | Bad Write")
            else:
                error = True
            
            #self.db_connection.connection.commit() #test
            result = cursor.fetchone()
            cursor.close()
        return result, error   

#Object Class
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
    
#Reals Methods
def get_updated_time():
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time


#Test Items
    #for now at least
def get_actor(actor_id: int):
    actor = ActorDAO().get_actor(actor_id)
    actor = Actor(*actor)
    return actor

def get_all_actor():
    actor_dao = ActorDAO()
    actors = actor_dao.get_all_actors()
    actor_out = []
    for actor_data in actors:
        actor_out.append(Actor(*actor_data))
        
    return actor_out


#main starting point
def main():
    print('\nstarting program\n')


    #Example of and update of a actor record
    if True == True:
        #gets the orginal record
        actor = get_actor(10) 

        #print("\n" + str(actor) + "\n") 
        #Updates the Object
        actor.update_first_name("Cole")
        #start the database update process updateing off the updated object
        actor_dao = ActorDAO()
        x, error = actor_dao.update_actor(actor.actor_id, actor.first_name, actor.last_name, actor.last_update)

        print(f"return: {x}")
        print(f"error: {error}")


    # gets all records that are return conver to objects
        # then all object where put into a list that is returned to main
    test_get_all_actors = 0
    if 1 == 0:
        actors = get_all_actor()

        for actor in actors:
            if str(actor.last_name).lower() == 'wood':
                print(str(actor))
        print()












# this tells the program to run main if the program is called
    #if it is called as a method then it will not do this
if __name__ == "__main__":
    main()