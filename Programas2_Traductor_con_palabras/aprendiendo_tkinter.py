import tkinter # Importacion de la libreria

def saludoPrueba(nombre):
    print(f"Pinche {nombre} Ya esta presionando el boton chamaco miado!")

ventana = tkinter.Tk() # Creacion de la ventana con variable asignada
ventana.geometry("600x400") # Modificacion del tamano de la ventana con parametro: "LargoxAncho"

etiqueta = tkinter.Label(ventana, text="Bienvenido al traductor de mierda!!!", bg="blue") # Etiqueta de datos
etiqueta.pack(fill=tkinter.Y, expand=True) # Metodo para implementar la etiqueta llenando el espacio correspondiente en la ventana (Vertical)
# etiqueta.pack(fill=tkinter.X, expand=True "[fill=tkinter.BOTH implementa en X y Y]") # Metodo para implementar la etiqueta llenando el espacio correspondiente en la ventana (Horizontal)
# etiqueta.pack(side=tkinter.BOTTOM) # Metodo para implementar la etiqueta en la ventana

boton1 = tkinter.Button(ventana, text="Haga click cabron!!!", padx=40, pady=30, command= lambda: saludoPrueba("Mao Zedong"))
boton1.pack(side=tkinter.RIGHT)

cajaDeTexto1 = tkinter.Entry(ventana, background="#ff120a")
cajaDeTexto1.pack(side=tkinter.LEFT)

ventana.mainloop() # Ejecucion de la ventana