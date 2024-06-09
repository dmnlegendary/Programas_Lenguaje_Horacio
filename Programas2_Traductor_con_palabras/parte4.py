import tkinter as tk

# Diccionario de traducción
diccionario = {
    'hola': 'hello',
    'adiós': 'goodbye',
    'por favor': 'please',
    'gracias': 'thank you',
    'sí': 'yes',
    'no': 'no',
    'perro': 'dog',
    'gato': 'cat',
    'casa': 'house',
    'libro': 'book',
    'el': 'the',
    'la': 'the',
    'es': 'is',
    'y': 'and',
    'casa' : 'house',
    'roja' : 'red'
}

# Función de traducción
def traducir():
    frase = entrada.get().strip().lower()
    palabras = frase.split()
    
    if var.get() == 'es_en':
        traduccion = [diccionario.get(palabra, palabra) for palabra in palabras]
    else:
        traduccion_inversa = {v: k for k, v in diccionario.items()}
        traduccion = [traduccion_inversa.get(palabra, palabra) for palabra in palabras]
    
    resultado.config(text=' '.join(traduccion))

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Traductor de Frases")
ventana.geometry("400x200")

# Etiqueta y campo de entrada
tk.Label(ventana, text="Ingrese la frase:").pack(pady=5)
entrada = tk.Entry(ventana, width=50)
entrada.pack(pady=5)

# Opciones de idioma
var = tk.StringVar(value='es_en')
tk.Radiobutton(ventana, text="Español a Inglés", variable=var, value='es_en').pack()
tk.Radiobutton(ventana, text="Inglés a Español", variable=var, value='en_es').pack()

# Botón de traducir
boton_traducir = tk.Button(ventana, text="Traducir", command=traducir)
boton_traducir.pack(pady=10)

# Etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text="", font=('Arial', 14))
resultado.pack(pady=5)

# Iniciar el bucle de la aplicación
ventana.mainloop()
