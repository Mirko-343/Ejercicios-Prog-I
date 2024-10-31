def promediar_edad(lista_alumnos : list, año : int, division : int) -> float:
    ''' Calcula el promedio de edad de un determinado curso.
        Recibe como primer parámetro la lista con los datos de los alumnos.
        Como segundo parámetro recibe el número de año y como tercero el número de división '''
        
    cantidad_alumnos = 0
    total_edades = 0
    for i in range(len(lista_alumnos)):
        tupla_curso = lista_alumnos[i]["Curso"]
        edad_alumno = lista_alumnos[i]["Edad"]
        
        if tupla_curso[0] == año and tupla_curso[1] == division:
            total_edades += edad_alumno
            cantidad_alumnos += 1
            
    promedio_edades = total_edades / cantidad_alumnos
    
    return promedio_edades
            

            