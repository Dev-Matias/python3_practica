# python3_practica
Tutorial básico y algo mas de Python3
Tutorial creado con IA usando DeepSeek
# **Tutorial Básico de Python con Ejercicios Prácticos** 🐍

Python es un lenguaje de programación fácil de aprender, con una sintaxis clara y versátil. Este tutorial cubre los fundamentos y ejercicios para practicar.

---

## **1. Instalación de Python**
### **En Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip
```
Verifica la instalación:
```bash
python3 --version
```

### **En Windows:**
Descarga Python desde [python.org](https://www.python.org/downloads/) y sigue el asistente de instalación.

---

## **2. Primer Programa: Hola Mundo**
Crea un archivo `hola_mundo.py`:
```python
print("¡Hola, Mundo!")
```
Ejecútalo:
```bash
python3 hola_mundo.py
```
**Salida:**
```
¡Hola, Mundo!
```

---

## **3. Variables y Tipos de Datos**
Python tiene varios tipos de datos:
- **Enteros (`int`)**: `5`, `-3`
- **Flotantes (`float`)**: `3.14`, `-0.001`
- **Cadenas (`str`)**: `"Hola"`, `'Python'`
- **Booleanos (`bool`)**: `True`, `False`

### **Ejemplo:**
```python
nombre = "Ana"
edad = 25
altura = 1.75
es_estudiante = True

print(f"{nombre} tiene {edad} años y mide {altura}m.")
```
**Salida:**
```
Ana tiene 25 años y mide 1.75m.
```

### **Ejercicio 1:**
Crea un programa que guarde tu comida favorita y su precio, luego imprímelo.
**Resuelto** [ Ejercicio 1](./ejercicios/ejercicio_1.py)

---

## **4. Operadores Básicos**
- **Aritméticos**: `+`, `-`, `*`, `/`, `//` (división entera), `%` (módulo)
- **Comparación**: `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Lógicos**: `and`, `or`, `not`

### **Ejemplo:**
```python
a = 10
b = 3

print(a + b)   # 13
print(a // b)  # 3 (división entera)
print(a == b)  # False
```

### **Ejercicio 2:**
Calcula el área de un círculo (fórmula: `π * radio²`). Usa `radio = 5` y `π = 3.1416`.

---

## **5. Condicionales (`if`, `elif`, `else`)**
### **Ejemplo:**
```python
edad = 18

if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")
```
**Salida:**
```
Mayor de edad
```

### **Ejercicio 3:**
Pide al usuario un número y determina si es **positivo, negativo o cero**.

---

## **6. Bucles (`for`, `while`)**
### **Ejemplo con `for`:**
```python
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)
```
**Salida:**
```
0
1
2
3
4
```

### **Ejemplo con `while`:**
```python
contador = 0
while contador < 3:
    print("Contador:", contador)
    contador += 1
```
**Salida:**
```
Contador: 0
Contador: 1
Contador: 2
```

### **Ejercicio 4:**
Imprime los números **pares** del 1 al 10 usando un bucle.

---

## **7. Listas y Diccionarios**
### **Listas (`list`):**
```python
frutas = ["manzana", "banana", "naranja"]
print(frutas[1])  # banana
```

### **Diccionarios (`dict`):**
```python
persona = {
    "nombre": "Carlos",
    "edad": 30,
    "ciudad": "Madrid"
}
print(persona["nombre"])  # Carlos
```

### **Ejercicio 5:**
Crea una lista de números y calcula su suma.

---

## **8. Funciones (`def`)**
### **Ejemplo:**
```python
def saludar(nombre):
    return f"¡Hola, {nombre}!"

print(saludar("Luisa"))
```
**Salida:**
```
¡Hola, Luisa!
```

### **Ejercicio 6:**
Crea una función que calcule el factorial de un número (ej: `5! = 120`).

---

## **9. Manejo de Archivos**
### **Leer un archivo:**
```python
with open("archivo.txt", "r") as f:
    contenido = f.read()
print(contenido)
```

### **Escribir en un archivo:**
```python
with open("saludo.txt", "w") as f:
    f.write("¡Hola desde Python!")
```

### **Ejercicio 7:**
Crea un programa que guarde en un archivo los números del 1 al 10.

---

## **10. Proyecto Final: Calculadora Simple**
Combina todo lo aprendido para hacer una calculadora que:
1. Pida dos números al usuario.
2. Permita elegir entre **sumar, restar, multiplicar o dividir**.
3. Muestre el resultado.