"""
Ejercicio 13 - Actividad 1
Proposito: Crear una lista con 10 números enteros aleatorios entre 1 y 1000 y luego imprimir en pantalla cada uno de
los números en forma separada
"""
"""
Algoritmo:
1. lista <---- []
2. i <-- 1
3. while i <= 10 
3.1 num aleatorio <--- generara número aleatorio(1, 1000)
3.2 lista <--- añadir num aleatorio
3.3 i = i + 1
4.b print <-- lista """

#Importar libreria ramdom
import random as rn
#Lista vacia
lista = []
#variable 
i = 1
#Lleno la lista
for i in range(10):
    N_A = rn.randint(1, 1000)
    lista.append (N_A)
    i *= 1
#Imprime la lista en forma separada
for x in lista:
    print (x) 
