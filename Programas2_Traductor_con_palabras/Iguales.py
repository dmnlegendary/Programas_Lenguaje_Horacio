import csv
import os
import math
import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel, IntVar

class Palabra:
    def __init__(self, original, traduccion, etiquetas, contador):
        self.original = original
        self.traduccion = traduccion
        self.etiquetas = etiquetas
        self.contador = contador

def leerDiccionarioDesdeCSV():
    diccionario = []
    if os.path.exists('diccionario.csv'):
        with open('diccionario.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                etiquetas = list(map(int, row[2].strip('[]').replace("'", "").split(',')))
                diccionario.append(Palabra(row[0], row[1], etiquetas, int(row[3])))
    return diccionario

def escribirDiccionarioEnCSV(diccionario):
    with open('diccionario.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for palabra in diccionario:
            writer.writerow([palabra.original, palabra.traduccion, palabra.etiquetas, palabra.contador])

def diccionarioInicial():
    diccionario = leerDiccionarioDesdeCSV()
    if not diccionario:
        diccionario = [
            Palabra("carro", "car", [1], 0),
            Palabra("manzana", "apple", [1], 0),
            Palabra("perro", "dog", [1], 0),
            Palabra("rojo", "red", [3], 0),
            Palabra("amanecer", "dawn", [1, 5], 0),
            Palabra("alba", "dawn", [1], 0)
        ]
        escribirDiccionarioEnCSV(diccionario)
    return diccionario

def leerOrdenEtiquetasDesdeCSV():
    orden_etiquetas = {}
    if os.path.exists('orden_etiquetas.csv'):
        with open('orden_etiquetas.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                etiquetas = row[1].strip('[]').replace("'", "").split(',')
                orden_etiquetas[row[0]] = list(map(int, etiquetas))
    return orden_etiquetas

def escribirOrdenEtiquetasEnCSV(orden_etiquetas):
    with open('orden_etiquetas.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for espanol, ingles in orden_etiquetas.items():
            writer.writerow([espanol, ingles])

def encontrarTraduccion(diccionario, palabra):
    traducciones = []
    for entrada in diccionario:
        if entrada.original == palabra:
            traducciones.append(entrada.traduccion)
        if entrada.traduccion == palabra:
            traducciones.append(entrada.original)
    return traducciones

def eliminarDuplicados(traducciones):
    return list(set(traducciones))

def actualizarContador(diccionario, traducciones):
    for palabra in traducciones:
        for entrada in diccionario:
            if palabra == entrada.original or palabra == entrada.traduccion:
                entrada.contador += 1
    escribirDiccionarioEnCSV(diccionario)

def distanciaLevenshtein(cadena1, cadena2):
    if not cadena1:
        return len(cadena2)
    if not cadena2:
        return len(cadena1)

    if cadena1[0] == cadena2[0]:
        costo = 0
    else:
        costo = 1

    return min(distanciaLevenshtein(cadena1[1:], cadena2) + 1,
               distanciaLevenshtein(cadena1, cadena2[1:]) + 1,
               distanciaLevenshtein(cadena1[1:], cadena2[1:]) + costo)

def buscarSimiles(palabra, diccionario):
    listaSimiles = []
    for entrada in diccionario:
        listaSimiles.append((entrada.original, distanciaLevenshtein(palabra, entrada.original) - (0.05 * math.log(entrada.contador + 1)) ))

    listaSimiles.sort(key=lambda x: x[1])

    return listaSimiles[:3]

def buscarPalabra(diccionario, palabra):
    traducciones = eliminarDuplicados(encontrarTraduccion(diccionario, palabra))
    if traducciones:
        actualizarContador(diccionario, traducciones)
        return traducciones  # Devuelve todas las traducciones
    else:
        return []  # Devuelve una lista vacía si no hay traducción

def buscar_palabra_button_clicked():
    frase = palabra_entry.get().lower()
    palabras = frase.split()
    diccionario = diccionarioInicial()
    orden_etiquetas = leerOrdenEtiquetasDesdeCSV()

    etiquetas_frase = []
    traduccion_completa = []

    for palabra in palabras:
        traducciones = buscarPalabra(diccionario, palabra)
        if traducciones:
            traduccion_completa.append(traducciones[0])
            etiquetas = [p.etiquetas for p in diccionario if p.original == palabra or p.traduccion == palabra][0]
            etiquetas_frase.append(etiquetas)
        else:
            anidarEntrada(diccionario, palabra)
            traducciones = buscarPalabra(diccionario, palabra)
            if traducciones:
                traduccion_completa.append(traducciones[0])
                etiquetas = [p.etiquetas for p in diccionario if p.original == palabra or p.traduccion == palabra][0]
                etiquetas_frase.append(etiquetas)
            else:
                traduccion_completa.append(palabra)  # Si no se agregó, se usa la palabra original

    etiquetas_flat = [item for sublist in etiquetas_frase for item in sublist]
    etiquetas_frase_str = str(etiquetas_flat)

    if etiquetas_frase_str not in orden_etiquetas:
        orden_traduccion = etiquetas_flat
        orden_etiquetas[etiquetas_frase_str] = etiquetas_flat
        escribirOrdenEtiquetasEnCSV(orden_etiquetas)
    else:
        orden_traduccion = orden_etiquetas[etiquetas_frase_str]

    traduccion_ordenada = ordenarSegunEtiquetas(traduccion_completa, orden_traduccion, diccionario)
    resultado_label.config(text=f"La frase '{frase}' tiene como traducción: {' '.join(traduccion_ordenada)}")

def ordenarSegunEtiquetas(traduccion_completa, orden_traduccion, diccionario):
    ordenada = []
    for num in orden_traduccion:
        for palabra in traduccion_completa:
            etiquetas = [p.etiquetas for p in diccionario if p.traduccion == palabra or p.original == palabra][0]
            if num in etiquetas and palabra not in ordenada:
                ordenada.append(palabra)
                break
    return ordenada

def solicitartraduccion(palabra):
    traduccion = simpledialog.askstring("Traducción", f"Ingrese la traducción para la palabra '{palabra}':", parent=root)
    return traduccion.lower() if traduccion else ""

def solicitarEtiquetas(palabra):
    etiquetas_window = Toplevel(root)
    etiquetas_window.title(f"Seleccionar Etiquetas para '{palabra}'")
    etiquetas_var = []

    etiquetas_diccionario = {
        1: "articulos",
        2: "sustantivos",
        3: "adjetivos",
        4: "pronombres",
        5: "verbos",
        6: "adverbio",
        7: "preposicion",
        8: "articulos"
    }

    def confirmar():
        etiquetas = [key for key, var in etiquetas_var if var.get() == 1]
        etiquetas_window.destroy()
        etiquetas_window.etiquetas_seleccionadas = etiquetas

    for key, value in etiquetas_diccionario.items():
        var = IntVar()
        chk = tk.Checkbutton(etiquetas_window, text=value, variable=var)
        chk.pack(anchor='w')
        etiquetas_var.append((key, var))

    confirmar_button = tk.Button(etiquetas_window, text="Confirmar", command=confirmar)
    confirmar_button.pack()

    etiquetas_window.wait_window()
    return etiquetas_window.etiquetas_seleccionadas

def solicitarEtiquetaUnica(etiquetas):
    etiqueta_window = Toplevel(root)
    etiqueta_window.title("Seleccionar Etiqueta")
    etiqueta_var = IntVar()

    def confirmar():
        etiqueta_window.destroy()

    for etiqueta in etiquetas:
        tk.Radiobutton(etiqueta_window, text=str(etiqueta), variable=etiqueta_var, value=etiqueta).pack(anchor='w')

    confirmar_button = tk.Button(etiqueta_window, text="Confirmar", command=confirmar)
    confirmar_button.pack()

    etiqueta_window.wait_window()
    return etiqueta_var.get()

def agregar_traduccion():
    diccionario = diccionarioInicial()
    nuevas_traducciones = []

    for entrada in diccionario:
        if not entrada.traduccion:
            nuevas_traducciones.append(entrada.original)

    for palabra in nuevas_traducciones:
        traduccion = solicitartraduccion(palabra)
        etiquetas = solicitarEtiquetas(palabra)
        entrada = next((p for p in diccionario if p.original == palabra), None)
        if entrada:
            entrada.traduccion = traduccion
            entrada.etiquetas = etiquetas
            entrada.contador = 1
            resultado_label.config(text=f"Palabra '{palabra}' agregada al diccionario con traducción '{traduccion}' y etiquetas '{etiquetas}'.")

    escribirDiccionarioEnCSV(diccionario)

def anidarEntrada(diccionario, palabra):
    respuesta = messagebox.askquestion("Nueva Palabra", f"Desea ingresar la palabra '{palabra}' al diccionario?")
    if respuesta == 'yes':
        traduccion = solicitartraduccion(palabra)
        etiquetas = solicitarEtiquetas(palabra)
        if traduccion:
            diccionario.append(Palabra(palabra, traduccion, etiquetas, 1))
            escribirDiccionarioEnCSV(diccionario)
            messagebox.showinfo("Palabra Agregada", f"Palabra '{palabra}' agregada al diccionario con traducción '{traduccion}' y etiquetas '{etiquetas}'.")
        else:
            messagebox.showinfo("Sin Traducción", f"No se agregó la palabra '{palabra}' ya que no se proporcionó una traducción.")
    else:
        messagebox.showinfo("Cancelado", f"No se agregará la palabra: '{palabra}'")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Traductor")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

palabra_label = tk.Label(frame, text="Frase a traducir:")
palabra_label.grid(row=0, column=0, sticky="w")

palabra_entry = tk.Entry(frame)
palabra_entry.grid(row=0, column=1)

traducir_button = tk.Button(frame, text="Buscar", command=buscar_palabra_button_clicked)
traducir_button.grid(row=0, column=2, padx=5)

resultado_label = tk.Label(frame, text="")
resultado_label.grid(row=1, column=0, columnspan=3, pady=5, sticky="w")

nueva_traduccion_button = tk.Button(frame, text="Agregar Traducción", command=agregar_traduccion)
nueva_traduccion_button.grid(row=2, column=2, padx=5)

root.mainloop()
