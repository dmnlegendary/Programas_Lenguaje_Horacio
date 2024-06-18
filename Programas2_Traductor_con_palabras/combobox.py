import tkinter as tk
from tkinter import ttk

def show_selection(event):
    selected_item = combobox.get()
    print("Seleccionaste:", selected_item)

root = tk.Tk()
root.title("Ejemplo de Combobox Completo")

# Crear un Combobox con valores y hacer que sea solo de lectura
combobox = ttk.Combobox(root, values=["Opción 1", "Opción 2", "Opción 3", "Opción 4"], state="readonly")
combobox.pack(padx=10, pady=10)
combobox.current(0)  # Selecciona la primera opción por defecto

# Configurar el evento de selección
combobox.bind("<<ComboboxSelected>>", show_selection)

root.mainloop()
