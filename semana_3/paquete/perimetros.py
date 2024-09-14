def calcular_perimetro_circulo(radio : float) -> float:
    ''' Calcula el perimetro de un circulo. Recibe como parametro el radio del mismo '''
    perimetro =  2 * 3.14 * radio
    return float(perimetro)

def calcular_perimetro_cuadrado(lado : float) -> float:
    ''' Calcula el perimetro de un cuadrado. Recibe como parametro la longitud de uno de sus lados '''
    perimetro = lado * 4
    return float(perimetro)

def calcular_perimetro_triangulo(lado_1 : float, lado_2 : float, lado_3 : float) -> float:
    ''' Calcula el perimetro de un triangulo. Recibe como parametros las longitudes de cada uno de sus lados '''
    perimetro = lado_1 + lado_2 + lado_3
    return float(perimetro)
