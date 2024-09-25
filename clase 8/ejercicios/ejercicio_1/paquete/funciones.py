
def calcular_ingresos_mayores(ingresos : list) -> float:
    ''' Calcula el 20% de valores mas altos de la lista que se pase por parametros '''
    
    cantidad_mayores = int(len(ingresos) * 0.2)

    repetido = False
    ingreso_mayor = 0
    bandera = False
    contador = 0
    ingresos_mayores = list()

    while contador < cantidad_mayores:     
        for i in range(len(ingresos)):
            repetido = False
            if bandera == False:
                ingreso_mayor = ingresos[i]
                bandera = True
            elif ingresos[i] > ingreso_mayor:
                for posicion in range(len(ingresos_mayores)):
                    if ingresos[i] == ingresos_mayores[posicion]:
                        repetido = True
                        continue
                if repetido != True:
                    ingreso_mayor = ingresos[i]
        
        if len(ingresos_mayores) < cantidad_mayores:
            ingresos_mayores += [ingreso_mayor]
         
        bandera = False    
        contador += 1

    return ingresos_mayores

def calcular_promedio_lista(lista : list) -> float:
    ''' Calcula el promedio de los valores que contenga una lista. Recibe como parametro la listas '''
    total = 0
    for i in range(len(lista)):       
        total += lista[i]
   
    promedio = total / len(lista)
    
    return promedio

def detectar_repetidos(lista : list) -> list:
    
    lista_repetidos = list()
    contador_repeticiones = 0
    contador_repeticiones_maximas = 0
    numeros_mas_repetidos = list()
    repetido = False

    for i in range(len(lista)): # Empiezo a recorrer la lista de numeros primera vez
        contador_repeticiones = 0 
        repetido = False
        for j in range(len(lista)): # Empiezo a recorrer la lista una seguna vez para comparar el valor en el indice i con el resto de la lista
            if lista[i] == lista[j]:
                contador_repeticiones += 1 # Por cada coincidencia que encuentre entre el numero en el indice i y el resto de la lista
                                           # le suma uno al contador de repeticiones
        if i == 0: # Si es la primera vuelta el contador de repeticiones maximo se configura por defecto con el contador del primer numero
            contador_repeticiones_maximas = contador_repeticiones
            numeros_mas_repetidos = numeros_mas_repetidos + [lista[i]]
        elif contador_repeticiones == contador_repeticiones_maximas: # Si el contador de repeticiones del numero actual iguala al contador maximo
            for k in range(len(numeros_mas_repetidos)): # Empiezo a recorrer la lista de numeros mas repetidos para ver si el que tengo ya esta ahi
                if lista[i] == numeros_mas_repetidos[k]: # Si el numero ya esta en la lista de mas repetidos lo marco como repetido
                     repetido = True
            if repetido != True: # Si el numero que igualo al que mas se repetia no esta en la lista donde los guardo recien ahi lo agrego
                numeros_mas_repetidos = numeros_mas_repetidos + [lista[i]]               
        elif contador_repeticiones > contador_repeticiones_maximas: # Si el contador de repeticiones del numero actual supera al contador maximo
                                                                    # limpio la lista de los numeros que mas se repitieron para dejar ese solo
            contador_repeticiones_maximas = contador_repeticiones
            numeros_mas_repetidos = list()
            numeros_mas_repetidos = numeros_mas_repetidos + [lista[i]]
    
       

    return(numeros_mas_repetidos)


        
def recorrer_lista(lista : list) -> list:
   ''' Recorre la lista que se pase por parametro en ambos sentidos. Primero imprime la lista ordenada y luego del reves '''
   print(lista)
   
   lista_reves = list()

   for i in range(len(lista), 0, -1):
       lista_reves = lista_reves + [lista[i - 1]]
       
   print(lista_reves)
       
def calcular_media_geometrica(lista : list) -> float:
    ''' Calcula la media geometrica de los elementos de la lista que se le pase como parametro '''
    resultado = 0

    for i in range(len(lista)):
        if i == (len(lista) - 1):
            continue
        elif i == 0:
            resultado = lista[i] * lista[i + 1]
        else:
            resultado = resultado * lista[i + 1]
   
    media = resultado ** (1 / len(lista))

    return media
        
            