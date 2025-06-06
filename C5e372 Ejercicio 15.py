"""
Ejercicio 15-4
CI-0110 Introducción a la computación
C5E372 Samuel Chinchilla Vásquez 
Proposito: Contar cuántos números hay en el archivo llamado Ejercicio 15-4 Archivo A.txt e indicar el
valor de la suma total de los números, el promedio de los números, cuál es el menor número del archivo y
cuál es el mayor número del archivo.

Algoritmo:
archivo <-- abrir archivo
cuantos <--- 0
sumatoria <--- 0
menor <---- 0
mayor <--- 0

while not eof #end of fle
  numero <--- leer cuantos
  cuantos <--- cuantos + 1
  sumatoria <---- sumatoria + numero
  if cuantos = 1 then
     menor = numero
     mayor = numero
  else
     if numero < menor then
         menor = mayor
     else
        if numero > mayor then
         mayor = numero  
promedo <--- sumatoria / cuantos 
print <--- Cantidad de nùmeros, sumatoria, promedio, nùmero mayor y nùmero menor

"""
archivo = open(r"C:\Users\c5e372\program\CI-0110\Ejercicio 15- PYTHON Manejo de archivos\Ejercicio 15-4 Archivo A.txt","r")
cuantos = 0
sumatoria = 0
menor = 0
mayor = 0
for numero in archivo:
 cuantos += 1
 sumatoria += int(numero)
 if cuantos == 1 :
  menor = int(numero)
  mayor = int(numero)
else:
 if int(numero) > mayor:
  mayor = int(numero)
promidio = int(sumatoria) / int(cuantos)
print(f"El archivo tiene {cuantos} números: la sumatoria total es {sumatoria}, el promedio total es {promidio},\n el número mayor es {mayor} y el menor es {menor}")  
archivo.close()