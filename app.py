from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/acerca")
def acerca():
    return render_template("acerca.html")

@app.route("/contactos")
def contacto():
    return render_template("contactos.html")

@app.route("/servicios")
def servicios():
    return render_template("servicios.html")

@app.route("/equipo")
def equipo ():
    return render_template("equipo.html")

if __name__ == "__main__":
    app.run(debug=True)

