# Mirko Becker
# Ejercicio 6

from turtle import pos


lista_edad = [26, 45, 33, 67, 53, 59, 19, 37, 41, 32]
lista_nombres = ["Juan", "Matias", "Carla", "Susana", "Olivia", "Carlos", "Daniel", "Jimena", "Mariela", "Ignacio"]

lista_varones = []
lista_mujeres = []
edad_mujeres = 0
edad_varones = 0

suma_mayores = 0
contador_mayores = 0

maximo = 0
minimo = 0
bandera = False

contador_nombre = 1

for posicion in range(len(lista_nombres)):
    if bandera == True:
        if lista_edad[posicion] > maximo:
            maximo = lista_edad[posicion]
            mas_grande = lista_nombres[posicion]      
        if lista_edad[posicion] < minimo:
            minimo = lista_edad[posicion]
            mas_chico = lista_nombres[posicion]
    else:
        maximo = lista_edad[posicion]
        minimo = lista_edad[posicion]
        bandera = True
        
    # if letra[len(lista_nombres[posicion])] == "a": # CoMO TOMAR EN CUENTA SOLO EL ULTIMO CARACTER?
    #     lista_mujeres += lista_nombres[posicion]
    #     edad_mujeres += lista_edad[posicion]
    # else:
    #     lista_varones += lista_nombres[posicion]
    #     edad_varones += lista_edad[posicion]
    
    for letra in lista_nombres[posicion]:
        if contador_nombre == len(lista_nombres[posicion]):
            if letra == "a":
                lista_mujeres += lista_nombres[posicion]
                edad_mujeres += lista_edad[posicion]
            else:
                lista_varones += lista_nombres[posicion]
                edad_varones += lista_edad[posicion]  
        contador_nombre += 1
        
            
    if lista_edad[posicion] >= 40:
        suma_mayores += lista_edad[posicion]
        contador_mayores += 1
        


media_edad_mujeres = edad_mujeres / len(lista_mujeres)
media_edad_varones = edad_varones / len(lista_varones)


print(lista_mujeres)
print(lista_varones)
print(f"El respondiente mas grande es {mas_grande} y el mas chico {mas_chico}")
print(f"La media etaria para varones es de {media_edad_varones} anos y para mujeres {media_edad_mujeres} anos")
print(f"La media etaria para mayores de 40 anos es de {suma_mayores / contador_mayores}")