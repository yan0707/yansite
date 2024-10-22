# importando a biblioteca do Flaskpara fazer um site dinâmico
from flask import Flask, render_template, request

app= Flask(__name__)

#definindo a rota pricipal do site
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/música")
def música():
    return render_template("música.html")

@app.route("/principal")
def principal():
    return render_template("principal.html")
# Parte pricipaldo programa em Python
if __name__== '__main__':
    app.run(debug=True)