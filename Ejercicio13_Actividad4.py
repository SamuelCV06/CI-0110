"""
Ejercicio 13 - Actividad 4
CI-0110 Introducción a la computación
C5E372 Samuel Chinchilla Vásquez 
Proposito:  
Crear una lista con 15 números aleatorios entre 1 y 100, para luego pedir al usuario un número:
si el número indicado por el usuario está en la lista, el usuario “ganó” el juego y se le debe indicar la posición
en que se encontró; si no adivina el número después de tres intentos, se le muestran todos los valores
contenidos en la lista.

Algoritmo: 
1. lista <---- []
2. i <-- 1
3. while i <= 15 
3.1 num aleatorio <--- generara número aleatorio(1, 100)
3.2 lista <--- añadir num aleatorio
3.3 i = i + 1
4. while p < 3 + 1 
5. numero_jugador <----- pedir al usuario
6. if numero_jugador <= numero en lista then
6.1. print <--- "Felicidades usted gano, su numero se ubicaba en la posicion  " 
6.1.1 break
7. else 
7.1 print <-- "Intentelo de nuevo"
7.1.1 p <= p + 1
8. else
8.1 print <-- "Usted perdio, estos eran los numeros correctos", lista  
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
#Pedimos el numero al usuario
#Esta lista es solo para comprobar que funciona con los numeros correctos:
print(lista)
while p <= 31:
    n_j = int(input("Digite un número del 1 al 100 para ganar: \n"))
    if n_j in lista:
        x = lista.index(n_j)
        print ("Felicidades usted ha ganado con el numero en la posición", x)
        break
    elif p <3 : 
        print("Intentelo de nuevo")
        p +=1
    else: 
       print("Usted perdio, los nuemeros correctos eran", lista)
       break
else: 
    print("Usted perdio, los nuemeros correctos eran", lista)