import tkinter

def textoDeLaCaja():
    text20 = cajaDeTexto.get()
    print(text20)
    etiqueta["text"] = text20

ventana = tkinter.Tk()
ventana.geometry("600x400")

etiqueta = tkinter.Label(ventana, bg="green")
etiqueta.pack()

cajaDeTexto = tkinter.Entry(ventana, bg="yellow")
cajaDeTexto.pack(side="top")

boton = tkinter.Button(ventana, text="Clickeale papu", command= lambda: textoDeLaCaja())
boton.pack(side="bottom")

ventana.mainloop()