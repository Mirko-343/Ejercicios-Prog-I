def inicializar_matriz(cantidad_filas : int, cantidad_columnas : int, valor_inicial : any) -> list:
    ''' inicializar una matriz. El primer parmetro es un entero que representa la cantidad de filas, el segundo es otro entero que representa la cantidad
        de columnas y el ultimo parametro puede ser de cualquier tipo y servira para completar los indices de la nueva matriz'''

    matriz = []
    
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    
    return matriz

def agregar_columna(matriz : list) -> list:
    ''' Agrega una columna a la matriz recibida por parametro '''
    
    if type(matriz) != list:
        print("El parametro recibido no es del tipo lista")
        return None
    
    for i in range(len(matriz)):
        matriz[i] += [0]
        
    return matriz

def imprimir_orden_matriz(matriz : list) -> None:
    ''' Muestra por pantalla el orden de la matriz que se pase como parametro '''
    
    if type(matriz) != list:
        print("La variable enviada como parametro no es del tipo lista")
        return None

    filas = len(matriz)
    columnas = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            columnas += 1
        break
    
    print(f"La lista tiene {filas} filas y {columnas} columnas")
    
def multiplicar_cruces(matriz : list) -> list:
    ''' Completa los elementos de una matriz que se pase por parametro con la multiplicacion entre los indices de ese elemento '''
    
    if type(matriz) != list:
        print("El elemento recibido como parametro no es una lista")
        return None

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = i * j
         
    return matriz

def calcular_media_etaria(matriz : list) -> float:
    ''' Calcula la media etaria de hombres y mujeres que esten en una matriz que recibe como parametro. La matriz debe tener una primer fila con los nombres,
        una segunda fila con las edades y una tercer fila con el sexo de la persona '''
    
    if type(matriz) != list:
        print("El elemento recibido como parametro no es una lista")
        return None

    total_edad_hombres = 0
    total_edad_mujeres = 0
    cantidad_hombres = 0
    cantidad_mujeres = 0

    for i in range(len(matriz)):
        if i == 2:
            for j in range(len(matriz[i])):
                if matriz[i][j] == "Hombre":
                    total_edad_hombres += matriz[i - 1][j]
                    cantidad_hombres += 1
                elif matriz[i][j] == "Mujer":
                    total_edad_mujeres += matriz[i - 1][j]
                    cantidad_mujeres += 1
    
    media_etaria_mujeres = total_edad_mujeres / cantidad_mujeres
    media_etaria_hombres = total_edad_hombres / cantidad_hombres
    
    return media_etaria_hombres, media_etaria_mujeres

def calcular_media_lista(lista : list) -> float:
    ''' Calcula la media de los valores de una lista que contenga numeros. Como parametro recibe la lista '''
    
    if type(lista[0]) != float and type(lista[0]) != int:
        print("La lista recibida no contine numeros")
        return None
    
    total_numeros = 0
    
    for i in range(len(lista)):
        total_numeros += lista[i]
        
    media = total_numeros / len(lista)
    return media

def calcular_ingresos_menores(ingresos : list) -> float:
    ''' Calcula el 20% de valores mas bajos de la lista que se pase por parametros '''
    
    if type(ingresos) != list:
        print("La variable recibida por parametros no es del tipo correcto")
        return None

    cantidad_menores = int(len(ingresos) * 0.2)

    repetido = False
    ingreso_menor = 0
    bandera = False
    contador = 0
    ingresos_menores = list()

    while contador < cantidad_menores:     
        for i in range(len(ingresos)):
            repetido = False
            if bandera == False:
                ingreso_menor = ingresos[i]
                bandera = True
            elif ingresos[i] < ingreso_menor:
                for posicion in range(len(ingresos_menores)):
                    if ingresos[i] == ingresos_menores[posicion]:
                        repetido = True
                        continue
                if repetido != True:
                    ingreso_menor = ingresos[i]
        
        if len(ingresos_menores) < cantidad_menores:
            ingresos_menores += [ingreso_menor]
         
        bandera = False    
        contador += 1

    return ingresos_menores

def inicializar_matriz(cantidad_filas : int, cantidad_columnas : int, valor_inicial : any) -> list:
    ''' Inicializa una matriz. El primer parametro sera la cantidad de filas, el segundo la cantidad de columnas y el tercero un valor opcional
        para completar los espacios'''
    matriz = []
    
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    
    return matriz

def multiplicar_matrices(matriz_1 : list, matriz_2 : list) -> list:
    ''' Multiplica las matrices que se pasen como parametro. Ademas verifica que se puede realizar la multiplicacion
        Devuelve la matriz resultante '''
    
    if type(matriz_1) != list or type(matriz_2) != list:
        print("Uno o mas de las variables recibidas por parametros no son matrices")
        return None

    if len(matriz_1[0]) != len(matriz_2):
        print("No es posible realizar la multilpicacion entre las matrices recibidas")
        return None
    
    matriz_resultante = []
    
    for i in range(len(matriz_1)):
        fila = [0] * len(matriz_2[0])
        matriz_resultante += [fila]

    contador = 0
    acumulador = 0

    #Usar dos variables distintas, 

    for i in range(len(matriz_1)):
        columna = 0
        contador = 0
        while contador < len(matriz_2[0]):
            acumulador = 0
            for j in range(len(matriz_1[0])):
                acumulador += matriz_1[i][j] * matriz_2[j][columna]            
            matriz_resultante[i][columna] += acumulador
            contador += 1
            columna += 1
            
    return(matriz_resultante)

def calcular_traspuesta(matriz : list) -> list:
    ''' Devuelve la traspuesta de la matriz que se pase por paramtero '''
    
    if type(matriz) != list:
        print("La variable recibida como parametro no es del tipo correcto")
        return None

    matriz_resultante = inicializar_matriz(len(matriz[0]), len(matriz), 0)

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz_resultante[j][i] = matriz[i][j]

    return matriz_resultante