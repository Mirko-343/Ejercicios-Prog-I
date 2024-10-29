class Animal():
    
    def __init__(self, nombre : str):
        self.nombre = nombre
        

class Perro(Animal):
    
    def __init__(self, nombre : str, sonido : str) -> None:
        super().__init__(nombre)
        self.sonido = sonido
        
    def mostrar_sonido(self) -> str:
        return self.sonido


class Gato(Animal):
    
    def __init__(self, nombre : str, sonido : str) -> None:
        super().__init__(nombre)
        self.sonido = sonido
        
    def mostrar_sonido(self) -> str:
        return self.sonido