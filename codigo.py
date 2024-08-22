"""
Fecha de creacion 13/03/2024
Hora 10:57
Autor Cristian Moyano
Contacto cmoyano@cesde.net
"""

print("Este programa compara cinco numeros")

# Solicitar los cinco números al usuario
Numero_1 = int(input("Ingrese el primer numero: "))
Numero_2 = int(input("Ingrese el segundo numero: "))
Numero_3 = int(input("Ingrese el tercer numero: "))
Numero_4 = int(input("Ingrese el cuarto numero: "))
Numero_5 = int(input("Ingrese el quinto numero: "))

# Comparaciones entre el cuarto y el quinto número
if Numero_4 > Numero_5:
    print("El cuarto numero es mayor que el quinto")
elif Numero_4 < Numero_5:
    print("El cuarto numero es menor que el quinto")
else:
    print("El cuarto numero es igual al quinto")

# Encontrar el mayor y menor de los primeros tres números
mayor = max(Numero_1, Numero_2, Numero_3)
menor = min(Numero_1, Numero_2, Numero_3)

print(f"El numero mayor entre los primeros tres es: {mayor}")
print(f"El numero menor entre los primeros tres es: {menor}")

# Comparaciones de igualdad
iguales = set([Numero_1, Numero_2, Numero_3, Numero_4, Numero_5])
if len(iguales) == 1:
    print("Todos los números son iguales")
else:
    if len(set([Numero_1, Numero_2])) < 5:
        print("El numero uno y el numero dos son iguales" if Numero_1 == Numero_2 else "", end="")
    if len(set([Numero_1, Numero_3])) < 5:
        print("El numero uno y el numero tres son iguales" if Numero_1 == Numero_3 else "", end="")
    if len(set([Numero_2, Numero_3])) < 5:
        print("El numero dos y el numero tres son iguales" if Numero_2 == Numero_3 else "", end="")
    if len(set([Numero_4, Numero_5])) < 5:
        print("El numero cuatro y el numero cinco son iguales" if Numero_4 == Numero_5 else "")

# Comparaciones adicionales para igualdad y mayor o menor
if (Numero_1 == Numero_2 == Numero_3) or (Numero_2 == Numero_3 == Numero_4) or (Numero_1 == Numero_3 == Numero_4):
    print("Hay dos o tres números iguales y al menos uno es mayor o menor que los otros")

 