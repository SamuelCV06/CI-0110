"""
Imprimir en pantalla las tablas de multiplicar (incluye valores multiplicados desde el 1 hasta el 12),
 según el reango de las tablas especificado por el usuario. cada tabla debe tener un encabezado y en 
  cada fila se imprime el resultado de una multiplicación. Por ejemplo: 1 x 2 = 2
"""
""" 
tabla_1 <----- solicitar al usuario
tabla_2 <----- solicitar al usario
numero <---- tabla_1
mult <= 0
multi_maximo <= 12
multi_minimo <= 0
for numero in range(numero, tabla_2, multi_maximo + 1)
multi *= numero
if multi <-- 0
print tabla range(numero, tabla_2, multi_maximo)
multi += 1
print (multi) 
print ("son los valores de las tablas selecionadas)
"""

#PEDIR LOS NUMEROS PARA LAS TABLAS

tabla_1 = int(input("Selecciones el numero menor del rango deseado:"))
tabla_2 = int(input("Selecciones el numero mayor del rango deseado:"))
numero = tabla_1
Mult_max = 12
Mult_min = 0
print("Estos son las tablas de los valores selecionados")
while  numero < tabla_2 + 1 and Mult_min != Mult_max + 1 : 
    try:
      if Mult_min == 0: print ("Tabla del", numero,":")
      print( numero, "x", Mult_min, "=", numero * Mult_min )
      Mult_min += 1
      if Mult_min == Mult_max + 1: 
          numero = numero + 1
          Mult_min = 0
          if tabla_1 == tabla_2 + 1:
            print("!Gracias por usar este programa¡")
            break
    except ValueError:
     print("Número no reconocido")