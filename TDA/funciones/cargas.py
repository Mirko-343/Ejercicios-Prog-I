def cargar_lista_alumnos() -> list:
    ''' Permite cargar de manera secuencial una lista de alumnos.
        Solicita al usuario 4 datos: nombre, apellido, edad y curso 
        No recibe parámetros y devuelve una lista en la que cada alumno es un diccionario '''
        
    continuar = "si"
    lista_alumnos = []

    while continuar == "si":
        tupla_curso = ()
        
        nombre = input("\nIngrese el nombre del alumno: ")
        apellido = input("Ingrese el apellido del alumno: ")
        edad = int(input("Ingrese la edad del alumno: "))
        año = (int(input("Ingrese el año en el que se encuentra el alumno: ")))
        division = (int(input("Ingrese la división en la que se encuentra el alumno: ")))
        
        tupla_auxiliar = tupla_curso + (año, division)
        
        alumno_nuevo = {"Nombre": nombre,
                        "Apellido" : apellido,
                        "Edad" : edad,
                        "Curso" : tupla_auxiliar}
        
        lista_alumnos.append(alumno_nuevo)
        
        continuar = input("¿Desea continuar cargando alumnos? (si / no): ")
        
    return lista_alumnos

# en la carga de cursos la tupla incluye la cantidad de alumnos

def cargar_cursos() -> list:
    ''' Permite cargar de manera secuencial una lista de cursos, 
        Solicita al usuario: año, división, cantidad de alumnos y el preceptor a cargo 
        No recibe ningún parámetro y devuleve una lista en la que cada curso es un diccionario '''
        
    continuar = "si"
    lista_cursos = []
    
    while continuar == "si":
        
        año = int(input("\nIngrese el año del curso: "))
        division = int(input("Ingrese la división del curso: "))
        cantidad_alumnos = int(input("Ingrese la cantidad de alumnos del curso: "))
        
        tupla_curso = (año, division, cantidad_alumnos)
        
        preceptor = input("Ingrese el nombre y apellido del preceptor a cargo del curso: ")
        
        curso_nuevo = {"Año, división y cantidad": tupla_curso,
                       "Preceptor": preceptor}
        
        lista_cursos.append(curso_nuevo)
        
        continuar = input("¿Desea continuar cargando cursos? (si / no): ")
        
    return lista_cursos

def generar_set_preceptores(lista_cursos : list) -> tuple:
    ''' Genera un set con los preceptores para cada año.
        Recibe como parámetro la lista con los datos de cada curso. 
        Devuelve una tupla con el set de cada año'''
    
    if type(lista_cursos) != list:
        print("El parámetro recibido no es del tipo correcto.")
        return None

    set_primer_año = set()
    set_segundo_año = set()
    set_tercer_año = set()

    for i in range(len(lista_cursos)):
        
        tupla_curso = lista_cursos[i]["Año, división y cantidad"]
        preceptor = lista_cursos[i]["Preceptor"]
        
        match tupla_curso[0]:           
            case 1:
                set_auxiliar = {preceptor}                
                set_primer_año = set_primer_año.union(set_auxiliar)
            case 2:
                set_auxiliar = {preceptor}
                set_segundo_año = set_segundo_año.union(set_auxiliar)
            case 3:
                set_auxiliar = {preceptor}
                set_tercer_año = set_tercer_año.union(set_auxiliar)
            case _:
                print("MARCH")
                
    return set_primer_año, set_segundo_año, set_tercer_año