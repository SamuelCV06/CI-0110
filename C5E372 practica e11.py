"""Ejercicio #11 - Actividad 1 
Algoritmo
1. Menos <-- Solicitar al usuario
2. mayor <-- Solicitar al usuario
3. numero <-- menor
4. while numero <= mayor
4.1 suma <-- suma + numero
4.2 numero <-- numero + 1 
5. print <-- "La sumatioria tiene un valor de ", suma" 
"""
#Inicialiso Valores
mayor = int(input("Indique el número mayor: "))
menor = int(input("Indique el número menor: "))
""" Si es un for no se ocupa el numero = menor"""
suma = 0
#Ciclo de a suma: 
for numero in range(menor, mayor + 1 ):
    suma += numero

#Imprimimos el resultado
print ("La sumatoria tiene un valor de", suma)