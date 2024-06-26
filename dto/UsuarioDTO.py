from dataclasses import dataclass

@dataclass
class Usuario:
    idUsuario:int
    userNombre:str
    userApellido: str
    userMail: str
    userPass: str
    esAdmin: bool
    
    def __str__(self) -> str:
        return f"Usuario(idUsuario={self.idUsuario}, userNombre={self.userNombre}, userApellido={self.userApellido}, userMail={self.userMail}, userPass={self.userPass}, esAdmin={self.esAdmin})"
    