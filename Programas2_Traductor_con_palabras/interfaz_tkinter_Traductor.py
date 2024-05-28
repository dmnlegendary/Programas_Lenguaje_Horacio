import tkinter

ventana = tkinter.Tk()
ventana.geometry("600x600")

Texto_Bienvenida = tkinter.Label(ventana, text="Bienvenido al traductor, Ingrese una palabra:", font="Arial", bg="yellow")
Texto_Bienvenida.pack()

ventana.mainloop() # Ejecucion de la ventana