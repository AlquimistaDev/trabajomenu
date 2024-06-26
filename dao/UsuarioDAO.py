from abc import ABC, abstractmethod
from typing import List
from dto.UsuarioDTO import Usuario

class UsuarioDAO(ABC):
    
    @abstractmethod
    def get_all_usuario(self) -> List[Usuario]:
        pass
    
    @abstractmethod
    def buscar_usuario(self,idUsuario:int):
        pass