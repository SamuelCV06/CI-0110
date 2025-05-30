"""
Actividad 2 - Ejercicio 15

Proposito:
Comparar los archivos de texto llamados Ejercicio 15-2 Archivo A.txt y Ejercicio 15-2 Archivo B.txt e
indicar si ambos archivos tienen el mismo contenido o no.

Algoritmo:
1. Abrir los archivos 1 y 2
2. Texto_1 <---- Cargar los contenidos del archivo 1
3. Texto_2 <---- Cargar los contenidos del archivo 2
4. lista_1 <---- Funcion de division (texto_1)
5. lista_2 <---- Funcion de division (texto_2)
6. for lista_1 in lista 2 then
7. imprimir "Los textos tiene el mismo contenido"
8. Else 
9. imprimir "no tienen el mismo contenido"
"""

archivo_1 = open(r"c:\Users\C5E372\APPS\Ejercicio 15- PYTHON Manejo de archivos\Ejercicio 15-2 Archivo A.txt")
archivo_2 = open(r"c:\Users\C5E372\APPS\Ejercicio 15- PYTHON Manejo de archivos\Ejercicio 15-2 Archivo B.txt")
texto_1 = archivo_1.read()
texto_2 = archivo_2.read()
lista_1 = texto_1.split()
lista_2 = texto_2.split()
if lista_1 == lista_2:
    print("Los textos tiene el mismo contenido")
else:
    print("Los textos no tienen el mismo contenido")
archivo_1.close()
archivo_2.close()