"""CI-0110 Introducción a la computación
   C5E372 Samuel Chinchilla Vásquez 
   Ejercio 11, Lab 1.
"""
""" 
Instrucciones del ejercicio:
Imprimir en pantalla las tablas de multiplicar (incluye valores multiplicados desde el 1 hasta el 12),
 según el reango de las tablas especificado por el usuario. cada tabla debe tener un encabezado y en 
  cada fila se imprime el resultado de una multiplicación. Por ejemplo: 1 x 2 = 2
"""

""" Algoritmo:
tabla_1 <----- solicitar al usuario
tabla_2 <----- solicitar al usario
numero <---- tabla_1
multi_maximo <= 12
multi_minimo <= 0
print <---- "son los valores de las tablas selecionadas"
while  numero < tabla_2 + 1 and multi_minimo <!= multi_maximo + 1 
 print <-- numero, "x", multi_minimo, "=", numero * multi_minimo
multi_minimo <--- multi_minimo + 1
if multi_minimo <= multi_maximo + 1:
numero <-- numero + 1
multi_minimo <= 0
if numero <= tabla_2 + 1
break
"""
#Resultado final:
#Hice de cosas que no estan en el algoritmo porque me emocione de más(espero no este mal)
#Pequeño bucle para evitar errores
start = 1
while start == 1:
 try:
   # Se piden los número para el rango numerico
   print("¡Bienvenido al programa de creación de tablas de multiplicar según un rango númerico especificado!") 
   tabla_1 = int(input("Selecciones el numero menor del rango deseado:"))
   tabla_2 = int(input("Selecciones el numero mayor del rango deseado:"))
   numero = tabla_1
   Mult_max = 12
   Mult_min = 0
   start = 0
   if tabla_1 < tabla_2 or tabla_1 == tabla_2: print("Estos son las tablas en el rango de los valores selecionados:") 
   elif tabla_2 < tabla_1: print("Los valores escogidos no son un rango válido")   
   while  numero < tabla_2 + 1 and Mult_min != Mult_max + 1 : 
      #Se imprimen el encabezado de cada tabla, se crean las tablas y se realizan las multiplicaciones
      if Mult_min == 0: print ("Tabla del", numero,":")
      print( numero, "x", Mult_min, "=", numero * Mult_min )
      Mult_min += 1
      if Mult_min == Mult_max + 1: 
          numero = numero + 1
          Mult_min = 0
      if numero == tabla_2 + 1:
        input("Presione ¨Enter¨ para cerrar el programa")   
   break         
 except ValueError: print("Número digitado no reconocido")     
