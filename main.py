import sys
from tkinter import ttk
import tkinter as tk

root = tk.Tk()


def crearArchivo():
    newWindow = tk.Toplevel(root)
    newWindow.geometry('300x300')
    newWindow.title("Crear Archivo")

    label = tk.Label(newWindow, text="Escriba la ruta donde se creara el archivo")
    entry = tk.Entry(newWindow)
    label = tk.Label(newWindow, text="Crear")
    kill = tk.Button(newWindow, text="Salir", command= lambda: newWindow.destroy())
    label.pack(padx=10, pady=10)
    entry.pack()
    kill.pack()
    newWindow.focus_set()


class Gui:
    def __init__(self, root):
        root.title("Gestion de archivos")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        ttk.Label(mainframe, text="Selecciona una opción").grid(
            column=0, row=0, sticky=(tk.N))
        ttk.Button(mainframe, text="1. Crear un archivo en el directorio actual", command=crearArchivo).grid(
            column=0, row=1, sticky=(tk.N))
        ttk.Label(mainframe, text="2. Copiar archivo a otro directorio").grid(
            column=0, row=2, sticky=(tk.N))
        ttk.Label(mainframe, text="3. Añadir texto a un archivo (simple edición)").grid(
            column=0, row=3, sticky=(tk.N))
        ttk.Label(mainframe, text="4. Comparar archivos en un directorio").grid(
            column=0, row=4, sticky=(tk.N))
        ttk.Label(mainframe, text="5. Concatenar 2 archivos").grid(
            column=0, row=5, sticky=(tk.N))
        ttk.Label(mainframe, text="6. Ocurrencias de palabras en un archivo").grid(
            column=0, row=6, sticky=(tk.N))
        ttk.Label(mainframe, text="7. Hacer archivo ejecutable").grid(
            column=0, row=7, sticky=(tk.N))
        ttk.Label(mainframe, text="8. Cambiar el propietario de un archivo").grid(
            column=0, row=8, sticky=(tk.N))
        ttk.Label(mainframe, text="9. Cambiar el archivo de un grupo").grid(
            column=0, row=9, sticky=(tk.N))
        ttk.Label(mainframe, text="10. Cambiar el nombre de un archivo").grid(
            column=0, row=10, sticky=(tk.N))
        ttk.Label(mainframe, text="11. Encriptar y desencriptar un archivo").grid(
            column=0, row=11, sticky=(tk.N))
        ttk.Button(mainframe, text="Salir", command=exit).grid(
            column=0, row=12, sticky=(tk.N))


if __name__ == "__main__":
    Gui(root)
    root.mainloop()
