import tkinter as tk
from tkinter import simpledialog, messagebox
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
root.geometry("500x400")

palabra_label = tk.Label(root, text="Oración 1:")
palabra2_label = tk.Label(root, text="Oración 2:")
palabra_entry = tk.Entry(root)
palabra2_entry = tk.Entry(root)
resultado_label = tk.Label(root, text="")

palabra_label.place(x=80, y=30)
palabra2_label.place(x=80, y=50)
palabra_entry.place(x=140, y=30)
palabra2_entry.place(x=140, y=50)
resultado_label.place(x=40, y=140)

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

def buscar_regla_traducida(etiquetas_origen):
    with open('resultados.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].strip().lower() == etiquetas_origen.strip().lower():
                return row[1]
    return None

def cargar_etiquetas_csv(archivo):
    etiquetas = {}
    with open(archivo, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 3:
                palabra_ingles = row[0]
                palabra_espanol = row[1]
                gramatica = row[2]
                etiquetas[palabra_ingles] = {'traduccion': palabra_espanol, 'etiqueta': gramatica}
                etiquetas[palabra_espanol] = {'traduccion': palabra_ingles, 'etiqueta': gramatica}
    return etiquetas

etiquetas_dict = cargar_etiquetas_csv('etiquetas.csv')

# Función para etiquetar una oración
def etiquetar_oracion(oracion, etiquetas_dict):
    palabras = oracion.split()
    etiquetas = [etiquetas_dict.get(palabra.lower(), {'etiqueta': 'desconocido'})['etiqueta'] for palabra in palabras]
    return ' '.join(etiquetas)

# Función principal para procesar la oración ingresada
def procesar_oracion(oracion, etiquetas_dict):
    return etiquetar_oracion(oracion, etiquetas_dict)
        
# Función para construir la oración en el idioma destino
def construir_oracion(oracion_origen, etiquetas_origen, etiquetas_destino, etiquetas_dict):
    palabras_origen = oracion_origen.split()
    etiquetas_origen_list = etiquetas_origen.split()
    oracion_destino = []

    for etiqueta in etiquetas_destino.split():
        for i, etiqueta_origen in enumerate(etiquetas_origen_list):
            if etiqueta_origen == etiqueta:
                palabra_destino = etiquetas_dict.get(palabras_origen[i].lower(), {'traduccion': palabras_origen[i]})['traduccion']
                oracion_destino.append(palabra_destino)
                break

    return ' '.join(oracion_destino)

# Función para extraer y guardar reglas gramaticales
def extraer_y_guardar_reglas(oracion1, oracion2, etiquetas_dict):
    etiquetas_origen = procesar_oracion(oracion1, etiquetas_dict)
    etiquetas_destino = procesar_oracion(oracion2, etiquetas_dict)
    
    with open('resultados.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([etiquetas_origen, etiquetas_destino])

# Función principal
def traducir_palabra():
    oracion = palabra_entry.get().lower()
    oracion2 = palabra2_entry.get().lower()

    primera_palabra = oracion.split()[0]

    if primera_palabra in diccionario_espanol_ingles:
        idioma_origen = 'español'
    elif primera_palabra in diccionario_ingles_espanol:
        idioma_origen = 'ingles'
    else:
        idioma_origen = 'desconocido'

    etiquetas_origen = procesar_oracion(oracion, etiquetas_dict)

    if oracion2:
        etiquetas_destino = procesar_oracion(oracion2, etiquetas_dict)
        extraer_y_guardar_reglas(oracion, oracion2, etiquetas_dict)
    else:
        etiquetas_destino = buscar_regla_traducida(etiquetas_origen)

    if not etiquetas_destino:
        messagebox.showinfo("Sin coincidencias", "No se encontró una regla gramatical. Por favor, ingrese la traducción correcta.")
        return

    oracion_destino = construir_oracion(oracion, etiquetas_origen, etiquetas_destino, etiquetas_dict)
    resultado_label.config(text=f"Traducción: {oracion_destino}.")

traducir_button = tk.Button(root, text="Traducir", command=traducir_palabra)
traducir_button.place(x=130, y=90)

root.mainloop()
