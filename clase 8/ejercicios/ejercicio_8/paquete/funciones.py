def verificar_tipos(lista : list) -> bool:
    ''' Verifica si los elementos de una lista son todos del mismo tipo. En caso de serlo informa el tipo, de no ser asi
        informa el tipo de cada elemento'''
        
    for i in range(len(lista)):
        for j in range(len(lista)):
            if type(lista[i]) == type(lista[j]):
                continue
            else:
                print("Hay elementos que no son del mismo tipo dentro de la lista. A continuacion el detalle:")
                for k in range(len(lista)):
                    print(f"{lista[k]} -> {type(lista[k])}")
                return False
     
    print(f"Todos los elementos son del mismo tipo: {type(lista[0])}")
    return True