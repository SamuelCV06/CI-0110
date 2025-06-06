"""
Actividad 1_ Ejercicio 15

Proposito:
Identificar cuántas veces aparece la palabra “Bebidas” en el archivo llamado Ejercicio 15-1 Archivo A.txt
y desplegar el resultado en pantalla.

Algoritmo:
1. Abrir el archivo
2. Texto <---- Cargar los contenidos del archivo
3. Cuantas <---- Funcion__palabra ("Bebidas", texto)
4. imprimir <---- "Se encontro" + cuantas + "veces"
5. archivo <---- cerrar
"""

archivo = open(r"c:\Users\C5E372\APPS\Ejercicio 15- PYTHON Manejo de archivos\Ejercicio 15-1 Archivo A.txt")
texto = archivo.read()
cuantas = texto.count("Bebidas")
print("Se encontro", cuantas, "veces")
archivo.close()