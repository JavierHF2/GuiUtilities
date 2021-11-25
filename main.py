import shutil
import os
from tkinter import ttk
import tkinter as tk

root = tk.Tk()


def cambiarpropietarioArchivo():
    newWindow = tk.Toplevel(root)
    newWindow.geometry("300x300")
    newWindow.title("Cambiar propietario")

    texto_propietario_archivo = tk.Label(
        newWindow, text="¿Cual sera el nuevo propietario?"
    )
    ruta_propietario_archivo = tk.Entry(newWindow)
    texto_ruta_origen = tk.Label(newWindow, text="¿Cual es la ruta del archivo?")
    ruta_origen_archivo = tk.Entry(newWindow)
    texto_grupo_archivo = tk.Label(newWindow, text="¿Cual seria el nuevo grupo?")
    ruta_grupo_archivo = tk.Entry(newWindow)

    cambiar_archivo_grupo_boton = tk.Button(
        newWindow,
        text="Cambiar grupo",
        command=lambda: os.chown(
            int(ruta_origen_archivo.get()),
            ruta_propietario_archivo.get(),
            int(ruta_grupo_archivo.get()),
        ),
    )

    boton_cerrar_ventana = tk.Button(
        newWindow, text="Salir", command=lambda: newWindow.destroy()
    )

    texto_propietario_archivo.pack()
    ruta_propietario_archivo.pack()
    texto_ruta_origen.pack()
    ruta_origen_archivo.pack()
    texto_grupo_archivo.pack()
    ruta_grupo_archivo.pack()
    cambiar_archivo_grupo_boton.pack()
    boton_cerrar_ventana.pack()


def concatenarArchivos():
    newWindow = tk.Toplevel(root)
    newWindow.geometry("300x300")
    newWindow.title("Concatenar Archivos")


def mostrarArchivos():
    newWindow = tk.Toplevel(root)
    newWindow.geometry("300x300")
    newWindow.title("Mostrar Archivos")

    boton_cerrar_ventana = tk.Button(
        newWindow, text="Salir", command=lambda: newWindow.destroy()
    )
    flist = os.listdir()
    lbox = tk.Listbox(newWindow)
    lbox.pack()
    boton_cerrar_ventana.pack()

    for item in flist:
        lbox.insert(tk.END, item)


def editarArchivo():
    newWindow = tk.Toplevel(root)
    newWindow.geometry("300x300")
    newWindow.title("Editar Archivo")

    texto_ruta_archivo = tk.Label(newWindow, text="¿Qué archivo se le añadira texto?")
    ruta_origen_texto = tk.Entry(newWindow)
    texto_apender_texto_origen = tk.Label(newWindow, text="¿Qué se le añadira?")
    apender_texto_origen = tk.Entry(newWindow)
    editar_archivo_boton = tk.Button(
        newWindow,
        text="Editar",
        command=lambda: open(ruta_origen_texto.get(), "a").write(
            apender_texto_origen.get()
        ),
    )
    boton_cerrar_ventana = tk.Button(
        newWindow, text="Salir", command=lambda: newWindow.destroy()
    )

    texto_ruta_archivo.pack()
    ruta_origen_texto.pack()
    texto_apender_texto_origen.pack()
    apender_texto_origen.pack()
    editar_archivo_boton.pack()
    boton_cerrar_ventana.pack()
    newWindow.focus_set()


def copiarArchivo():
    newWindow = tk.Toplevel(root)
    newWindow.geometry("300x300")
    newWindow.title("Copiar Archivo")

    texto_ruta_origen = tk.Label(newWindow, text="Escriba la ruta de origen")
    ruta_origen_texto = tk.Entry(newWindow)
    texto_ruta_destino = tk.Label(newWindow, text="Escriba la ruta de destino")
    ruta_destino_texto = tk.Entry(newWindow)
    copiar_archivo_boton = tk.Button(
        newWindow,
        text="Copiar Archivo",
        command=lambda: shutil.copyfile(
            ruta_origen_texto.get(), ruta_destino_texto.get()
        ),
    )
    boton_cerrar_ventana = tk.Button(
        newWindow, text="Salir", command=lambda: newWindow.destroy()
    )

    texto_ruta_origen.pack()
    ruta_origen_texto.pack()
    texto_ruta_destino.pack()
    ruta_destino_texto.pack()
    copiar_archivo_boton.pack()
    boton_cerrar_ventana.pack()
    newWindow.focus_set()


