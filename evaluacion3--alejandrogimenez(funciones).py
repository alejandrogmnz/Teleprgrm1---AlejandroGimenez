#Ejercicio 1: Defina una función en Python que acepte el radio y devuelve el valor del área de un círculo de esas dimensiones. (4pts)
print("Ejercicio 1. Se necesita hallar el valor del área de un círculo digitando su radio")

print()

def circunferencia():
	radio= float(input('Ingrese el valor del radio: '))
	area= 3.14*radio**2
	return area
total_circ= circunferencia()

print()

print("El área del circulo es: ", total_circ)

print()

#Ejercicio 2: Defina una función en Python que acepte 3 valores y devuelva solo el máximo de los tres. (7pts)

Valores= [15, 8, 3]

print("Ejercicio 2. Se tienen los siguientes valores, de los cuales se quiere hallar el máximo de estos", Valores)

print()

print("Se define la función 'def maximo(Valores):'")

def maximo (Valores):
	return max(Valores)
total_valores= maximo(Valores)

print()

print("El valor maximo es: ", total_valores)

print()

#Ejercicio 3: Dada una lista de enteros, defina una función en Python que devuelva la suma de solo los valores impares de dicha lista. (7pts)

import math

Lista_enteros= [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]

print("Ejercicio 3. En la siguiente lista se muestran números enteros de los cuales se necesita sumar los impares: ", Lista_enteros), print("Se le recuerda al usuario que los números impares son aquellos que no son múltiplos de 2, y que al dividirlos dan un residuo diferente a 0")

print()

def suma_impares(lista):
	suma= 0
	for numeros in lista:
		if numeros%2!= 0:
			suma= suma+numeros
	return suma

total_impares=suma_impares(Lista_enteros)

print()

print("Los números enteros impares de la lista son: ", total_impares)

print()

#Ejercicio 4: Desarrolle una función en Python que acepte una variable string como primer parámetro y la cantidad de caracteres necesarios para que el string salga centrado. No agregue caracteres al final del string. (10pts)

print("Ejercicio 4. Se solicita crear una función con una variable string junto a la cantidad de caracteres y que resulte en una string nueva que conserve la original y tenga el número de caracteres correcto para que quede centrada")

print()

def sustancia():
       liquido= 'agua'
       caracteres= len(liquido)

       liquido.rjust(caracteres+25)
       liquido_b= liquido.rjust(caracteres+25)
       return liquido_b

total_sust= sustancia()

print()

print(total_sust)
	