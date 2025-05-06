# Ejercicio 2: Calcular el área de un círculo
#(fórmula: `π * radio²`). Usa `radio = 5` y `π = 3.1416`.
## **4. Operadores Básicos**
#Aritméticos: `+`, `-`, `*`, `/`, `//` (división entera), `%` (módulo)
#Comparación: `==`, `!=`, `>`, `<`, `>=`, `<=`
#Lógicos: `and`, `or`, `not`

# Definición de variables
PI = 3.1416
radio = 5
area = PI * radio ** 2
# Imprimir el resultado
print(f"El área del círculo con radio {radio} es: {area}")

#Ejercicio alternativo usando la función input y operadores logicos 
# Definición de variables
PI = 3.1416
radio = float(input("Introduce el radio del círculo: "))
if radio == 0 or radio < 0:
     print("El radio debe ser un número major a cero  y positivo.")
     
else:
    area = PI * radio ** 2
    # Imprimir el resultado
    print(f"El área del círculo con radio {radio} es: {area}")

