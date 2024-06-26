import mysql.connector

class DatabaseSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseSingleton, cls).__new__(cls)
            cls._instance.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="HOTEL_MPC"
            )
        return cls._instance

    def get_connection(self):
        # Verificamos si la conexión fue exitosa.
        if self.connection.is_connected():
            print("_____________Conexión exitosa a la base de datos_________________")
        
        return self.connection