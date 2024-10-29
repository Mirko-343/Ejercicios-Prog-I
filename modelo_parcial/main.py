from modulo import funciones

lista = [7, 2, 1, 8, 9, 5, 3, 6, 6]
valores_eventos = [5000000, 130, 200, 80]


continuar = "si"
lista_id = []
tipo_eventos = []
salones = []

matriz_eventos = funciones.inicializar_matriz(3, 0, 0)

# Punto 1 resuelto
while continuar == "si":
        
    id_evento = int(input("Ingrese el id del evento: "))
    tipo_evento = input("Ingrese el tipo de evento (casamiento, bodas de oro, fiesta 15, cumple): ")
    salon = input("Ingrese el salon: ")
    
    matriz_eventos[0] = matriz_eventos[0] + [id_evento]
    matriz_eventos[1] = matriz_eventos[1] + [tipo_evento]
    matriz_eventos[2] = matriz_eventos[2] + [salon]

    continuar = input("Desea continuar cargando eventos?: ")


matriz_palermo = funciones.generar_matriz_evento(matriz_eventos, "Palermo")
matriz_madero = funciones.generar_matriz_evento(matriz_eventos, "Puerto Madero")
matriz_santelmo = funciones.generar_matriz_evento(matriz_eventos, "San Telmo")

# Punto 2 resuelto
funciones.mostrar_datos_salon(matriz_palermo, "Palermo")

# Punto 3 resuelto
mayor_evento_santelmo = funciones.calcular_evento_mas_realizado(matriz_santelmo, "San Telmo")
print(f"\nEl evento mas realizado en San Telmo fue: {mayor_evento_santelmo}")

# Punto 4 resuelto
recaudacion_palermo = funciones.calcular_recaudacion_salon(valores_eventos, matriz_palermo)
print(f"La recaudación para el salón de Palermo fue de: {recaudacion_palermo}")

# Punto 5 resuelto
print(funciones.calcular_casamientos_caros(matriz_palermo, valores_eventos))

# Punto 6 resuelta la parte de calcular el porcentaje
bodas_palermo = funciones.calcular_porcentaje_bodas(matriz_palermo)
print(f"El porcentaje de bodas de oro realizadas en Palermo fue de: ")

# Punto 7 resuelto
recaudacion_madero = funciones.calcular_recaudacion_salon(valores_eventos, matriz_madero)
recaudacion_santelmo = funciones.calcular_recaudacion_salon(valores_eventos, matriz_santelmo)
recaudacion_palermo = recaudacion_palermo

lista_recaudaciones = funciones.inicializar_matriz(2, 3, 0)


lista_recaudaciones[0][0] = "Puerto Madero"
lista_recaudaciones[0][1] = "Palermo"
lista_recaudaciones[0][2] = "San Telmo"
lista_recaudaciones[1][0] = recaudacion_madero
lista_recaudaciones[1][1] = recaudacion_palermo
lista_recaudaciones[1][2] = recaudacion_santelmo


recaudaciones_ordenadas = funciones.oredenar_recaudaciones(lista_recaudaciones)

print(f"\nRecaudaciones de los salones ordenadas de mayor a menor: ")
funciones.mostrar_recaudaciones(recaudaciones_ordenadas)
