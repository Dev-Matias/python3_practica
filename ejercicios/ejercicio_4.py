# Ejercicio 4:
#Imprime los números **pares** del 1 al 10 usando un bucle.
#se usa % para determinar si un número es par
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

#Solucion alternativa
#se usa el paso de 2 en el range
for i in range(2, 11, 2):
    print(i)

#solucion alternativa usando wile
i = 1
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1