'''
"Traductor evolutivo: Parte 2

Alumno: Diaz Jimenez Jorge Arif

Grupo: 5BM1

Se solicita un programa divido en tres partes:
1) Un arreglo de palabras en espanol, otro en ingles y se solicitara al usuario buscar una palabra: el programa traduce, de no ser el caso aborta y fracasa.
2) Complementamos la aprte anterior integrando una opcion para que el usuario ingrese la palabra y su traduccion.
3) Se agrega un tercer arreglo para predecir palabras que estan mal escritas.
'''

# Librerias de GUI
import tkinter
from tkinter import messagebox 
import tkinter.simpledialog

# Apertura e inicializacion de ventana principal
ventana = tkinter.Tk()
ventana.geometry("600x400")
ventana.title("Traductor Espanol-Ingles")
ventana.title("Traductor Espanol-Ingles")
ventana.configure(background="#35DB7A")

# Control del sistema 
palabrasEspanol = ["carro", "mesa", "tiburon", "negro", "blanco", "barco", "tarro", "barro"]
palabrasIngles = ["car", "table", "shark", "black", "white", "ship", "jar", "mud"]
correcciones = [
    ["karro", "carro", 12],
    ["karro", "barro", 8]
    ["karro", "tarro", 4]
    ["komer", "comer", 1],
    ["kuando", "cuando", 2],
    ["meza", "mesa", 7],
    ["kar", "car", 6],
    ["tavle", "table", 3],
]

'''Funciones para el desarrollo del programa'''

# Funcion que busca la palabra en el idioma objetivo
def buscarTraduccion(palabra) -> str:
    for indice, palabrasArreglo in enumerate(palabrasEspanol):
        if (palabra==palabrasArreglo):
            print(f"La traduccion de {palabra} es {palabrasIngles[indice]}")
            return palabrasIngles[indice]

    for indice, palabrasArreglo in enumerate(palabrasIngles):
        if (palabra==palabrasArreglo):
            print(f"La traduccion de {palabra} es {palabrasEspanol[indice]}")
            return palabrasEspanol[indice]

    print("No se pudo corregir.")
    iniciarVentanaDeAgregarTraduccion()
    return "NO SE ENCONTRO TRADUCCION."

def iniciarVentanaDeAgregarTraduccion() -> None:
    ventanaParaTraducciones = tkinter.Toplevel(ventana)
    ventanaParaTraducciones.geometry("300x180")
    ventanaParaTraducciones.title("Agregar palabras")
    ventanaParaTraducciones.configure(background="#B9DBE4")

    etiquetaDescriptiva = tkinter.Label(ventanaParaTraducciones, text="Agrege la traduccion de las palabras:", font=("Arial", 12, "bold"))
    etiquetaDescriptiva.pack(pady=20)

    etiquetaInsercionEspanol = tkinter.Label(ventanaParaTraducciones, text="Ingresa la palabra en ESPANOL:", font=("Verdana", 10, "bold"), bg="#E0AC69")
    etiquetaInsercionEspanol.pack(side=tkinter.TOP)
    entradaPalabraEspanol = tkinter.Entry(ventanaParaTraducciones, bg="#F5FFAE")
    entradaPalabraEspanol.pack(side=tkinter.TOP)

    etiquetaInsercionIngles = tkinter.Label(ventanaParaTraducciones, text="Ingresa la palabra en INGLES:", font=("Verdana", 10, "bold"), bg="#E0AC69")
    etiquetaInsercionIngles.pack(side=tkinter.TOP)
    entradaPalabraIngles = tkinter.Entry(ventanaParaTraducciones, bg="#F5FFAE")
    entradaPalabraIngles.pack(side=tkinter.TOP)

    botonConfirmacion = tkinter.Button(ventanaParaTraducciones, text="Actualizar datos", font=("Arial", 12, "bold"), bg="#27B79A", command=lambda: agregarInformacion(ventanaParaTraducciones, entradaPalabraEspanol, entradaPalabraIngles))
    botonConfirmacion.pack(side=tkinter.BOTTOM)
    
