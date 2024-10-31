from funciones import cargas
from funciones import calculos
from funciones import busquedas

lista_cursos = list()
lista_alumnos = list()
preceptores = ()
continuar = "si"

while continuar == "si":
    año = 0
    division = 0
    
    print("\n1 - Carga de alumnos")
    print("2 - Carga de cursos")
    print("3 - Generar lista de preceptores")
    print("4 - Obtener promedio de edad")
    print("5 - Buscar preceptores repetidos")
    print("6 - Buscar preceptores exclusivos de algún año")
    print("7 - Buscar alumno mayor")
    opcion = int(input("Seleccione una opción para continuar: "))

    match opcion:
        case 1:
            print("\n ------ Carga de alumnos ------")
            lista_alumnos = cargas.cargar_lista_alumnos()
        case 2:
            print("\n ------ Carga de cursos ------")
            lista_cursos = cargas.cargar_cursos()
        case 3:
            if len(lista_cursos) == 0:
                print("\n ¡Primero es necesario generar una lista con los cursos!")
            else:
                preceptores = cargas.generar_set_preceptores(lista_cursos)
                print("\nListado de preceptores generado.")
        case 4:
            if len(lista_alumnos) == 0:
                print("\n ¡Primero es necesario generar una lista con los alumnos!")
            else:
                año = int(input("\nIngrese el año para el que desea calcular el promedio: "))
                division = int(input("Ingrese la división para la cual desea calcular el promedio: "))
                promedio_edad = calculos.promediar_edad(lista_alumnos, año, division)
                print(f"\nEl promedio de edad para los alumnos del año {año} división {division} es de: {promedio_edad}")
        case 5:
            if len(preceptores) == 0:
                print("\n ¡jPrimero es necesario cargar los datos de los preceptores!")
            else:
                busquedas.buscar_preceptor_repetido(preceptores)
        case 6:
            if len(preceptores) == 0:
                print("\n ¡Primero es necesario cargar los datos de los preceptores!")
            else:
                año_filtro = int((input("\nIngrese el año para el que desea filtrar: ")))
                busquedas.buscar_preceptores_unicos(preceptores, año_filtro)
        case 7:
            if len(lista_alumnos) == 0:
                print("\n ¡Primero es necesario generar una lista con los alumnos!")
            else:
                alumno_mayor = busquedas.buscar_alumno_mayor(lista_alumnos)
                print(f"Datos del alumno más grande: {alumno_mayor}")
               
    continuar = input("\n¿Desea seleccionar otra opción? (si / no): ")
    

