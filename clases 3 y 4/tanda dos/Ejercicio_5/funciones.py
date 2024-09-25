def validar_rango(numero : int, desde : int, hasta : int) -> bool:
    if numero < desde or numero > hasta:
        return False
    else:
        return True
    
def realizar_descuento(numero : int, descuento : int):
    valor_final = numero - ((numero / 100) * descuento )
    return valor_final

def suma(numero_a : float, numero_b: float):
    resultado = numero_a + numero_b
    return resultado

def resta(numero_a : float, numero_b: float):
    resultado = numero_a - numero_b
    return resultado