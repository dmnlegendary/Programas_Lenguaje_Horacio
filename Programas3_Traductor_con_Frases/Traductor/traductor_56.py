import tkinter as tk
from tkinter import simpledialog, messagebox, Toplevel
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

palabra_label = tk.Label(root, text="Texto a traducir:")
palabra_entry = tk.Entry(root)
resultado_label = tk.Label(root, text="")
regla_gramatical = {}

palabra_label.place(x=80, y=30)
palabra_entry.place(x=140, y=30)
resultado_label.place(x=40, y=100)

# Inicializar las etiquetas
etiquetas_dict = {}

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

# Función para agregar traducción y etiqueta si no se encuentra
def pedir_traduccion_y_etiqueta(palabra, idioma_origen):
    ventana_traduccion = Toplevel(root)
    ventana_traduccion.title("Agregar Traducción")
    ventana_traduccion.geometry("300x150")

    tk.Label(ventana_traduccion, text=f"Palabra: {palabra}").pack(pady=5)
    tk.Label(ventana_traduccion, text="Traducción:").pack(pady=5)
    traduccion_entry = tk.Entry(ventana_traduccion)
    traduccion_entry.pack(pady=5)

    tk.Label(ventana_traduccion, text="Etiqueta:").pack(pady=5)
    etiqueta_entry = tk.Entry(ventana_traduccion)
    etiqueta_entry.pack(pady=5)

    def guardar_traduccion():
        palabra_traducida = traduccion_entry.get().lower()
        etiqueta_gramatical = etiqueta_entry.get().lower()
        if idioma_origen == 'español':
            etiquetas_dict[palabra.lower()] = {'traduccion': palabra_traducida, 'etiqueta': etiqueta_gramatical}
        else:
            etiquetas_dict[palabra_traducida.lower()] = {'traduccion': palabra.lower(), 'etiqueta': etiqueta_gramatical}
        
        with open('etiquetas.csv', 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            if idioma_origen == 'español':
                writer.writerow([palabra.lower(), palabra_traducida.lower(), etiqueta_gramatical])
            else:
                writer.writerow([palabra_traducida.lower(), palabra.lower(), etiqueta_gramatical])
                
        agregar_palabras_txt(palabra.lower(), palabra_traducida.lower())
        ventana_traduccion.destroy()
        traducir_palabra()  # Volver a traducir después de agregar la traducción

    tk.Button(ventana_traduccion, text="Guardar", command=guardar_traduccion).pack(pady=10)

def cargar_etiquetas_csv(archivo):
    etiquetas = {}
    with open(archivo, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 3:  # Asegúrate de que la fila tenga al menos 3 elementos
                palabra_ingles = row[0]
                palabra_espanol = row[1]
                gramatica = row[2]
                etiquetas[palabra_ingles] = {'traduccion': palabra_espanol, 'etiqueta': gramatica}
                etiquetas[palabra_espanol] = {'traduccion': palabra_ingles, 'etiqueta': gramatica}
    return etiquetas

def cargar_reglas_csv(archivo):
    reglas = {}
    with open(archivo, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 2:  # Asegúrate de que la fila tenga al menos 2 elementos
                etiquetas_origen = row[0]
                etiquetas_destino = row[1]
                reglas[etiquetas_origen] = etiquetas_destino
    return reglas

def buscar_regla_gramatical(palabra, etiquetas, idioma_origen):
    if palabra in etiquetas:
        traduccion, gramatica = etiquetas[palabra]['traduccion'], etiquetas[palabra]['etiqueta']
        return traduccion, gramatica
    else:
        messagebox.showinfo("Sin coincidencias", "Agregando la palabra manualmente.")
        pedir_traduccion_y_etiqueta(palabra, idioma_origen)
        etiquetas = cargar_etiquetas_csv('etiquetas.csv')  # Recargar las etiquetas después de agregar la palabra
        return etiquetas[palabra]['traduccion'], etiquetas[palabra]['etiqueta']

def traducir_con_reglas(oracion, idioma_origen, etiquetas, archivo):
    palabras = oracion.split()
    traduccion = []

    for palabra in palabras:
        palabra_traducida, gramatica = buscar_regla_gramatical(palabra, etiquetas, idioma_origen)
        traduccion.append((palabra_traducida, gramatica))

    return traduccion

# Función para agregar una palabra manualmente al diccionario
def agregar_palabras_txt(palabra_espanol, palabra_ingles):
    with open("./Español.txt", "a", encoding="utf-8") as archivo1:
        archivo1.write("\n" + palabra_espanol)
    with open("./Ingles.txt", "a", encoding="utf-8") as archivo2:
        archivo2.write("\n" + palabra_ingles)

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

# Inicializar las etiquetas, las frecuencias y las reglas
frecuencias = cargar_frecuencias()
etiquetas_dict = cargar_etiquetas_csv('etiquetas.csv')
reglas_dict = cargar_reglas_csv('reglas.csv')

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

# Función para eliminar el artículo "the" de la traducción
def eliminar_articulo(traduccion):
    palabras = traduccion.split()
    if palabras[0].lower() == "the":
        palabras = palabras[1:]
    return " ".join(palabras)

def extraer_reglas(oracion1, oracion2):
    palabras1 = oracion1.split()
    palabras2 = oracion2.split()

    etiquetas_origen = []
    etiquetas_destino = []
    for palabra in palabras1:
        if palabra in etiquetas_dict:
            etiquetas_origen.append(etiquetas_dict[palabra]['etiqueta'])
    for palabra in palabras2:
        if palabra in etiquetas_dict:
            etiquetas_destino.append(etiquetas_dict[palabra]['etiqueta'])

    regla_origen = ' '.join(etiquetas_origen)
    regla_destino = ' '.join(etiquetas_destino)

    with open('reglas.csv', 'a', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([regla_origen, regla_destino])
    
    reglas_dict[regla_origen] = regla_destino

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

        etiquetas_oracion = [gramatica for _, gramatica in traducciones]
        etiquetas_oracion_str = ' '.join(etiquetas_oracion)

        if etiquetas_oracion_str in reglas_dict:
            regla_aplicada = reglas_dict[etiquetas_oracion_str]
            etiquetas_destino = regla_aplicada.split()

            palabras_traducidas = {'adjetivo': [], 'sustantivo': [], 'verbo': [], 'articulo': [], 'preposicion': [], 'conjuncion': [], 'adverbio': [], 'pronombre': [], 'interjeccion': []}
            for palabra_traducida, gramatica in traducciones:
                if gramatica in palabras_traducidas:
                    palabras_traducidas[gramatica].append(palabra_traducida)

            oracion_destino = []
            for etiqueta in etiquetas_destino:
                if etiqueta in palabras_traducidas:
                    oracion_destino.extend(palabras_traducidas[etiqueta])

            oracion_destino = eliminar_articulo(' '.join(oracion_destino))
            resultado_label.config(text=f"La traducción de '{palabra}' es '{oracion_destino}'.")
        else:
            oracion_destino = [palabra_traducida for palabra_traducida, _ in traducciones]
            oracion_destino = eliminar_articulo(' '.join(oracion_destino))
            resultado_label.config(text=f"La traducción de '{palabra}' es '{oracion_destino}'.")

            # Pedir al usuario la traducción correcta
            oracion_traducida = simpledialog.askstring("Entrada", "Por favor, introduce la traducción correcta de la oración:", parent=root)
            if oracion_traducida:
                extraer_reglas(palabra, oracion_traducida)

traducir_button = tk.Button(root, text="Traducir", command=traducir_palabra)
traducir_button.place(x=130, y=60)

root.mainloop()
