numero_uno = int(input("Por favor ingrese el primer numero: "))
while numero_uno < 10 or numero_uno > 100:
    numero_uno = int(input("El numero debe estar entre 10 y 100. Intente nuevamente: "))

numero_dos = int(input("Por favor ingrese el segundo numero: "))
while numero_dos < 10 or numero_dos > 100:
    numero_dos = int(input("El numero debe estar entre 10 y 100. Intente nuevamente: "))
    
operacion = input("Que operacion desea realizar? Suma (s) o Resta (r): ")
while operacion != "s" and operacion != "r":
    operacion = input("Ingreso no valido. Ingrese s (suma) o r (resta): ")
    

def restar_v4(numero_a, numero_b):
    resultado = numero_a - numero_b
    return resultado

def sumar (numero_a, numero_b):
    resultado = numero_a + numero_b
    return resultado

match operacion:
    case "r":
        print(f"El resultado de la operacion es {restar_v4(numero_uno, numero_dos)}")
    case "s":
        print(f"El resultado de la operacion es {sumar(numero_uno, numero_dos)}")
        
