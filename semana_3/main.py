import paquete.areas
import paquete.perimetros

figura = input("Con que figura desea trabjar? Circulo (c), cuadrado (s) o triangulo (t): ")

match figura:
    case "c":
        radio = float(input(("\nIngrese el valor del radio del circulo: ")))
        area = paquete.areas.calcular_area_circulo(radio)
        perimetro = paquete.perimetros.calcular_perimetro_circulo(radio)
        print(f"El area del circulo es {area} y el perimetro {perimetro}")
    case "s":
        lado = float(input("\nIngrese el valor de un lado del circulo: "))
        area = paquete.areas.calcular_area_cuadrado(lado)
        perimetro = paquete.perimetros.calcular_perimetro_cuadrado(lado)
        print(f"El area del cuadrado es {area} y el perimetro {perimetro}")
    case "t":
        base = float(input("Ingrese el valor de la base del triangulo: "))
        altura = float(input("Ingrese el valor de la altura del triangulo: "))
        area = paquete.areas.calcular_area_triangulo(base, altura)
        lado_1 = base
        lado_2 = float(input("Ingrese el valor del segundo lado: "))
        lado_3 = float(input("Ingrese el valor del tercer lado: "))
        perimetro = paquete.perimetros.calcular_perimetro_triangulo(lado_1, lado_2, lado_3)
        print(f"El area del triangulo es {area} y el perimetro {perimetro}")