def iniciarVentanaDeCorreccion(correcto) -> None:
    ventanaParaCorrecciones = tkinter.Toplevel(ventana)
    ventanaParaCorrecciones.geometry("300x180")
    ventanaParaCorrecciones.title("Corregir Palabras")
    ventanaParaCorrecciones.configure(background="#B9DBE4")
    
    etiquetaDescriptiva = tkinter.Label(ventanaParaCorrecciones, text="¿Quizo decir lo siguiente?", font=("Arial", 12, "bold"))
    etiquetaDescriptiva.pack(pady=20)
    etiquetaPosibleCorreccion = tkinter.Label(ventanaParaCorrecciones, text=correcto, font=("Arial", 12, "bold"))
    etiquetaPosibleCorreccion.pack(side=tkinter.TOP)
    
    botonAfirmacion = tkinter.Button(ventanaParaCorrecciones, text="SI", command=lambda: correccionExitosa(ventanaParaCorrecciones, correcto))
    botonAfirmacion.pack()
    botonNegacion = tkinter.Button(ventanaParaCorrecciones, text="NO", command= lambda: correccionCancelada(ventanaParaCorrecciones))
    botonNegacion.pack()

# Funcion que asegura que solo se trabaje con palabras
def encontrarCoincidencia() -> None:
    palabraIngresada = entradaDeTexto.get()
    palabraIngresada = palabraIngresada.lower()
    if (palabraIngresada.find(' ') != -1):
        print("Ha sucedido un error: Ingreso mas de una palabra!")
        exit(1)
    else:
        palabraTraducida = buscarTraduccion(palabraIngresada)
        etiquetaDeTraduccion["text"] = palabraTraducida

# Funcion que permitira modificar las listas de palabras espanol-ingles
def agregarInformacion(ventanaSecundaria, palabrasEnEspanol, palabrasEnIngles) -> None:
    control1, control2 = palabrasEnEspanol.get(), palabrasEnIngles.get()
    if (control1=="" or control2==""):
        print("No se ha agregado informacion debido a algun campo vacio")
        ventanaSecundaria.destroy()
    else:
        palabrasEspanol.append(control1)
        palabrasIngles.append(control2)
        print("Se ha agregado exitosamente la nueva informacion")
        ventanaSecundaria.destroy()
        
# Funcion para corregir palabra y cerrar ventana de correccion
def correccionExitosa(ventanaSecundaria, palabraCorregida) -> str:
    ventanaSecundaria.destroy()
    entradaDeTexto.delete(0,tkinter.END)
    entradaDeTexto.insert(0,palabraCorregida)
    return palabraCorregida

# Funcion para cerrar ventana de correccion sin corregir palabra
def correccionCancelada(ventanaSecundaria) -> str:
    ventanaSecundaria.destroy()
    return "0"

# Funcion para cerrar ventana principal
def cerrarVentanaPrincipal() -> None:
    if messagebox.askokcancel("Salir", "¿Seguro que quieres salir?"):
        ventana.destroy()

# Boton y etiquetas para para realizar la traducción
etiquetaTitulo = tkinter.Label(ventana, text="Bienvenido al traductor de idiomas!!!", bg="#850903", padx=30, pady=10, fg="#FFFEFE")
etiquetaTitulo.pack(side=tkinter.TOP, expand=True)

entradaDeTexto = tkinter.Entry(ventana, background="#850903", fg="#FFFEFE", width=50)
entradaDeTexto.pack(side=tkinter.TOP, expand=True, pady=6)

etiquetaDeTraduccion = tkinter.Label(ventana, bg="#9E9C7C", padx=20, pady=20)
etiquetaDeTraduccion.pack(side=tkinter.TOP)

botonTraduccion = tkinter.Button(ventana, text="Traducir", padx=40, pady=30, command=lambda: encontrarCoincidencia())
botonTraduccion.pack(side=tkinter.TOP, expand=True)

botonAbandonar = tkinter.Button(ventana, text="Cerrar traductor espanol-ingles", padx=30, pady=18, command=lambda: cerrarVentanaPrincipal())
botonAbandonar.pack(side=tkinter.BOTTOM, expand=True)

ventana.mainloop() # Ejecucion principal de la ventana