import tkinter as tk
from tkinter import messagebox
import csv


class SistemaExpertoPeliculas:

    def __init__(self, root, peliculas):
        self.root = root
        self.root.title("Sistema experto de recomendacion de peliculas")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        self.genero = tk.StringVar()
        self.edad = tk.IntVar()
        self.resultado = tk.StringVar()

        tk.Label(root, text="Genero prefefido:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.genero).grid(row=0, column=1, padx=10, pady=10)

        tk.Label(root, text="Edad:").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.edad).grid(row=1, column=1, padx=10, pady=10)

        tk.Button(root, text="Recomendar Peliculas", command=self.recomendar_pelicula).grid(row=2, column=0, columnspan=2, pady=10)

        tk.Label(root, text="Recomendacion:").grid(row=3, column=0, padx=10, pady=10)
        tk.Label(root, textvariable=self.resultado).grid(row=3, column=1, padx=10, pady=10)
        self.peliculas = peliculas

    def recomendar_pelicula(self):
        genero = self.genero.get().lower()
        edad = self.edad.get()

        peliculasFiltradas = [p for p in self.peliculas if p["Género"].lower() == genero and int(p["Edad"]) <= edad]
        print(peliculasFiltradas)
        if peliculasFiltradas:
            # resultado = peliculasFiltradas[0]["Título"]
            # for pf in peliculasFiltradas:
            #     resultado += pf["Título"]
            resultado = "\n".join(pf["Título"] for pf in peliculasFiltradas)
        else:
            resultado = "Lo siento no hay recomendaciones disponibles"

        self.resultado.set(resultado)


def cargar_peliculas(ruta):
    peliculas = []
    with open(ruta, newline="", encoding="utf-8") as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            peliculas.append(fila)
    return peliculas
