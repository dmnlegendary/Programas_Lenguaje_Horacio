import tkinter

# Funciones a implementar
def primeraFuncion():
    print("Primera")

def segundaFuncion():
    print("Segunda")

def terceraFuncion():
    print("Tercera")

ventana = tkinter.Tk()
ventana.geometry("600x400")

# Uso del metodo GRID
boton1 = tkinter.Button(ventana, bg="blue", command=primeraFuncion, width=10, text="button1")
boton2 = tkinter.Button(ventana, bg="navy", command=segundaFuncion, width=10, text="button2")
boton3 = tkinter.Button(ventana, bg="#0000A8", command=terceraFuncion, width=10, text="button3")
boton1.pack()
boton2.pack()
boton3.pack()

ventana.mainloop()