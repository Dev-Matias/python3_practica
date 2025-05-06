#Crea una función que calcule el factorial de un número (ej: `5! = 120`).
# El factorial producto de todos los números enteros positivos desde 1 hasta n.
# Por ejemplo, el factorial de 5 es 5 * 4 * 3 * 2 * 1 = 120.
#Uso de for in range(n, 0, -1) range(inicio, fin, paso)
def factorial(n):
    if n < 0:
        return "Solo numeros positivos."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(n, 0, -1):
            result *= i
            print(f"Multiplicando {result}")
        return result
# Prueba la función con diferentes valores
print(factorial(5))  # Debería imprimir 120