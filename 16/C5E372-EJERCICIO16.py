"""
Ejercicio 16
CI-0110 Introducción a la computación
C5E372 Samuel Chinchilla Vásquez 
Proposito: Una tienda está recopilando información sobre sus ventas del año anterior para un producto específico, 
para lo cual se ha generado el archivo de texto llamado Ejercicio 16-1.txt. Usted debe crear un programa 
en Python que lea el archivo recibido para, después de procesarlo, indicar los montos en colones de las 
ventas por semestre y por zona. Considere que: 
i. Siempre la primera fila del archivo corresponde a los encabezados de las columnas. 
ii. Todas las funciones deben ser creadas en un módulo que luego se importa al programa principal. 
iii. Dado que los montos vienen en euros, debe crear una función que solicite al usuario el tipo de 
cambio que desea utilizar para hacer la conversión a colones y que devuelva el valor indicado por 
el usuario en un valor numérico sin perder los posibles decimales. 
iv. Para establecer el trimestre, debe crear una función que analice el mes de la venta y devuelva el 
semestre, considerando que ventas de enero, febrero, marzo, abril, mayo y junio corresponden al 
I Semestre; y ventas de julio, agosto, setiembre, octubre, noviembre y diciembre corresponden al 
II Semestre. 
v. Para establecer la zona, debe crear una función que analice la tienda y devuelva el nombre de la 
zona, considerando que las tiendas 1, 2, 3 y 4 pertenecen a la Zona Central; las tiendas 5 y 6 
pertenecen a la Zona Sur; y las tiendas 7, 8 y 9 pertenecen a la Zona Norte. 
vi. Debe crear un programa principal que procese el archivo de texto, haga los cálculos y muestre los 
totales por semestre y por zona en la pantalla.



Funciones a realzar:
F1 = convercion-de-divisa
F2 = venta_y_semestre
F3 = Ubicacion_por_tienda
"""
q,w,e,f,g,h = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO"]
j,k,l,ñ,z = ["JULIO", "AGOSTO", "SEPTIEMBRE", "NOVIEMBRE", "DICIEMBRE"]
num_lineas = []
a = 1

text = open(r"C:\Users\C5E372\APPS\CI-0110\16\Ejercicio 16-1.txt", "r")
one = 0
final = 4
ventas_s_1 = []
ventas_s_2 = []
ventas_z_n = []
ventas_z_c = []
ventas_z_s = []
P1 = []
P2 = []
data = []
for a in range(0, 100):
    x = text.readline(a)
    data.append(x)
    if q or w or e or f or g or h in data:
          P1.append(x)    
    elif j or k or l or ñ or z in data:
          P2.append(x)
    a+=1

print(P1)
"""
for x in text:
    data.append(x)
    print(data)  
"""


""""
data1 
lineas = f.readlines()
for num_lineas, linea in enumerate(lineas, start=1):
"""