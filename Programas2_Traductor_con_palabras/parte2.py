'''
"Traductor evolutivo: Parte 1

Alumno: Diaz Jimenez Jorge Arif

Grupo: 5BM1

Se solicita un programa divido en tres partes:
1) Un arreglo de palabras en espanol, otro en ingles y se solicitara al usuario buscar una palabra: el programa traduce, de no ser el caso aborta y fracasa.
2) Complementamos la aprte anterior integrando una opcion para que el usuario ingrese la palabra y su traduccion.
3) Se agrega un tercer arreglo para predecir palabras que estan mal escritas.
'''

import tkinter # Libreria de GUI

# Apertura e inicializacion de ventana
ventana = tkinter.Tk()
ventana.geometry("600x400")
ventana.title("Tradcutor Espanol-Ingles")
ventana.configure(background="#35DB7A")

# Control del sistema 
palabrasEspanol = ["carro", "mesa", "tiburon", "negro", "blanco", "barco", "tarro", "barro"]
palabrasIngles = ["car", "table", "shark", "black", "white", "ship", "jar", "mud"]

# Funciones para el desarrollod el programa
def buscarTraduccion(palabra) -> str:
    for indice, palabrasArreglo in enumerate(palabrasEspanol):
        if (palabra==palabrasArreglo):
            print(f"La traduccion de {palabra} es {palabrasIngles[indice]}")
            return palabrasIngles[indice]

    for indice, palabrasArreglo in enumerate(palabrasIngles):
        if (palabra==palabrasArreglo):
            print(f"La traduccion de {palabra} es {palabrasEspanol[indice]}")
            return palabrasEspanol[indice]

    print("Esta madre no sirvio de nada.")
    return "NO SE ENCONTRO TRADUCCION."

def encontrarCoincidencia() -> None:
    palabraIngresada = entradaDeTexto.get()
    palabraIngresada = palabraIngresada.lower()
    if (palabraIngresada.find(' ') != -1):
        print("Ha sucedido un error: Ingreso mas de una palabra!")
        exit(1)
    else:
        palabraTraducida = buscarTraduccion(palabraIngresada)
        etiquetaDeTraduccion["text"] = palabraTraducida

def agregarInformacion() -> None:
    print("Se ha agregado exitosamente la nueva informacion")

# Boton y etiquetas para para realizar la traducción
etiquetaTitulo = tkinter.Label(ventana, text="Bienvenido al traductor de idiomas!!!", bg="#850903", padx=30, pady=10, fg="#FFFEFE")
etiquetaTitulo.pack(side=tkinter.TOP, expand=True)

entradaDeTexto = tkinter.Entry(ventana, background="#850903", fg="#FFFEFE", width=50)
entradaDeTexto.pack(side=tkinter.TOP, expand=True, pady=6)

etiquetaDeTraduccion = tkinter.Label(ventana, bg="#9E9C7C", padx=20, pady=20)
etiquetaDeTraduccion.pack(side=tkinter.TOP)

botonTraduccion = tkinter.Button(ventana, text="Traducir", padx=40, pady=30, command=lambda: encontrarCoincidencia())
botonTraduccion.pack(side=tkinter.BOTTOM, expand=True)

# botonParaAgregarTraduccion = tkinter.Button(ventana, text="SI", padx=4, pady=4, command=lambda: agregarInformacion())

ventana.mainloop() # Ejecucion principal de la ventana