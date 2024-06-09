import tkinter as tk
from tkinter import messagebox
import Levenshtein as lev

# Lista de palabras correctas (puedes añadir más palabras a esta lista)
correct_words = ["hola", "mundo", "programación", "python", "corrección", "ejemplo", "palabra"]

def get_closest_word(word):
    # Encuentra la palabra más cercana en la lista de palabras correctas
    closest_word = min(correct_words, key=lambda w: lev.distance(word, w))
    return closest_word

def correct_word():
    input_word = entry.get()
    closest_word = get_closest_word(input_word)
    result_label.config(text=f"Quizás quisiste decir: {closest_word}")
    if input_word != closest_word:
        messagebox.showinfo("Corrección", f"Palabra sugerida: {closest_word}")

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

result_label = tk.Label(frame, text="")
result_label.pack(padx=5, pady=5)

root.mainloop()