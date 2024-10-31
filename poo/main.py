from clases.Libro import *
from clases.Rectangulo import *
from clases.Calculadora import *
from clases.Animales import *
from clases.Cuenta_Bancaria  import *

# Punto 1
libro_1 = Libro("1984", "George Orwell", 1949)

libro_1.mostrar_datos()


# Punto 2
rectangulo_1 = Rectangulo(10, 5)
area = rectangulo_1.calcular_area()
perimetro = rectangulo_1.calcular_perimetro()

print(f"\nArea del rectángulo: {area}")
print(f"Perimetro del rectángulo: {perimetro}")

# Punto 3
cuenta_1 = Calculadora(10, 5)

resultado = cuenta_1.sumar
print(f"\nEl resultado de la operación es: {resultado()}")

# Punto 4
perro = Perro("Milo", "guau guau")
print(f"\nSonido del perro: {perro.mostrar_sonido()}")

gato = Gato("Yisus", "Miau")
print(f"Sonido del gato: {gato.mostrar_sonido()}")

# Punto 5
cuenta_1 = Cuenta("Mirko", 2100)
saldo = cuenta_1.consultar_saldo()

print(f"\nSaldo de la cuenta: {saldo}")

cuenta_1.depositar(400)
cuenta_1.retirar(500)