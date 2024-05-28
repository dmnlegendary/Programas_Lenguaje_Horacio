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

ventana = tkinter.Tk()
ventana.geometry("600x400")

seEncontroLaPalabra = False
palabrasEspanol = ["carro", "mesa", "tiburon", "negro", "blanco", "barco"]
palabrasIngles = ["car", "table", "shark", "black", "white", "ship"]

palabraUsuario = str(input("Ingrese la palabra a traducir: "))

for indice, palabra in enumerate(palabrasEspanol):
    if (palabraUsuario==palabra):
        print(f"La traduccion de {palabraUsuario} es {palabrasIngles[indice]}")
        seEncontroLaPalabra = True

if seEncontroLaPalabra==False:
    print("Esta madre no sirvio de nada.")

ventana.mainloop()