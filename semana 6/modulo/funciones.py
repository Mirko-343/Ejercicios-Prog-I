def ordenar_nombre_ascendente(lista_nombres : list, lista_edades : list) -> list:
    ''' Recibe por parametro dos listas, una de nombres y otra de edades. Ordena
        los elementos por nombre de manera ascendente.
        Devuelve las listas ordenadas '''
       
    if type(lista_nombres) != list or type(lista_edades) != list:
        print("Uno de los parametros recibidos no es del tipo correcto")
        return None
    
    n = len(lista_nombres)
    
    for i in range(n):
        intercambio = False
        
        for j in range(n - i - 1):
            if lista_nombres[j] > lista_nombres[j + 1]:
                intercambio = True
                menor_edad = lista_edades[j + 1]
                nombre_menor = lista_nombres[j + 1]
                
                lista_nombres[j + 1] = lista_nombres[j]
                lista_edades[j + 1] = lista_edades[j]
                
                lista_nombres[j] = nombre_menor
                lista_edades[j] = menor_edad
        if intercambio == False:
            break
            
    return lista_nombres, lista_edades

def ordenar_nombre_ascen_puntos_descen(lista_nombres : list, lista_puntos : list) -> list:
    ''' Recibe una lista de nombres y otra con valores numericos. Ordena ambas listas por orden
        alfabetico ascendente y si los nombres son iguales los ordena segun los puntos de manera
        descendiente.
        Devuelve ambas listas oredenadas '''
        
    if type(lista_nombres) != list or type(lista_puntos) != list:
        print("Uno de los parametros recibidos no es del tipo lista")
        return None
    
    n = len(lista_puntos)
    
    for i in range(n):
        intercambio = False
        for j in range(n - i - 1):
            if lista_puntos[j] > lista_puntos[j + 1]:
                intercambio = True
                menor = lista_puntos[j + 1]
                lista_puntos[j + 1] = lista_puntos[j]
                lista_puntos[j] = menor
        if intercambio == False:
            break
    
    return lista_puntos