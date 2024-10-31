def buscar_preceptor_repetido(tupla_preceptores : tuple) -> None:
    ''' Busca qué preceptores se encuentra repetidos en dos años distintos
        Recibe como parámetro la tupla con los datos de los preceptores 
        Devuelve un print con la información '''
    
    if type(tupla_preceptores) != tuple:
        print("El parámetro recibido no es del tipo correcto")
        return None    

    set_primer, set_segundo, set_tercero = tupla_preceptores
        
    # Buscar repetidos en Primer y Segundo año
    print(f"Los preceptores que están en el primer y segundo año son: {set_primer & set_segundo}")
    
    # Buscar repetidos en el Segundo y Tercer año
    print(f"Los preceptroes que están en el segundo y tercer año son: {set_segundo & set_tercero}")
    
    #Buscar repetidos en el Primer y Tercer año
    print(f"Los preceptores que están en el primer y tercer año son: {set_primer & set_tercero}")
    
def buscar_preceptores_unicos(tupla_preceptores : tuple, año = int) -> None:
    ''' Busca los preceptores que se encuentra únicamente en un año
        Recibe como primer parámetro la tupla con los datos de los preceptores
        Como segundo parámetro recibe el año para el cual se quiere filtrar
        Devuelve un print con la información '''
        
    if type(tupla_preceptores) != tuple:
        print("El parámetro recibido no es del tipo correcto")
        return None

    set_primer, set_segundo, set_tercero = tupla_preceptores
    
    if año == 1:
        print(f"Preceptores que se encuentran únicamente en el primer año: {set_primer - set_segundo - set_tercero}")
    elif año == 2:
        print(f"Preceptores que se encuentran únicamente en el segundo año: {set_segundo - set_primer - set_tercero}")
    elif año == 3:
        print(f"Preceptores que se encuentran únicamente en el tercer año: {set_tercero - set_primer - set_segundo}")
    else:
        print(f"El año recibido por parámetro no es válido.")
        return None
        
def buscar_alumno_mayor(lista_alumnos : list) -> dict:
    ''' Busca el alumno más grande entre todos.
        Recibe como primer parámetro la lista con los datos de los alumnos 
        Devuelve un diccionario con los datos del alumno '''
       
    bandera = True
    for i in range(len(lista_alumnos)):       
        if bandera == True:
            alumno_mayor = lista_alumnos[i]["Nombre"]
            edad_mayor = lista_alumnos[i]["Edad"]
            bandera = False            
        elif lista_alumnos[i]["Edad"] > edad_mayor:
            alumno_mayor = lista_alumnos[i]["Nombre"]
            edad_mayor = lista_alumnos[i]["Edad"]
            
    mayor = {"Nombre" : alumno_mayor, "Edad" : edad_mayor}

    return mayor