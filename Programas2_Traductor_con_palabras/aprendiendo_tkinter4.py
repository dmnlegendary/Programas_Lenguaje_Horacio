'''Apertura de ventana secundaria y posterior destruccion'''
import tkinter as tk
from tkinter import messagebox

def abrir_ventana_secundaria():
    ventana_secundaria = tk.Toplevel(root)
    ventana_secundaria.title("Ventana Secundaria")
    ventana_secundaria.geometry("300x200")

    lbl = tk.Label(ventana_secundaria, text="Esta es una ventana secundaria")
    lbl.pack(pady=20)

    btn_cerrar = tk.Button(ventana_secundaria, text="Cerrar Ventana", command=ventana_secundaria.destroy)
    btn_cerrar.pack(pady=10)

def cerrar_ventana_principal():
    if messagebox.askokcancel("Salir", "¿Estás seguro que quieres salir?"):
        root.destroy()

root = tk.Tk()
root.title("Ventana Principal")
root.geometry("400x300")

btn_abrir = tk.Button(root, text="Abrir Ventana Secundaria", command=abrir_ventana_secundaria)
btn_abrir.pack(pady=20)

btn_cerrar = tk.Button(root, text="Cerrar Ventana Principal", command=cerrar_ventana_principal)
btn_cerrar.pack(pady=20)

root.mainloop()