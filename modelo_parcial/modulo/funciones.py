def inicializar_matriz(cantidad_filas : int, cantidad_columnas : int, valor_inicial : any) -> list:
    
    matriz = []
    
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    
    return matriz
    
def generar_matriz_evento(matriz_eventos : list, salon : str) -> list:
    ''' Calcula el tipo de fiesta por salon. Recibe como parametro una matriz con:
        - id de evento en la primer fila
        - tipo de evento en la segunda fila
        - el salon del evento en la tercer fila
        Devuelve una matriz con los eventos realizados en el salon recibido como segundo parametro'''
    
    matriz_salon = inicializar_matriz(2, 4, 0)
    
    matriz_salon[0][0] = "Casamiento"
    matriz_salon[0][1] = "Bodas de Oro"
    matriz_salon[0][2] = "Fiesta de 15"
    matriz_salon[0][3] = "Cumpleanios"
    

    for i in range(len(matriz_eventos[0])):
        tipo_evento = matriz_eventos[1][i]
        if matriz_eventos[2][i] == salon:
            match tipo_evento:
                case "casamiento":
                    matriz_salon[1][0] += 1
                case "bodas de oro":
                    matriz_salon[1][1] += 1
                case "fiesta 15":
                    matriz_salon[1][2] += 1
                case "cumple":
                    matriz_salon[1][3] += 1
                
    
    return matriz_salon    

def calcular_evento_mas_realizado(matriz_salon : list, salon : str) -> str :
    ''' Caclula el evento mas realizado en cada salon. Recibe como parammetro una matriz con:
        - id de evento en la primer fila
        - tipo de evento en la segunda fila
        - el salon del evento en la tercer fila
        Como segundo parametro recibe el nombre del salon para el cual se quiere realizar la busqueda.
        Devuelve un string con el nombre del mayor evento realizado en ese salon'''
        
    
    
    for i in range(len(matriz_salon[1])):
        if i == 0:
            mayor_evento = matriz_salon[1][i]
            evento = matriz_salon[0][i]
        elif matriz_salon[1][i] > mayor_evento:
            mayor_evento = matriz_salon[1][i]
            evento = matriz_salon[0][i]
            
    return evento

def mostrar_datos_salon(matriz_salon : list, salon : str) -> list:
    ''' Muestra el detalle de eventos realizados por salon. Recibe una matriz con los datos del salon ya ordenados y
        como segundo parametro el nombre del salon para el cual se desean ver los datos. Devuelve un print con los
        resultados'''
        
    print(f"\nDatos para el salon: {salon} ----")
    print(f"{matriz_salon[0][3]}: {matriz_salon[1][3]}")
    print(f"{matriz_salon[0][2]}: {matriz_salon[1][2]}")
    print(f"{matriz_salon[0][1]}: {matriz_salon[1][1]}")
    print(f"{matriz_salon[0][0]}: {matriz_salon[1][0]}")
    
def calcular_recaudacion_salon(lista_precios : list, matriz_salon : list) -> int:
    ''' Calcula la recaudacion total por salon. Recibe como primer parametro una lista con
        los valores de cada evento. Tienen que estar ordenados de la siguiente manera:
        1. Casamiento
        2. Bodas de oro
        3. Cumple 15
        4. Cumpleanios
        Como segundo parametro recibe la matriz de eventos realizados en el salon correspondiente.
        Devuelve un entero con el valor de la recaudacion total'''
    recaudacion = 0
    for i in range(len(matriz_salon[1])):
        recaudacion += matriz_salon[1][i] * lista_precios[i]
        
    return recaudacion

def calcular_casamientos_caros(matriz_salon : list, lista_precios : list) -> bool:
    ''' Calcula si un salon genero mas de 5000000 en en casamientos.
        Recibe como primer parametro la matriz del salon correspondiente.
        Como segundo parametro recibe una lista con los valores de cada fiesta ordenados de la siguiente manera:
        1. Casamiento
        2. Bodas de oro
        3. Cumple 15
        4. Cumpleanios
        Devuelve un bool. True si dicho salon genero 5m o mas y False si no lo hizo'''

    recaudacion = False
    total_casamientos = matriz_salon[1][0] * lista_precios[0]

    if total_casamientos >= 5000000:
        recaudacion = True

    return recaudacion

def calcular_porcentaje_bodas(matriz_salon : list) -> float:
    ''' Calcula el porcentaje de bodas de oro realizadas en cada salon.
        Recibe como primer parametro la matriz salon del salon correspondiente
        Devuelve un float con el porcentaje'''
        
    cantidad_bodas = 0
    total_eventos = 0
    for i in range(len(matriz_salon[1])):
        total_eventos += matriz_salon[1][i]
        if matriz_salon[0][i] == "Bodas de Oro":
            cantidad_bodas = matriz_salon[1][i]           
          
    porcentaje = (cantidad_bodas / total_eventos) * 100
    return porcentaje

def oredenar_recaudaciones(lista : list) -> list:
    ''' Ordena los elementos de la lista recibida por parametros de menor a mayor.
        Devuelve la lista ordenada. '''

    n = len(lista[0])
    
    for i in range(n):
        intercambio = False
        for j in range(n - i - 1):
            if lista[1][j] < lista[1][j + 1]:
                intercambio = True
                # Intercambio fila recaudaciones
                menor_recaudacion = lista[1][j]
                lista[1][j] = lista[1][j + 1]
                lista[1][j + 1] = menor_recaudacion
                # Intercambio fila salones
                menor_salon = lista[0][j]
                lista[0][j] = lista [0][j + 1]
                lista[0][j + 1] = menor_salon
               
        if intercambio == False:
            break
    return lista

def mostrar_recaudaciones(matriz_recaudaciones : list) -> list:
    ''' Muestra un informe de las recaudaciones de cada salon.
        Recibe como parametro una matríz que contenga los siguientes datos:
        1. En la primer fila el nombre de los salones
        2. En la segunda fila la recaudación de los mismos '''
        
    for i in range(len(matriz_recaudaciones[0])):
        print(f"Recaudación salón {matriz_recaudaciones[0][i]}: {matriz_recaudaciones[1][i]}")

def prueba_quick(lista : list) -> list:
    
    menores = []
    iguales = []
    mayores = []

    if len(lista) > 1:
        
        pivot = lista[0]
        
        for i in range(len(lista)):
            elemento_nuevo = lista[i]    
            if lista[i] > pivot:
                mayores += elemento_nuevo
            elif lista[i] == pivot:
                iguales += elemento_nuevo
            else:
                menores += elemento_nuevo
                
        return prueba_quick(mayores) + iguales + prueba_quick(menores)
    else:
        return lista

    d