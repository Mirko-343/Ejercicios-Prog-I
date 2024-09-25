# Mirko Becker
# Ejercicios 1, 2, 3 y 4

nombre_encuestado = input("Ingrese el nombre del encuestado: ")
salario_encuestado = int(input("Ingrese el salario mensual del encuestado: "))
horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas la semana anterior: "))
while horas_trabajadas < 0 or horas_trabajadas > 120:
    horas_trabajadas = int(input("Las horas trabajadas deben ser entre 0 y 120. Intente nuevamente: "))

ingreso_horario = salario_encuestado / horas_trabajadas

print("\nResumen de datos del encuestado: ")
print(f"Nombre del encuestado: {nombre_encuestado} ")
print(f"Salario mensual del encuestado: {salario_encuestado}")
print(f"Horas semanales trabajadas por el encuestado: {horas_trabajadas}")
print(f"Ingreso horario del encuestado: {ingreso_horario}")