def agregar_elementos_lista(lista : list) -> list:
    ''' Permite agregar elementos a una lista cualquiera. Como primer parametro recibe la lista. Valida que el elemento
        ingresado sea del mismo tipo que el resto en la lista'''
        
    continuar = "si"
    tipo = type(lista[0])
    print(f"La lista contiene elementos del tipo: {tipo}")
    
    while continuar == "si":
        
        match tipo:
            case tipo if str:
                nuevo_elemento = input("Ingrese el nuevo elemento de la lista: ")
            case tipo if int:
                nuevo_elemento = int(input("Ingrese el nuevo elemento de la lista: "))
            case tipo if float:
                nuevo_elemento = float(input("Ingrese el nuevo elemento de la lista: "))
        
        lista += [nuevo_elemento]
        
        continuar = input("Desea anadir mas elementos? si o no: ")
        
    return lista
