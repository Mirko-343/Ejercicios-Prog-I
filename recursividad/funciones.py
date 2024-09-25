def calcular_potencia (base : int, exponente : int) -> int:
    ''' Calcula la potencia de un numero entero. Recibe como primer parametro la base y como segundo el exponente '''
    if exponente == 1:
        return base
    else:
        return base * calcular_potencia (base, exponente - 1)
    

print(calcular_potencia(4, 3))