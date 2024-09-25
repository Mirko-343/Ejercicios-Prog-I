import funciones

numero_uno = int(input("Ingrese un numero entre 10 y 100 por favor: "))

while not funciones.validar_rango(numero_uno, 10, 100):
    numero_uno = int(input("El numero no esta dentro del rango especificado, intente nuevamente: "))
    
print(f"El numero despues del descuento es:",funciones.realizar_descuento(numero_uno, 5))