#Esto es un comentario en Python

""" Esto no tiene sentido 
    me entienes reealemtne no tiene logica
	pero bueno """

restart = "s"
while restart == "s":
     print ("¡Buenos días! \n Por favor, indique su edad:") 
     edad = float(input ()) 
     if edad < 6:
          print ("El precio del tiquete es de $2.00") 
     elif edad > 10:
          print ("El precio del tiquete es de $3") 
     else:
          print ("El precio del tiquete es de $2,50")
     print ("quieres reiniciar s/n")
     restart = input("¿Quieres volver a ejecutar el programa? (s/n): ")
     




