import tkinter as tk
from tkinter import ttk

def traducir():
    # Aquí iría la lógica para traducir el texto.
    # Reemplazar con la llamada a tu función/método de traducción.
    texto_origen = texto_entrada.get("1.0", "end-1c")
    texto_traducido.delete("1.0", "end")
    texto_traducido.insert("1.0", texto_origen)  # Ejemplo: copia el texto

root = tk.Tk()
root.title("Traductor Evolutivo")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

texto_entrada = tk.Text(frame, height=10, width=50)
texto_entrada.grid(row=0, column=0, columnspan=2, pady=10)

idioma_origen = ttk.Combobox(frame, values=["Español", "Inglés"])
idioma_origen.grid(row=1, column=0, sticky=tk.W, padx=5)
idioma_origen.set("Español")

idioma_destino = ttk.Combobox(frame, values=["Inglés", "Español"])
idioma_destino.grid(row=1, column=1, sticky=tk.W, padx=5)
idioma_destino.set("Inglés")

boton_traducir = ttk.Button(frame, text="Traducir", command=traducir)
boton_traducir.grid(row=2, column=0, columnspan=2, pady=10)

texto_traducido = tk.Text(frame, height=10, width=50, state="disabled")
texto_traducido.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()