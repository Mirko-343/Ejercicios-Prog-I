numero_uno = int(input("Por favor ingrese un numero: "))
while numero_uno < 10 or numero_uno > 100:
    numero_uno = int(input("El numero debe estar entre 10 y 100. Intente nuevamente: "))
    
def realizar_descuento(numero):
    resultado = numero - (numero * 0.05)
    return resultado

print(f"El numero luego del descuento es: {realizar_descuento(numero_uno)}")
