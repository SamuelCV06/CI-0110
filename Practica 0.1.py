#Esto es un comentario en Python
""" Esto no tiene sentido 
    me entienes reealemtne no tiene logica
	pero bueno """

restart = "s"
while restart == ("s") :
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
          if restart == "n":
               try:
                    print ("Gracias por usar este programa")
                    break
                    input()
               except restart == ("s") or ("si") or ("SI") or ("Si") or ("S"):
                    restart = "s"
          elif restart == "no":
                try:
                    print ("Gracias por usar este programa")
                    break
                    input()
                except restart == ("s") or ("si") or ("SI") or ("Si") or ("S"):
                    restart = "s"
          elif restart == "No":
               try:
                    print ("Gracias por usar este programa")
                    break
                    input()
               except restart == ("s") or ("si") or ("SI") or ("Si") or ("S"):
                    restart = "s"
          elif restart == "NO":
               try:
                    print ("Gracias por usar este programa")
                    break
               except restart == ("s") or ("si") or ("SI") or ("Si") or ("S"):
                    restart = "s"
                    restart == "s"
          elif restart == "Si":
               try: restart = "s"
               except restart == "n":
                    restart = "n"
          elif restart == "si":
               try: restart = "s"
               except restart == "n":
                    restart = "n"
          elif restart == "SI":
               try: restart = "s"
               except restart == "n":
                    restart = "n"
          elif restart == "s":
               try: restart = "s"
               except restart == "n":
                    restart = "n"
          elif restart == "S":
               try: restart = "s"
               except restart == "n":
                    restart = "n"
          else:
               print ("Gracias por usar este programa")
               break
     except ValueError:
          print("Número no reconocido")
          print ("quieres reiniciar s/n")
          restart = input()
          if restart == ("n") or ("no") or ("No") or ("no"):
               print ("Gracias por usar este programa")
               input()


