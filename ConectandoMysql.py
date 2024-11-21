import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="turmaa")

meucursor = banco.cursor()
pesquisa = 'select*from alunos;'
meucursor.execute(pesquisa)
#fetchall recebe tudo da pesquisa e retorna atráves de uma tupla
resultado = meucursor.fetchall()
for x in resultado:
    print(x)

nome = input("Digite sue nome: ")
telefone = input("Informe seu número: " )

sql = "insert into alunos(nome, telefone) values (%s,%s);"
data = (nome, telefone)
meucursor.execute(sql,data)
banco.commit()

meucursor.close()
banco.close()