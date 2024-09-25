# Resueltos 3 y 5
# Ejercicio 4 pendiente


from paquete import funciones

continuar = "si"
lista_nombres = list()
lista_sexos = list()
lista_horas_trabajadas = list()

while continuar == "si":
    nombre_respondiente = input("Por favor ingrese el nombre del nuevo respondiente: ")
    sexo_respondiente = input("Por favor ingrese el sexo del respondiente: ")
    horas_trabajadas = int(input("Por favor ingrese las horas trabajadas por el respondiente: "))
        
    lista_nombres += [nombre_respondiente]
    lista_sexos += [sexo_respondiente]
    lista_horas_trabajadas += [horas_trabajadas]
        
    continuar = input("Desea agregar otro respondiente? si / no: \n")
    

funciones.corregir_valores(lista_horas_trabajadas)