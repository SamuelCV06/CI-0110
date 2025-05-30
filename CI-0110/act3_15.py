"""
Actividad 3 - Ejercicio 15

Proposito:
Generar un archivo llamado Ejercicio 15-3 Aleatorios.txt con 10,000 números enteros aleatorios entre 1 
y 6,000,000. En el caso de que el archivo ya exista, se deben sobrescribir los números, no añadirlo

Algoritmo: 
1. Archivo <--- abrir para sobrescribir
2. lista <---- []
3. while i <= 10000 
4.1 num aleatorio <--- generara número aleatorio(1, 6000000)
4.2 numero <--- escribir al archivo
5. archivo <--- cerrar
6. imprimir <-- "Se generaron los numeros"

"""
archivo = open(r"C:\Users\C5E372\APPS\Ejercicio 15- PYTHON Manejo de archivos\Ejercicio 15-3 Aleatorios.txt", "w")
import random as rn
for i in range(10000):
    numero = rn.randint(1, 6000000)
    archivo.write(str(numero) + "\n")
   
archivo.close()
print("Numeros aleatorios generados")