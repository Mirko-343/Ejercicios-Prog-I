def calcular_area_circulo(radio : float = 3) -> float:
    ''' Calcula el area de un circulo. Recibe como parametro el radio del mismo. En caso de no recibir ningun valor, el radio sera 3 '''
    area = 3.14 * (radio ** 2)
    return float(area)

def calcular_area_cuadrado(lado : float) -> float:
    ''' Calcula el area de un cuadrado. Recibe como parametro la longitud de uno de los lados '''
    area = lado * lado
    return float(area)

def calcular_area_triangulo(base : float, altura : float) -> float:
    ''' Calcula el area de un triangulo. Recibe como primer parametro la base y como segundo la altura '''
    area = (base * altura) / 2
    return area