"""
Ejercicio 13 - Actividad 4
CI-0110 Introducción a la computación
C5E372 Samuel Chinchilla Vásquez 
Proposito:  
Crear una lista con 15 números aleatorios entre 1 y 100, para luego pedir al usuario un número:
si el número indicado por el usuario está en la lista, el usuario “ganó” 
el juego y se le debe indicar la posición en que se encontró; si no adivina el número 
después de tres intentos, se le muestran todos los valores contenidos en la lista.

Algoritmo: 
1. lista <---- []
2. i <-- 1
3. while i <= 15 
3.1 num aleatorio <--- generara número aleatorio(1, 100)
3.2 lista <--- añadir num aleatorios
3.3 i = i + 1
4. p <-- 1
5. while p <= 3 
5.1. numero_jugador <----- pedir al usuario
5.1.1 if numero_jugador in lista then
5.1.1.1 x <-- posición en la lista
5.1.1.1.1 print <--- "Felicidades usted ha ganado con el número que se encuentra en la posición",x,"de la lista." 
5.1.1.1.1.1 break
6.1 else
6.1.1 if p < 3 then
6.1.1.1 print <-- " Su número no esta en la lista, intentelo de nuevo "
6.1.1.1.1 p <= p + 1
7.1. else
7.1.1 print <-- " Usted perdió, los números correctos son los siguientes", lista "  
"""
#Importar libreria ramdom
import random as rn
#Lista vacia
lista = []
#variables 
i = 1
p = 1
#Lleno la lista77
for i in range(15):
    N_A = rn.randint(1, 100)
    lista.append (N_A)
    i *= 1
#Pedimos el número para jugar al usuario 
#print (lista) # <----- Quitar el # del print si se complica el adivinar el número 
while p <= 3:
    n_j = int(input("Digite un número del 1 al 100 para ganar: \n"))
    if n_j in lista:
        x = lista.index(n_j)
        print (" Felicidades usted ha ganado con el número \n que se encuentra en la posición",x, "de la lista.")
        break
    #Si el número es incorrecto se le dan 2 oportunidades más al jugador
    elif p < 3 : 
        print(" Su número no esta en la lista, intentelo de nuevo")
        p +=1
    else: 
       print("Usted perdió, los números correctos son los siguientes\n", lista)
       break