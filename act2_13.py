"""
Ejercicio 13 - Actividad #2
Proposito: Pedir al usuario que escriba un texto y luego solicitarle una palabra: el resultado en pantalla debe ser
indicarle al usuario cuántas veces aparece esa palabra en el texto previamente digitado.


Algoritmo: 
1. texto_completo <--- Pedir al usuario 
2. palabra <------ Pedir al usuario
3. cuantas <----- función_cuantas(palabras)
4. cuantas <----- imprimir en pantalla
"""
texto = input("Digite el texto principal:\n")
palabra = input ("Digite la palabra a buscar: \n")
cuantas = texto.count(palabra)
# print("La palabra", palabra, "se encuentra", cuantas, "veces en el texto.")
print(f"La palabra {palabra} se encuentra {cuantas} veces en el texto.")