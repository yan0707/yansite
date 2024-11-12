import sqlite3

#Função que conecta o banco de dados
def conectar_banco():
    # Conectar ao banco ou criar se não existir
    conexao = sqlite3.connect('meu_bacno.db')
    cursor = conexao.cursor()

    # parte principal do programa
    if__name__=='__main__':
    conectar_banco()