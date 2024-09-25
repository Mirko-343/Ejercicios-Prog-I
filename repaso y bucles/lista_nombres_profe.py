lista_edad = [26, 45, 33, 67, 53, 59, 19, 37, 41, 32]
lista_nombres = ["Juan", "Matias", "Carla", "Susana", "Olivia", "Carlos", 
                 "Daniel", "Jimena", "Mariela", "Ignacio"]

bandera = True
edad_maxima = 0
edad_minima = 0

for index in range(len(lista_edad)):
    if bandera == True:
        nombre_mayor = lista_nombres[index]
        edad_maxima = lista_edad[index]
        nombre_menor = lista_nombres[index]
        edad_minima = lista_edad[index]
        bandera = False
    else:
        if lista_edad[index] > edad_maxima:
            nombre_mayor = lista_nombres[index]
            edad_maxima = lista_edad[index]
        elif lista_edad[index] < edad_minima:
            nombre_menor = lista_nombres[index]
            edad_minima = lista_edad[index]
            edad_minima = lista_edad[index]


print(f"La edad minima es {edad_minima} y corresponde a {nombre_menor}")
print(f"La edad maxima es {edad_maxima} y corresponde a {nombre_mayor}")