def crearArchivo():
    newWindow = tk.Toplevel(root)
    newWindow.geometry("300x300")
    newWindow.title("Crear Archivo")

    texto_nombre_origen = tk.Label(newWindow, text="Escriba el nombre del archivo")
    ruta_entrada_texto = tk.Entry(newWindow)
    texto_ruta_origen = tk.Label(newWindow, text="Escriba su ruta de creación")
    ruta_archivo_texto = tk.Entry(newWindow)
    crear_archivo_boton = tk.Button(
        newWindow,
        text="Crear archivo",
        command=lambda: os.system(
            "touch {0} && mkdir {1} && mv {0} {1} ".format(
                ruta_entrada_texto.get(), ruta_archivo_texto.get()
            )
        ),
    )
    boton_cerrar_ventana = tk.Button(
        newWindow, text="Salir", command=lambda: newWindow.destroy()
    )

    texto_nombre_origen.pack()
    ruta_entrada_texto.pack()
    texto_ruta_origen.pack()
    ruta_archivo_texto.pack()
    crear_archivo_boton.pack()
    boton_cerrar_ventana.pack()
    newWindow.focus_set()


class Gui:
    def __init__(self, root):
        root.title("Gestion de archivos")
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        ttk.Label(mainframe, text="Selecciona una opción").grid(
            column=0, row=0, sticky=(tk.N)
        )
        ttk.Button(
            mainframe,
            text="1. Crear un archivo",
            command=crearArchivo,
        ).grid(column=0, row=1, sticky=(tk.N))
        ttk.Button(
            mainframe, text="2. Copiar archivo a otro directorio", command=copiarArchivo
        ).grid(column=0, row=2, sticky=(tk.N))
        ttk.Button(
            mainframe,
            text="3. Añadir texto a un archivo (simple edición)",
            command=editarArchivo,
        ).grid(column=0, row=3, sticky=(tk.N))
        ttk.Button(
            mainframe,
            text="4. Comparar archivos en un directorio",
            command=mostrarArchivos,
        ).grid(column=0, row=4, sticky=(tk.N))
        ttk.Button(
            mainframe, text="5. Concatenar 2 archivos", command=concatenarArchivos
        ).grid(column=0, row=5, sticky=(tk.N))
        ttk.Button(mainframe, text="6. Ocurrencias de palabras en un archivo").grid(
            column=0, row=6, sticky=(tk.N)
        )
        ttk.Button(mainframe, text="7. Hacer archivo ejecutable").grid(
            column=0, row=7, sticky=(tk.N)
        )
        ttk.Button(
            mainframe,
            text="8. Cambiar el propietario de un archivo",
            command=cambiarpropietarioArchivo,
        ).grid(column=0, row=8, sticky=(tk.N))
        ttk.Button(mainframe, text="9. Cambiar el archivo de un grupo").grid(
            column=0, row=9, sticky=(tk.N)
        )
        ttk.Button(mainframe, text="10. Cambiar el nombre de un archivo").grid(
            column=0, row=10, sticky=(tk.N)
        )
        ttk.Button(mainframe, text="11. Encriptar y desencriptar un archivo").grid(
            column=0, row=11, sticky=(tk.N)
        )
        ttk.Button(mainframe, text="Salir", command=exit).grid(
            column=0, row=12, sticky=(tk.N)
        )


if __name__ == "_main_":
    Gui(root)
    root.mainloop()
