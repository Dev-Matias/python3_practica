# **Ejercicio 3:**
#Pide al usuario un número y determina si es **positivo, negativo o cero**.

pedir_numero = input("Introduce un número: ")
numero = float(pedir_numero)
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")