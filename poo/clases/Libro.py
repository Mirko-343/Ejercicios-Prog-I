class Libro():
    def __init__(self, titulo : str, autor : str, año_publicacion : int):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        
    def mostrar_datos(self) -> None:
        print(f"Datos del libro: {self.titulo}")
        print(f"-Autor: {self.autor}")
        print(f"-Año de publicación: {self.año_publicacion}")