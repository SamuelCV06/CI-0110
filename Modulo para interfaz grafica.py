#Módulo para interfaz grafica
import tkinter as tk

#Submódulo para carpetas y archivos
from tkinter import filedialog

#Crear ventana gráfica
root = tk.Tk()
root.withdraw()  #Oculta

#Abrir el cuadro de diálogo para pedir archivo
ruta = filedialog.askopenfilename(title = "Seleccione un archivo",
                                    filetypes= [("Archivo de texto", "*.txt")])

if ruta:
    try: 
        with open(ruta, "r") as archivo:
            contenido = archivo.read()
            print(contenido)
    except:
        print("Error al abrir el archivo")
else: 
    print("Archivo no seleccionado")