import Ejercicio_5.funciones as funciones
numero_1 = int(input("Por favor ingrese el primer numero"))

while not funciones.validar_rango(numero_uno, 10, 100):
    numero_uno = int(input("El numero no esta dentro del rango especificado, intente nuevamente: "))

numero_dos = int(input("Por favor ingrese el segundo numero"))

while not funciones.validar_rango(numero_dos, 10, 100):
    numero_dos = int(input("El numero no esta dentro del rango especificado, intente nuevamente: "))
    
operacion = input("Porfavor indique la operacion a realizar. Suma (s) o Resta (r): ")

match operacion:
    case "s":
        resultado = funciones.suma(numero_uno, numero_dos)
    case "r":
        resultado = funciones.resta(numero_uno, numero_dos)

print(f"El resultado de la operacion es {resultado}")




