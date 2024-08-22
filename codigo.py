"""
Fecha de creacion 13/03/2024
Hora 10:57
Autor Cristian Moyano
Contacto cmoyano@cesde.net
"""

print("Este programa compara tres numeros")

Numero_1 = 0
Numero_2 = 0
Numero_3 = 0
Numero_4 = 0
Numero_5 = 0

Numero_1 = int(input("Ingrese el primer numero: "))

Numero_2 = int(input("Ingrese el segundo numero: "))

Numero_3 = int(input("Ingrese el tercer numero: "))

Numero_4 = int(input("Ingrese el tercer numero: "))

Numero_5 = int(input("Ingrese el tercer numero: "))

if Numero_4 > Numero_5:
    print("El numero es Mayor")

else: print("No Hay comparacion")     

if Numero_1 > Numero_2 and Numero_1 > Numero_3:
    print("El numero uno es mayor: ",Numero_1)

elif Numero_2 > Numero_1 and Numero_2 > Numero_3:
    print("El numero dos es mayor: ",Numero_2)

elif Numero_3 > Numero_1 and Numero_3 > Numero_2:
    print("El numero tres es mayor: ",Numero_3)


if Numero_1 < Numero_2 and Numero_1 < Numero_3:
    print("El numero uno es menor: ",Numero_1)

elif Numero_2 < Numero_1 and Numero_2 < Numero_3:
    print("El numero dos es menor: ",Numero_2)

elif Numero_3 < Numero_1 and Numero_3 < Numero_2:
    print("El numero tres es menor: ",Numero_3)


if Numero_1 == Numero_2 and Numero_1 == Numero_3:
    print("los tres numeros son iguales: ")

elif Numero_2 == Numero_3:
    print("El numero dos y el numero tres son iguales: ")

elif Numero_1 == Numero_2:
    print("El numero uno y el numero dos son iguales: ")

elif Numero_3 == Numero_1:
    print("El numero tres y el numero uno son iguales")

else: print("No hay numeros iguales")




if (Numero_1 == Numero_2)  and Numero_1 == Numero_2 > Numero_3:
    print("El numero uno y el numero dos son iguales y mayores que numero tres")

elif (Numero_1 == Numero_3) and Numero_1 == Numero_3 > Numero_2:
    print("El numero uno y el numero tres son iguales y mayores que numero dos")

elif (Numero_2 == Numero_3) and Numero_2 == Numero_3 > Numero_1:
    print("El numero dos y el numero tres son iguales y mayores que numero uno")

#else: print("No hay numeros mayores e iguales")




if (Numero_1 == Numero_2) and Numero_1 == Numero_2 < Numero_3:
    print("El numero uno y el numero dos son iguales y menores que numero tres")

elif (Numero_2 == Numero_3) and Numero_2 == Numero_3 < Numero_1:
    print("El numero dos y el numero tres son iguales y menores que numero uno")

elif (Numero_3 == Numero_1) and Numero_3 == Numero_1 < Numero_2:
    print("El numero uno y el numero tres son iguales y menores que numero dos")

#else:  print("No hay numero menores e iguales")
 