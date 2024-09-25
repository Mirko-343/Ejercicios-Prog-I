def identificar_mas_joven(lista_edades : list, lista_nombres : list) -> str:
    ''' Identifica y devuelve el nombre del respondiente mas joven. Recibe como primer parametro la lista
        con las edades y como segundo la lista con los nombres. Deben ser del mismo tamano para que funcione'''
        
    bandera = False
    for i in range(len(lista_edades)):
        if bandera == False:
            mas_joven = lista_nombres[i]
            menor_edad = lista_edades[i]
            bandera = True
        elif lista_edades[i] < menor_edad:
            mas_joven = lista_nombres[i]
            menor_edad = lista_edades[i]
            
    return mas_joven

def identificar_mas_grande(lista_edades : list, lista_nombres : list) -> str:
    ''' Identifica y devuelve el nombre del respondiente mas grande. Recibe como primer parametro la lista
        con las edades y como segundo la lista con los nombres. Deben ser del mismo tamano para que funcione'''
        
    bandera = False
    for i in range(len(lista_edades)):
        if bandera == False:
            mas_grande = lista_nombres[i]
            mayor_edad = lista_edades[i]
            bandera = True
        elif lista_edades[i] > mayor_edad:
            mas_grande = lista_nombres[i]
            mayor_edad = lista_edades[i]
            
    return mas_grande

def detectar_mayores(lista_edades : list, lista_nombres : list, edad_maxima : int) -> None:
    ''' Verifica si hay respondientes mayores a una edad determinada. Como primer parametro recibe la lista de edades
        como segundo la lista de nombres y como tercer parametro recibe el limite de edad por el que va a filtrar'''
    for i in range(len(lista_edades)):
        if lista_edades[i] > edad_maxima:
            print (f"Se ha detectado un respondiente mayor de {edad_maxima} ({lista_nombres[i]}). Ejecucion detenida")
            break
        
def calcular_media_etaria(lista_edades : list, edad_minima : int) -> float:
    ''' Calcula la media etaria para una lista de edades. Como primer parametro recibe la lista y como segundo la edad minima
        a paritr de la cual filtrar'''
        
    total_edades = 0
    contador = 0
    for i in range(len(lista_edades)):
        if lista_edades[i] < edad_minima:
            continue
        else:
            total_edades += lista_edades[i]
            contador += 1
            
    promedio = total_edades / contador
    return promedio
    