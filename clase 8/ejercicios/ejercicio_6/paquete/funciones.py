def validar_lista(desde : int, hasta : int) -> list:
    ''' Genera una lista con 10 numeros enteros que le solicita al usuario. Ademas valida que los numeros esten dentro de un 
        rango especifico. Como primer parametro pide desde donde comienza el rango de validacion y como segundo hasta donde 
        llega el mismo'''
        
    contador = 0
    lista_numeros = list()

    while contador < 10:
        numero_a_cargar = int(input(f"Ingrese un numero entre {desde} y {hasta}: "))
        while numero_a_cargar < desde or numero_a_cargar > hasta:
            numero_a_cargar = int(input(f"El numero no esta dentro del rango especificado. (Desde {desde} hasta {hasta}) Intente nuevamente: "))
        lista_numeros += [numero_a_cargar]
        contador += 1
        
    return lista_numeros
    
