#Esto es un comentario en Python

""" Esto no tiene sentido 
    me entienes reealemtne no tiene logica
	pero bueno """

restart = "s"
while restart == "s":
     try:
          print ("¡Buenos días! \n Por favor, indique su edad:") 
          edad = float(input ()) 
          if edad < 6:
               print ("El precio del tiquete es de $2.00") 
               print("¿Quieres volver a ejecutar el programa? (s/n): ")
          elif edad > 10:
               print ("El precio del tiquete es de $3")
               print("¿Quieres volver a ejecutar el programa? (s/n): ")
          else:
               print ("El precio del tiquete es de $2,50")
               print("¿Quieres volver a ejecutar el programa? (s/n): ")
          restart = input()
          if restart == "n" or "no" or "No" or "no":
               print ("Gracias por usar este programa")
          input()
     except ValueError:
          print("Número no reconocido")
          print ("quieres reiniciar s/n")
          restart = input()
          if restart == "n" or "no" or "No" or "no":
               print ("Gracias por usar este programa")


