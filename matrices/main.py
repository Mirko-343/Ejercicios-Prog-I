from paquete import modulo

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Punto 1 resuelto
resultado = modulo.agregar_columna(matriz)
print(resultado)

# Punto 2 resuelto
modulo.imprimir_orden_matriz(matriz)

# Punto 3 resuelto
matriz_cuadrada = modulo.inicializar_matriz(4, 4, 0)
matriz_cuadrada = modulo.multiplicar_cruces(matriz_cuadrada)
print(matriz_cuadrada)

# Punto 4 resuelto
matriz_datos = [["Juan", "Ricardo", "Nahuel", "Eugenia", "Jimena"], 
                [23, 35, 34, 40, 24],
                ["Hombre", "Hombre", "Hombre", "Mujer", "Mujer"]]

media_etaria_hombres, media_etaria_mujeres = modulo.calcular_media_etaria(matriz_datos)
print(f"La meda etaria de los hombres es de {media_etaria_hombres} y la de las mujeres es de {media_etaria_mujeres}")

# Punto 5 resuelto
lista_numeros = [1, 56, 98, 7, 17, 12, 8]
media = modulo.calcular_media_lista(lista_numeros)
print(f"La media de los valores de la lista es: {media}")

# Punto 6 resuelto
lista_ingresos = [ 10, 15, 33, 8, 45, 16, 90, 19, 43, 54,
                    9, 32, 15, 6, 50, 19, 26, 65, 10, 18 ]

ingresos_menores = modulo.calcular_ingresos_menores(lista_ingresos)
print(ingresos_menores)

# Punto 7 resuelto
matriz_1 = [[4, 5],
           [1, 2]]

matriz_2 = [[2, 1],
            [2, 5]]

producto_matricial = modulo.multiplicar_matrices(matriz_1, matriz_2)
print(producto_matricial)

# Punto 8 resuelto

matriz_traspuesta = modulo.calcular_traspuesta(matriz_1)
print(matriz_traspuesta)