#Calculadora simple 
# Definimos la función suma,resta,multiplicacion y division
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b
# Definimos la función calculadora
# def calculadora(a, b, operacion):
#     if operacion == "+":
#         return suma(a, b)
#     elif operacion == "-":
#         return resta(a, b)
#     elif operacion == "*":
#         return multiplicacion(a, b)
#     elif operacion == "/":
#         return division(a, b)
#     else:
#         return "Operación no válida"
 
# Función calculadora usando un diccionario (calve, valor)
# Dicionario de operaciones, clave: operación, valor: función
operaciones = {
    "+": suma,
    "-": resta,
    "*": multiplicacion,
    "/": division
}
def calculadora(a, b, operacion):
    if operacion in operaciones:
        return operaciones[operacion](a, b)
    else:
        return "Operación no válida"

while True:
    print("Bienvenido a la calculadora")
    # Pedimos al usuario que ingrese los números y la operación
    a = int(input("Ingrese el primer número: "))
    operacion = input("Ingrese la operación (+, -, *, /): ")
    b = int(input("Ingrese el segundo número: "))
    
    # Llamamos a la función calculadora y mostramos el resultado
    resultado = calculadora(a, b, operacion)
    print(f"El resultado de {a} {operacion} {b} es: {resultado}")
    salir = input("¿Desea salir? (s/n): ")
    print(salir)
    if salir.lower() == "s":
        print("Gracias por usar la calculadora")
        break
    else:
        print("Volviendo a la calculadora")


