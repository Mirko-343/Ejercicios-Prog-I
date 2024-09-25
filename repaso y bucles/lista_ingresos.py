# Mirko Becker
# Ejercicio 5

# [ 10, 15, 33, 8, 45, 16, 90, 19, 43, 54, 9, 32, 15, 6, 50, 19, 26, 65, 10, 18 ]
# a) Calcular el promedio de ingresos/hora del 20% que mas gana.
# b) Calcular el promedio de ingresos/hora de todos los respondentes.
# c) Buscar cual es el valor que mas se repite.
# d) Calcular la media geometrica

lista = [ 10, 15, 33, 8, 45, 16, 90, 19, 43, 54, 9, 32, 15, 6, 50, 19, 26, 65, 10, 18 ]

total_ingresos = 0

ingresos_mayores = []
suma_ingresos_mayores = 0

repetido = False
bandera = False
maximo = 0
minimo = 0
maximo_final = 0

contador = 0

while contador < len(lista):
    for ingreso in lista:
        total_ingresos += ingreso
        if bandera == True:
            if ingreso > maximo:
                for valor in ingresos_mayores:
                    if ingreso == valor:                        
                        repetido = True
                if repetido != True:
                    maximo = ingreso
                repetido = False
            elif ingreso < minimo:
                minimo = ingreso
        else:
            maximo = ingreso
            minimo = ingreso
            bandera = True
            
    if len(ingresos_mayores) < 4:
        ingresos_mayores.append(maximo)
        suma_ingresos_mayores += maximo
    if contador == 0:
        maximo_final = maximo
    contador += 1
    bandera = False



promedio_ingresos = total_ingresos / len(lista) # B
print(f"El maximo es {maximo_final} y el minimo {minimo}")
print(ingresos_mayores)
print(f"El promedio de ingresos/hora del 20% con mayor ingreso es de {suma_ingresos_mayores / 4}")
    
