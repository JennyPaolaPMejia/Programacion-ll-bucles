import shutil

from flask import Flask, render_template, request
import math
import subprocess
import os

app = Flask(__name__)


@app.route("/")
def inicio():

    return render_template("menu.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    matriz = None
    if request.method == "POST":
        n = int(request.form["numero"])
        matriz = []
        for i in range(n):
            fila = []
            for j in range(n):
                fila.append(0)
            matriz.append(fila)
        contador = 1
        arriba, abajo = 0, n-1
        izquierda, derecha = 0, n-1
        while contador <= n*n:
            for j in range(izquierda, derecha+1):
                matriz[arriba][j] = contador
                contador += 1
            arriba += 1
            for i in range(arriba, abajo+1):
                matriz[i][derecha] = contador
                contador += 1
            derecha -= 1
            for j in range(derecha, izquierda-1, -1):
                matriz[abajo][j] = contador
                contador += 1
            abajo -= 1
            for i in range(abajo, arriba-1, -1):
                matriz[i][izquierda] = contador
                contador += 1
            izquierda += 1
    return render_template("ejercicio1.html", matriz=matriz)


def generar_tablas(inicio, fin, incremento, modo):
    tablas = []
    for numero in range(inicio, fin+1):
        tabla = []
        if modo == "creciente":
            for i in range(1, 11, incremento):
                tabla.append(f"{numero} x {i} = {numero*i}")
        else:
            for i in range(10, 0, -incremento):
                tabla.append(f"{numero} x {i} = {numero*i}")
        tablas.append({
            "numero": numero,
            "operaciones": tabla
        })
    return tablas

@app.route("/ejercicio2", methods=["GET","POST"])
def ejercicio2():
    tablas = None
    if request.method == "POST":
        inicio = int(request.form["inicio"])
        fin = int(request.form["fin"])
        incremento = int(request.form["incremento"])
        modo = request.form["modo"]
        tablas = generar_tablas(inicio, fin, incremento, modo)
    return render_template("ejercicio2.html", tablas=tablas)
@app.route("/ejercicio3", methods=["GET","POST"])
def ejercicio3():
    video=None
    if request.method=="POST":
        x=request.form["x"]
        rc=request.form["rc"]
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        subprocess.run(
            [
                "manim",
                "animacion.py",
                "GraficaTaylor",
                "-pql",
                x,
                rc
            ],
            cwd=BASE_DIR
        )
        origen=os.path.join(
            BASE_DIR,
            "media",
            "videos",
            "animacion",
            "480p15",
            "GraficaTaylor.mp4"
        )
        destino=os.path.join(
            BASE_DIR,
            "static",
            "videos",
            "GraficaTaylor.mp4"
        )

        shutil.copy2(origen,destino)
        video="videos/GraficaTaylor.mp4"
    return render_template("ejercicio3.html", video=video)

if __name__ == "__main__":
    app.run(debug=True)