import tkinter as tk
from tkinter import simpledialog, messagebox
import textdistance
import json
import csv

# Lectura de archivos y creación de diccionarios
with open("./Español.txt", "r", encoding="utf-8") as archivo1:
    contenido_archivo1 = archivo1.read().splitlines()
with open("./Ingles.txt", "r", encoding="utf-8") as archivo2:
    contenido_archivo2 = archivo2.read().splitlines()

diccionario_espanol_ingles = {palabra.lower(): traduccion.lower() for palabra, traduccion in zip(contenido_archivo1, contenido_archivo2)}
diccionario_ingles_espanol = {palabra.lower(): traduccion.lower() for palabra, traduccion in zip(contenido_archivo2, contenido_archivo1)}

root = tk.Tk()
root.title("Traductor")
root.geometry("1280x720")
root.configure(bg="#f0f0f0")  # Color de fondo de la ventana

font_style = ("Verdana", 16, "bold")

palabra_label = tk.Label(root, text="Palabra:", font=font_style, bg="#d3d3d3")  # Color de fondo del label
palabra_entry = tk.Entry(root, font=font_style, bg="#ffffff")  # Color de fondo del entry
resultado_label = tk.Label(root, text="", font=font_style, bg="#f0f0f0")  # Color de fondo del label

palabra_label.place(x=80, y=30)
palabra_entry.place(x=140, y=30)
resultado_label.place(x=40, y=100)

