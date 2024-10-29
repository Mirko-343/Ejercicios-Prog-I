class Rectangulo():
    
    def __init__(self, base : float, altura : float) -> None:
        self.base = base
        self.altura = altura
        
    def calcular_area(self) -> float:
        area = self.base * self.altura
        return area
    
    def calcular_perimetro(self) -> float:
        perimetro = (self.base + self.altura) * 2
        return perimetro