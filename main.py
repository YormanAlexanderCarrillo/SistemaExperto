import tkinter as tk

from SistemaExpertoPeliculas import cargar_peliculas, SistemaExpertoPeliculas

if __name__ == '__main__':
    ruta_csv = "peliculas.csv"
    peliculas = cargar_peliculas(ruta_csv)

    root = tk.Tk()
    app = SistemaExpertoPeliculas(root, peliculas)
    root.mainloop()
