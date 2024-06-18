import tkinter as tk

root = tk.Tk()
root.title("Ejemplo de Frame")

# Crear un frame
frame1 = tk.Frame(root, bg="lightblue", bd=10)
frame1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Crear otro frame
frame2 = tk.Frame(root, bg="lightgreen", bd=10)
frame2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Agregar widgets al primer frame
label1 = tk.Label(frame1, text="Frame 1", bg="lightblue")
label1.pack(padx=10, pady=10)

button1 = tk.Button(frame1, text="Botón 1")
button1.pack(padx=10, pady=10)

# Agregar widgets al segundo frame
label2 = tk.Label(frame2, text="Frame 2", bg="lightgreen")
label2.pack(padx=10, pady=10)

button2 = tk.Button(frame2, text="Botón 2")
button2.pack(padx=10, pady=10)

root.mainloop()