def corregir_valores(lista : list) -> None:
    ''' Permite cambiar el valor de una posicion determinada en una lista. Como parametro recibe la lista '''
    print("\n")
    for i in range(len(lista)):        
        print(f"{i} - {lista[i]}")
    posicion = int(input("Que posicion de la lista desea modificar? "))    
    
    if type(lista[posicion]) == str:
        lista[posicion] = input("Ingrese el nuevo valor: ")
    else:
        lista[posicion] = int(input("Ingrese el nuevo valor: "))
        
    print(f"Lista luego de la modificacion: {lista}")
    

def ordenar_lista(lista : list) -> list:
    ''' Ordena de menor a mayor los valores de la lista que se pase por parametro '''


def calcular_cuartiles(lista : list):
    tama�o_cuartil = len(lista) // 4
    
    maximos = [lista[0]] * tama�o_cuartil
    minimos = [lista[0]] * tama�o_cuartil
    
