import tkinter as tk
from tkinter import messagebox
import csv

class SistemaExpertoPeliculas:

    def __init__(self, root, peliculas):
        self.root = root
        self.root.title("Sistema experto de recomendacion de peliculas")
        self.root.geometry("450x600")
        self.root.resizable(False, False)
        self.genero = tk.StringVar()
        self.edad = tk.IntVar()
        self.calificacion = tk.IntVar()
        self.ano = tk.IntVar()
        self.resultado = tk.StringVar()
        # Lista de géneros posibles
        generos_posibles = ["Acción", "Animación", "Aventura", "Ciencia Ficción", "Comedia", "Crimen", "Drama", "Familiar", "Musical", "Romance", "Terror", "Western"]

        tk.Label(root, text="Genero prefefido:").grid(row=0, column=0, padx=10, pady=10)
        tk.OptionMenu(root, self.genero, *generos_posibles).grid(row=0, column=1, padx=10, pady=10)

        tk.Label(root, text="Edad:").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.edad).grid(row=1, column=1, padx=10, pady=10)

        tk.Label(root, text="Calificacion:").grid(row=2, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.calificacion).grid(row=2, column=1, padx=10, pady=10)

        tk.Label(root, text="Año de lanzamiento:").grid(row=3, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.ano).grid(row=3, column=1, padx=10, pady=10)

        tk.Button(root, text="Recomendar Peliculas", command=self.recomendar_pelicula).grid(row=4, column=0, columnspan=2, pady=10)

        tk.Label(root, text="Recomendacion:").grid(row=5, column=0, padx=10, pady=10)
        tk.Label(root, textvariable=self.resultado).grid(row=5, column=1, padx=10, pady=10)
        self.peliculas = peliculas

    def recomendar_pelicula(self):
        genero = self.genero.get().lower()
        edad = self.edad.get()
        calificacion = self.calificacion.get()
        anio = self.ano.get()

        peliculasFiltradas = [p for p in self.peliculas if
                             p["Género"].lower() == genero and
                             int(p["Edad"]) <= edad and
                             int(p["Calificación"]) >= calificacion and
                             int(p["Año"]) >= anio]
        if peliculasFiltradas:
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

