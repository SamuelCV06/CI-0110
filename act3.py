""" Ejercicio 11 - Actividad 3
Proposito : A partir de una calificación académica numérica entre 0 y 10, generar la nota equivalente en Europa con
base en la siguiente tabla:

Calificación Numérica (cn) Equivalencia Europea
9 <= cn <= 10 = A
7 <= cn < 9 = B
5 <= cn < 7 = C
cn < 5 = F
"""
"""
Algoritmo: 
1. nota <---- pedir al usuario
2. if nota >= 9 then
2.1 cal_eu = "A"
3. else
3.1 if nota >= 7 then
3.1.1 cal_eu = "B"
3.2 else
3.2.1 if nota >= 5 then
3.2.1.1 cal_eu = "C"
3.2.2 else
3.2.2.2 cal_eu = "F"
4. print <--- "El equivalente europeo es " & cal_eu"1
"""

nota = float(input("Digite su calificación numerica: "))
cal_eu = 0
if nota >= 9:
    cal_eu = "A"
elif nota >= 7:
    cal_eu = "B"
elif nota >= 5:
    cal_eu = "C"
else: 
    cal_eu = "F"
print("El equivalente de su califición numerica", nota, "en calificación Europea es", cal_eu)
