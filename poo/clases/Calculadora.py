class Calculadora():
    
    def __init__(self, numero_1 : float, numero_2 : float) -> None:
        self.numero_1 = numero_1
        self.numero_2 = numero_2
        
    def sumar(self) -> float:
        resultado = self.numero_1 + self.numero_2
        return resultado
    
    def restar(self) -> float:
        resultado = self.numero_1 - self.numero_2
        return resultado
    
    def multiplicar(self) -> float:
        resultado = self.numero_1 * self.numero_2
        return resultado
    
    def dividir(self) -> float:
        resultado = self.numero_1 / self.numero_2
        return resultado