# Mirko Becker
# Ejercicio 8

precio_base = 15000
precio_final = 0
recargo = 0
descuento = 0

destino = input("Ingrese el destino deseado (Bariloche/Cataratas/Mar del Plata/Cordoba): ")
estacion = input("Ingrese el periodo de vacaiones (Invierno/Primavera/Verano/Otono): ")


match estacion:
    case "Invierno":
        if destino == "Bariloche":
            recargo += 0.20
        elif destino == "Cataratas" or destino == "Cordoba":
            descuento += 0.10
        else:
            descuento += 0.20    
    case "Verano":
         if destino == "Bariloche":
            descuento += 0.20
         elif destino == "Cataratas" or destino == "Cordoba":
            recargo += 0.10
         else:
            recargo += 0.20  
    case "Otono":
         if destino == "Bariloche":
            recargo += 0.10
         if destino == "Cataratas" or destino == "Mar del Plata":
             recargo += 0.10
    case "Primavera":
        if destino == "Bariloche":
            recargo += 0.10
        if destino == "Cataratas" or destino == "Mar del Plata":
            recargo += 0.10

if recargo != 0:
    precio_final = precio_base + (precio_base * recargo)
else:
    precio_final = precio_base - (precio_base * descuento)
    
print(f"El precio final es de: {precio_final}")