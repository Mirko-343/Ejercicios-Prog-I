# Mirko Becker
# Ejercicio 7

lista_numeros = [14, 99, 8, 15, 17, 33, 19, 24, 12, 10]

multiplos_cinco = 0

for numero in lista_numeros:
    if numero % 5 == 0:
        multiplos_cinco += 1
    if numero % 2 == 0:
        print(numero)
        
print(multiplos_cinco)
