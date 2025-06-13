numero = int(input("N:"))
divisor = int(input("D:"))

try:
    resultado = numero / divisor
except ZeroDivisionError:
    print("La maquina es tonta y no puede dividir por 0")
else:
    print(f"el resultado fue {resultado}")
