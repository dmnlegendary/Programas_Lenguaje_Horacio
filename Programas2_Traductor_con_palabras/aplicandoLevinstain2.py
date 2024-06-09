import tkinter as tk
from tkinter import messagebox
import Levenshtein as lev

# Lista de palabras correctas (puedes añadir más palabras a esta lista)
correct_words = ["hola", "mundo", "programación", "python", "corrección", "ejemplo", "palabra"]

# Variables globales para almacenar las sugerencias y el índice actual
suggestions = []
current_index = 0

def get_suggestions(word):
    global suggestions, current_index
    # Ordena las palabras correctas por su distancia de Levenshtein a la palabra ingresada
    suggestions = sorted(correct_words, key=lambda w: lev.distance(word, w))
    current_index = 0
    return suggestions

def correct_word():
    input_word = entry.get()
    suggestions = get_suggestions(input_word)
    if suggestions:
        result_label.config(text=f"Quizás quisiste decir: {suggestions[0]}")
        if input_word != suggestions[0]:
            messagebox.showinfo("Corrección", f"Palabra sugerida: {suggestions[0]}")
    else:
        result_label.config(text="No se encontraron sugerencias.")

def next_suggestion():
    global current_index
    if suggestions:
        current_index = (current_index + 1) % len(suggestions)
        next_word = suggestions[current_index]
        result_label.config(text=f"Quizás quisiste decir: {next_word}")
        messagebox.showinfo("Corrección", f"Siguiente sugerencia: {next_word}")
    else:
        result_label.config(text="No se encontraron sugerencias adicionales.")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Corrector de Palabras")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Ingresa una palabra:")
label.pack(padx=5, pady=5)

entry = tk.Entry(frame)
entry.pack(padx=5, pady=5)

button = tk.Button(frame, text="Corregir", command=correct_word)
button.pack(padx=5, pady=5)

next_button = tk.Button(frame, text="Siguiente Sugerencia", command=next_suggestion)
next_button.pack(padx=5, pady=5)

result_label = tk.Label(frame, text="")
result_label.pack(padx=5, pady=5)

root.mainloop()
