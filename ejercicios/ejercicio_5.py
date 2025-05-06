### **Ejercicio 5:**
#Crea una lista de números y calcula su suma.
# Usa un bucle para recorrer la lista y sumar los números.

# Definición de la lista de números
numeros = [1, 2, 3, 4, 5]
#Acceso a los elementos de la lista lista[indice]
print(f"El primer número de la lista es: {numeros[0]}")
#Agregar un elemento a la lista usando append(elemento)
numeros.append(6)
print(f"El último número de la lista es: {numeros[-1]}")
#Eliminar un elemento de la lista usando remove(elemento)
numeros.remove(3)
print(f"El número 3 ha sido eliminado de la lista: {numeros}")
# Inicialización de la variable suma
suma = 0
# Bucle para recorrer la lista y sumar los números
for numero in numeros:
    suma += numero
# Imprimir el resultado
print(f"La suma de los números en la lista es: {suma}")

#Ejercicio alternativo usando un diccionario
# Definición de un diccionario de números
numeros_dict = {
    "uno": 1,
    "dos": 2,
    "tres": 3,
    "cuatro": 4,
    "cinco": 5
}
# Inicialización de la variable suma
suma_dict = 0
# Bucle para recorrer el diccionario y sumar los números
# Acceso a los elementos del diccionario usando la clave
# Se puede acceder a los valores del diccionario usando los métodos keys(), values(), get(calve) y items() 
for numero in numeros_dict.values():
    suma_dict += numero
# Imprimir el resultado
print(f"La suma de los números en el diccionario es: {suma_dict}") 
print(numeros_dict.keys()) #Imprime las claves del diccionario
print(numeros_dict.values()) #Imprime los valores del diccionario
print(numeros_dict.get("uno")) #Imprime el valor de la clave "uno"
print(numeros_dict.items()) #Imprime los elementos del diccionario

#Ejercicio alternativo usando un diccionario en un bucle while imprimiendo los elementos
# Definición de un diccionario de números
numeros_dict_while = {
    "uno": 1,
    "dos": 2,
    "tres": 3,
    "cuatro": 4,
    "cinco": 5
}
# Inicialización de la variable suma
suma_dict_while = 0
# Inicialización del índice
indice = 0
# Obtener las claves del diccionario
claves = list(numeros_dict_while.keys())
# Bucle while para recorrer el diccionario y sumar los números
while indice < len(claves):
    clave = claves[indice]
    suma_dict_while += numeros_dict_while[clave]
    indice += 1
# Imprimir el resultado
print(f"La suma de los números en el diccionario usando while es: {suma_dict_while}")