# Cargar o inicializar el archivo de frecuencias
def cargar_frecuencias():
    try:
        with open("frecuencias.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

def guardar_frecuencias(frecuencias):
    with open("frecuencias.json", "w", encoding="utf-8") as archivo:
        json.dump(frecuencias, archivo, ensure_ascii=False, indent=4)

def agregar_etiqueta(palabra, idioma_origen, etiquetas):
    if idioma_origen == 'español':
        palabra_traducida = simpledialog.askstring("Entrada", f"Por favor, introduce la traducción en inglés para '{palabra}':")
        gramatica = simpledialog.askstring("Entrada", f"Por favor, introduce la etiqueta gramatical para '{palabra}':")
        etiquetas[palabra] = (palabra_traducida, gramatica)
        etiquetas[palabra_traducida] = (palabra, gramatica)
    else:
        palabra_traducida = simpledialog.askstring("Entrada", f"Por favor, introduce la traducción en español para '{palabra}':")
        gramatica = simpledialog.askstring("Entrada", f"Por favor, introduce la etiqueta gramatical para '{palabra}':")
        etiquetas[palabra] = (palabra_traducida, gramatica)
        etiquetas[palabra_traducida] = (palabra, gramatica)

    with open('etiquetas.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([palabra, palabra_traducida, gramatica])

    return palabra_traducida, gramatica

def cargar_etiquetas_csv(archivo):
    etiquetas = {}
    with open(archivo, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 3:  # Asegúrate de que la fila tenga al menos 3 elementos
                palabra_ingles = row[0]
                palabra_espanol = row[1]
                gramatica = row[2]
                etiquetas[palabra_ingles] = (palabra_espanol, gramatica)
                etiquetas[palabra_espanol] = (palabra_ingles, gramatica) 
    return etiquetas

def buscar_regla_gramatical(palabra, etiquetas, idioma_origen):
    if palabra in etiquetas:
        traduccion, gramatica = etiquetas[palabra]
        return traduccion, gramatica
    else:
        messagebox.showinfo("Sin coincidencias", "Agregando la palabra manualmente.")
        traduccion, gramatica = agregar_etiqueta(palabra, idioma_origen, etiquetas)
        return traduccion, gramatica

def traducir_con_reglas(oracion, idioma_origen, etiquetas, archivo):
    palabras = oracion.split()
    traduccion = []

    for palabra in palabras:
        palabra_traducida, gramatica = buscar_regla_gramatical(palabra, etiquetas, idioma_origen)
        etiquetas = cargar_etiquetas_csv(archivo)
        traduccion.append(palabra_traducida)

    return traduccion

# Función para agregar una palabra manualmente al diccionario
def agregar_palabra_manualmente(palabra):
    traduccion_manual = simpledialog.askstring("Agregar palabra", f"Ingrese la traducción de '{palabra}':", parent=root).lower()
    if traduccion_manual:
        with open("./Español.txt", "a", encoding="utf-8") as archivo1:
            archivo1.write("\n" + palabra)
        with open("./Ingles.txt", "a", encoding="utf-8") as archivo2:
            archivo2.write("\n" + traduccion_manual)

        messagebox.showinfo("Palabra agregada", f"La traducción de '{palabra}' ha sido agregada correctamente.")

        diccionario_espanol_ingles[palabra] = traduccion_manual
        diccionario_ingles_espanol[traduccion_manual] = palabra

        if palabra_entry.get().lower() == palabra:
            resultado_label.config(text=f"La traducción de '{palabra}' es '{traduccion_manual}'.")

# Inicializar las etiquetas y las frecuencias
frecuencias = cargar_frecuencias()

# Función para sugerir una traducción basada en la entrada del usuario
def sugerir_traduccion(palabra, diccionario):
    sugerencias = []

    for palabra_dicc in diccionario:
        distancia = textdistance.levenshtein.normalized_distance(palabra, palabra_dicc)
        if distancia < 0.4:
            sugerencias.append((palabra_dicc, distancia))

    # Ordenar las sugerencias por frecuencia (descendente) y luego por distancia (ascendente)
    sugerencias.sort(key=lambda x: (-frecuencias.get(x[0], 0), x[1]))
    return sugerencias

# Función principal
def traducir_palabra():
    palabra = palabra_entry.get().lower()
    palabras = palabra.split()

    if len(palabras) < 2:
        if palabra in diccionario_espanol_ingles:
            traduccion = diccionario_espanol_ingles[palabra]
            resultado_label.config(text=f"La traducción de '{palabra}' es '{traduccion}'.")
        elif palabra in diccionario_ingles_espanol:
            traduccion = diccionario_ingles_espanol[palabra]
            resultado_label.config(text=f"La traducción de '{palabra}' es '{traduccion}'.")
        else:
            sugerencias_espanol = sugerir_traduccion(palabra, diccionario_espanol_ingles)
            sugerencias_ingles = sugerir_traduccion(palabra, diccionario_ingles_espanol)

            # Depuración: Mostrar sugerencias y frecuencias antes de preguntar al usuario
            print("Sugerencias ingles:", [(sug, frecuencias.get(sug, 0)) for sug, _ in sugerencias_ingles])
            print("Sugerencias español:", [(sug, frecuencias.get(sug, 0)) for sug, _ in sugerencias_espanol])

            if sugerencias_ingles or sugerencias_espanol:
                for sug, _ in sugerencias_ingles + sugerencias_espanol:
                    # Mostrar la frecuencia junto con la sugerencia
                    frecuencia = frecuencias.get(sug, 0)
                    respuesta = messagebox.askyesno("Sugerencia", f"¿Quisiste decir '{sug}'?")

                    if respuesta:
                        palabra_entry.delete(0, tk.END)
                        palabra_entry.insert(0, sug)
                        frecuencias[sug] = frecuencia + 1
                        guardar_frecuencias(frecuencias)
                        traducir_palabra()
                        return
                messagebox.showinfo("Sin coincidencias", "Agregando la palabra manualmente.")
                agregar_palabra_manualmente(palabra)
            else:
                respuesta = messagebox.askyesno("No encontrada", f"La palabra '{palabra}' no se encontró en ninguno de los archivos.\n¿Desea agregarla manualmente?")
                if respuesta:
                    agregar_palabra_manualmente(palabra)
    elif len(palabras) >= 2:
        primera_palabra = palabras[0]

        if primera_palabra in diccionario_espanol_ingles:
            idioma_origen = 'español'
        elif primera_palabra in diccionario_ingles_espanol:
            idioma_origen = 'ingles'

        archivo_csv = 'etiquetas.csv'
        etiquetas = cargar_etiquetas_csv(archivo_csv)

        traducciones = traducir_con_reglas(palabra, idioma_origen, etiquetas, archivo_csv)
        oracion_traducida = " ".join(traducciones)
        resultado_label.config(text=f"La traducción de '{palabra}' es '{oracion_traducida}'.")

traducir_button = tk.Button(root, text="Traducir", command=traducir_palabra, font=font_style, bg="#a3a3a3")  # Color de fondo del botón
traducir_button.place(x=130, y=60)

root.mainloop()
