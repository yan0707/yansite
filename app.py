# importando a biblioteca do Flaskpara fazer um site dinâmico
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "chave_muito_segura"
#Cria uma lista de usúario e senha, depois vamos pegar o DB
usuarios = {
    'yan' : '0907',
    'Rayanna' : '1906' 
}
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


@app.route("/canal")
def canal():
    return render_template("canal.html")


    #verificar login
@app.route('/verificar_login', methods=['POST'])
def verificar_login():

    #pegando o qe o usuario digitou no campo de entrada de user e senha
    username = request.form['usuario']
    password = request.form['senha']

    #verifica se o usuario digitado está na lista e se a senha está correta
    if username in usuarios and usuarios[username] == password:
            return redirect(url_for("principal"))
    else:
            #Flash envia mensagempara o front-end
            flash('Usuário ou senha incorretos','danger')
            return redirect(url_for('login'))
    
# Parte pricipal do programa em Python
if __name__== '__main__':
    app.run(debug=True)