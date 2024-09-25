def buscar_menor(lista_edades : list, lista_nombres : list) -> None:
    
    bandera = False
    menor_edad = 0
    posicion_de_los_menores = list()

    for i in range(len(lista_edades)):
        if bandera == True:
            if lista_edades[i] <= menor_edad:
                menor_edad = lista_edades[i]
        else:
            menor_edad = lista_edades[i]
            bandera = True
        
            
    for j in range(len(lista_edades)):
        if lista_edades[j] == menor_edad:
            posicion_de_los_menores = posicion_de_los_menores + [j]
            
    print("Lista de las personas mas jovenes: ")
    for k in range(len(posicion_de_los_menores)):
        print(f"- {lista_nombres[posicion_de_los_menores[k]]} -> {lista_edades[posicion_de_los_menores[k]]} anos")

         
