from typing import List
import json
from DatabaseSingleton import DatabaseSingleton
from dto.UsuarioDTO import Usuario
from dao.UsuarioDAO import UsuarioDAO

class UsuarioDAOImpl(UsuarioDAO):
    def __init__(self) -> None:
        self.db = DatabaseSingleton()
        self.queries= self.load_queries()
    
    
    def load_queries(self):
        with open('queries.json', 'r') as file:
            return json.load(file)
        

    def get_all_usuario(self) -> List[Usuario]:
        ListaUsuarios= []

        conection = self.db.get_connection()
        cursor = conection.cursor(dictionary=True)
        sql = self.queries['listar_usuarios']
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            try:
                lista = Usuario(
                    idUsuario	= int (row['ID_USUARIO']),
                    userNombre	= str (row['USER_NOMBRE']),
                    userApellido= str (row['USER_APELLIDO']),
                    userMail	= str (row['USER_EMAIL']),
                    userPass	= str (row['CONTRASENA']),
                    esAdmin		= bool(row['ES_ADMINISTRADOR'])
                )
                ListaUsuarios.append(lista)
                
            except Exception as e:
                print(f"Error al crear ListaUsuarios con row: {row}")
                print(f"Error: {e}")

        cursor.close()
        return ListaUsuarios
    
    def buscar_usuario(self,idUsuario:int) -> Usuario:
        usuario_encontrado = None
        connection = self.db.get_connection()
        cursor = connection.cursor(dictionary=True)
        
        try:
            sql = self.queries['buscar_usuario']
            #sql = "SELECT * FROM hotel_mpc.tbl_usuario WHERE ID_USUARIO = %s"
            cursor.execute(sql, (idUsuario,))
            row = cursor.fetchone()
            
            if row:
                usuario_encontrado = Usuario(
                    idUsuario	= int (row['ID_USUARIO']),
                    userNombre	= str (row['USER_NOMBRE']),
                    userApellido= str (row['USER_APELLIDO']),
                    userMail	= str (row['USER_EMAIL']),
                    userPass	= str (row['CONTRASENA']),
                    esAdmin		= bool(row['ES_ADMINISTRADOR'])
                )
        except Exception as e:
            print(f"Error al buscar el usuario: {e}")
        finally:
            cursor.close()
            connection.close()
        return usuario_encontrado