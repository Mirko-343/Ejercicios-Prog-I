class Cuenta():
    def __init__(self, titular : str, saldo : float) -> None:
        self.__titular = titular
        self.__saldo = saldo
        
    def consultar_saldo(self) -> float:
        return self.__saldo
    
    def depositar(self, monto : float) -> None:
        ''' Permite depositar dinero en la cuenta, modificando el saldo.
            Recibe como parametro el monto a depositar '''
            
        self.__saldo += monto
        print(f"El nuevo saldo luego del deposito es: {self.__saldo}")
        
    def retirar(self, monto : float) -> None:
        ''' Permite retirar dinero de la cuenta, modificando el saldo.
            Recibe como parametro el monto a retirar '''
            
        self.__saldo -= monto
        print(f"El nuevo saldo luego del retiro es: {self.__saldo}")