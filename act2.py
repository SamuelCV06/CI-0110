"""Ejercicio 11 - Actividad 2
Proposito: Para un rango de números enteros especificado por el usuario, indicar cuántos y cuáles son divisibles por
dos, por tres y por cinco."""
"""
Algoritmo:
1. menor <-- pedir al usuario
2. mayor <--- pedir al usuario
3. numero <--- menor
4. cuantos_2 <--- 0
5. cuantos_3 <--- 0
6. cuantos_5 <--- 0
7. lista_2 <-- []
8. lista_3 <-- []
9. lista_5 <-- []
10. while numero <= mayor
10.1. if numero MOD 2 = 0 then
10.1.1. cuantos_2 <---- cuantos_2 + 1
10.1.2. lista_2 <--- añadir número
10.2. if numero MOD 3 = 0 then
10.2.1. cuantos_3 <---- cuantos_3 + 1
10.2.2. lista_3 <--- añadir número
10.3. if numero MOD 3 = 0 then
10.3.1. cuantos_3 <---- cuantos_3 + 1
10.3.2. lista_3 <--- añadir número
10.4. numero <-- numero + 1
11. print <----- Cuántos y cuales valores son divisibles por 2
12. print <----- Cuántos y cuales valores son divisibles por 3
13. print <----- Cuántos y cuales valores son divisibles por 5
"""
#Pido valores al usuario
menor = int(input("Digite el número de menor rango deseado:"))
mayor = int(input("digite el número de mayor rango deseado:"))
numero = menor 

#Inicializar los valores
c_2, c_3, c_5 = 0, 0, 0
lista_2, lista_3, lista_5 = [], [], []

#ciclo de revision
for numero in range(menor, mayor+1): 
    #Revisión si es divisible por 2
    if numero % 2 == 0:
        c_2 += 1
        lista_2.append(numero)
    #Revisión si es divisible por 3
    if numero % 3 == 0:
        c_3 += 1
        lista_3.append(numero)
    #Revisión si es divisible por 5
    if numero % 5 == 0:
        c_5 += 5
        lista_5.append(numero)

#Imprimo los resultados en pantalla
print("Hay", c_2, "divisibles por 2:", lista_2)
print("Hay", c_3, "divisibles por 3:", lista_3)
print("Hay", c_5, "divisibles por 5:", lista_5)  


