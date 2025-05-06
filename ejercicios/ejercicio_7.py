#Crea un programa que guarde en un archivo los números del 1 al 10.
#Parametros de la función open
# "r" = leer, "w" = escribir, "a" = agregar
# "b" = binario, "t" = texto
# "x" = crear un nuevo archivo, "a+" = agregar y leer
# "w+" = escribir y leer, "r+" = leer y escribir
with open("numeros.txt", "w") as file:
    for i in range(1, 11):
        file.write(f"{i}\n")
# El archivo se cierra automáticamente al salir del bloque with
# El archivo se guarda en el mismo directorio donde se ejecuta el script
#Leer el archivo y mostrar su contenido
with open("numeros.txt", "r") as file:
    contenido = file.read()
    print(contenido)
# El archivo se cierra automáticamente al salir del bloque with