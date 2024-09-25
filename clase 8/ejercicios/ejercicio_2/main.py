# Resuelto

from paquete import funciones

lista_edad = [26, 45, 33, 67, 53, 59, 19, 37, 41, 32]
lista_nombres = ["Juan", "Matias", "Carla", "Susana", "Olivia", "Carlos", "Daniel", "Jimena", "Mariela", "Ignacio"]respondiente_mas_joven = funciones.identificar_mas_joven(lista_edad, lista_nombres)respondiente_mas_grande = funciones.identificar_mas_grande(lista_edad, lista_nombres)media_etaria = funciones.calcular_media_etaria(lista_edad, 40)print(f"El respondiente mas joven es {respondiente_mas_joven}")print(f"El respondiente mas grande {respondiente_mas_grande}")print(f"La media etaria de los mayores de 40 es de: {media_etaria}")funciones.detectar_mayores(lista_edad, lista_nombres, 65)