# def resolver_hanoi(fichas = 4, origen = 4, destino = 0, auxiliar = 0):
    
#     if origen == 1:
#         print("Mover el disco 1 de la pila origen a la pila destino")
    
#     if origen % 2 == 0 and origen == fichas:
#         print("Mover el primer disco de la pila origen a la pila auxiliar")
#         resolver_hanoi(fichas - 1, origen - 1, 0, 1)
#     elif origen % 2 != 0:
#         print("Mover ficha a la varilla destino")
#         resolver_hanoi(fichas - 1, origen -1, 0 , 1)


# ----------------- Intento 2 ----------------- #

def resolver_hanoi(discos : int):
    origen = discos
    destino = 0
    auxiliar = 0
    
    if origen == 1:
        return print("Mover el disco 1 de la pila origen a la pila destino")
    else:
        resolver_hanoi()
    

# Como llevar registro de lo que hay en cada pila sin usar listas?   
        