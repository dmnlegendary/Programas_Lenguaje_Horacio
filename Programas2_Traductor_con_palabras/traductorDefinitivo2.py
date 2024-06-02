import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

def translate_text():
    try:
        text_to_translate = input_text.get("1.0", tk.END)
        source_lang = source_lang_combobox.get()
        target_lang = target_lang_combobox.get()
        
        translator = Translator()
        translated = translator.translate(text_to_translate, src=source_lang, dest=target_lang)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated.text)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# Crear la ventana principal
root = tk.Tk()
root.title("Traductor")

# Crear el marco principal
main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Etiquetas y campos de entrada
ttk.Label(main_frame, text="Texto a traducir:").grid(row=0, column=0, sticky=tk.W)
input_text = tk.Text(main_frame, width=50, height=10)
input_text.grid(row=1, column=0, columnspan=2)

ttk.Label(main_frame, text="Idioma de origen:").grid(row=2, column=0, sticky=tk.W)
source_lang_combobox = ttk.Combobox(main_frame, values=list(LANGUAGES.keys()), width=20)
source_lang_combobox.grid(row=2, column=1)
source_lang_combobox.set('auto')

ttk.Label(main_frame, text="Idioma de destino:").grid(row=3, column=0, sticky=tk.W)
target_lang_combobox = ttk.Combobox(main_frame, values=list(LANGUAGES.keys()), width=20)
target_lang_combobox.grid(row=3, column=1)
target_lang_combobox.set('en')

# Botón para traducir
translate_button = ttk.Button(main_frame, text="Traducir", command=translate_text)
translate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Etiqueta y campo de salida
ttk.Label(main_frame, text="Texto traducido:").grid(row=5, column=0, sticky=tk.W)
output_text = tk.Text(main_frame, width=50, height=10)
output_text.grid(row=6, column=0, columnspan=2)

# Ajustar el redimensionamiento
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)

# Iniciar la aplicación
root.mainloop()
