def mostrar_numero(numero : int) -> None :
    print(numero)
   

def definir_par(numero : int) -> bool:
    if numero % 2 == 0:
        return True
    else:
        return False
    
def definir_par_validado(numero : int, desde : int, hasta : int):
    if numero < desde or numero > hasta:
        print("El numero ingresado no esta dentro del rango especificado")
    else:
        if numero % 2 == 0:
            print(True)
        else:
            print(False)