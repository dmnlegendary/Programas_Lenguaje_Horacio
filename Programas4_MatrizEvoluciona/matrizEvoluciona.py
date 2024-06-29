import tkinter as tk
from tkinter import simpledialog, messagebox
import csv
import random
from collections import Counter, defaultdict

# Función para construir n-gramas a partir de una lista de palabras
def construir_ngramas(palabras, n):
    ngramas = defaultdict(list)
    for i in range(len(palabras) - n):
        key = tuple(palabras[i:i+n])
        next_word = palabras[i + n]
        ngramas[key].append(next_word)
    return ngramas

# Función para contar las frecuencias de los n-gramas
def contar_frecuencias_ngramas(ngramas):
    frecuencias = defaultdict(Counter)
    for key, words in ngramas.items():
        frecuencias[key] = Counter(words)
    return frecuencias

# Función para predecir la siguiente palabra basada en el historial de n-gramas
def predecir_palabra(ngramas, historial):
    key = tuple(historial)
    if key in ngramas:
        return random.choice(ngramas[key])
    else:
        return random.choice(list(ngramas.keys()))[0]

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Generador de Texto con N-gramas")
        self.geometry("1280x720")
        self.configure(bg="#40A12F")

        self.result_label = tk.Label(self, text="", fg="#000000", bg="#FF99DD", font=("Verdana", 16, "bold"), justify=tk.CENTER, wraplength=500)
        self.result_label.pack(side=tk.LEFT)
        
        self.textLabel = tk.Label(self, text="El cuento generado es el siguiente: \n\n\n\n\n\n\n\n\n. Cuento generado correctamente", fg="#FFFFFF", justify=tk.CENTER, font=("Verdana", 16, "bold"), bg="#1020A0", padx=300, pady=300)
        # self.textLabel.pack(side=tk.RIGHT)

        self.procesar_archivo()

    def procesar_archivo(self):
        ruta_archivo = 'historia.csv'  # Ruta fija al archivo CSV
        letras = []
        with open(ruta_archivo, newline='', encoding='ISO-8859-1') as csvfile:
            lector = csv.DictReader(csvfile)
            for fila in lector:
                letras.append(fila['cuento'])

        linea = ' '.join(letras)
        palabras = linea.split()

        frecuencias = Counter(palabras)

        numero_palabras = simpledialog.askinteger("Input", "Ingrese la cantidad de palabras mas usadas que quiera ver", minvalue=1)
        if numero_palabras:
            palabras_mas_comunes = frecuencias.most_common(numero_palabras)
            self.result_label.config(text=f"Las {numero_palabras} palabras más usadas y sus frecuencias:\n" +
                                      '\n'.join([f"{palabra}: {frecuencia} veces" for palabra, frecuencia in palabras_mas_comunes]))

            n = simpledialog.askinteger("Input", "Ingrese la cantidad para los n-gramas:", minvalue=2, maxvalue=4)
            if n:
                tamaño = simpledialog.askinteger("Input", "Ingrese la cantidad de palabras a generar", minvalue=1)
                if tamaño:
                    ngramas = construir_ngramas(palabras, n)
                    frecuencias_ngramas = contar_frecuencias_ngramas(ngramas)

                    imprimir = 'Había'
                    historial = [imprimir] * n

                    with open('texto_generado_y_conteo.txt', 'w', encoding='utf-8') as archivo:
                        archivo.write(f"Las {numero_palabras} palabras más usadas y sus frecuencias:\n")
                        for palabra, frecuencia in palabras_mas_comunes:
                            archivo.write(f"{palabra}: {frecuencia} veces\n")
                        
                        archivo.write("\nTexto generado:\n")
                        archivo.write(imprimir + ' ')
                        for _ in range(tamaño - 1):
                            siguiente = predecir_palabra(ngramas, historial[-n:])
                            historial.append(siguiente)
                            archivo.write(siguiente + ' ')
                        archivo.write("\n\n")

                        archivo.write("Frecuencias de los n-gramas:\n")
                        for key, counter in frecuencias_ngramas.items():
                            archivo.write(f"{' '.join(key)}:\n")
                            for word, freq in counter.items():
                                archivo.write(f"  {word}: {freq} veces\n")

                    self.textLabel.pack(side=tk.RIGHT)
                    messagebox.showinfo("Éxito", "El texto y las palabras mas populares han sido correctamente guardadas.")

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()