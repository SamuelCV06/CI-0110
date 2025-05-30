"""
Ejercicio 13 - Actividad #3
Proposito:
Pedir al usuario que escriba un texto y convertirlo en una lista. Luego, desplegar el tamaño de la lista y
solicitar al usuario un valor de índice, verificando que sea menor al tamaño de la lista, y desplegar la palabra
que se encuentra en esa posición. 

Algoritmo:
1. Texto_completo <---- Pedir al usuario
2. lista <--- palabras_del_texto()
3. tamaño <-- tam_lista()
4. print <---- Indicar tamaño de lista
5. Valor_indice <----- Pedir al usuario
6- if indice <= tamaño then
6.1 print <----- lista[indice]
7. else 
7.1 print <--- "Indice invalido"
"""

texto_c = input("Digite su texto \n")
lista = texto_c.split()
tam = len(lista)
print(f"La lista tiene un tamaño de {tam}")
indice = int(input("Digite el índice deseado: \n"))

if indice <= tam:
    print (lista[indice-1])
else: 
    print("Indice invalido")
    