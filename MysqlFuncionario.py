import requests
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="turmaa")

meucursor = banco.cursor()
cep = input("Digite seu cep: ")
if len(cep) == 8:
    link = f'https://viacep.com.br/ws/{cep}/json/'
    requisicao = requests.get(link)
    print(requisicao)
    dic_requisicao = requisicao.json()

    cep = dic_requisicao['cep']
    lagradouro = dic_requisicao['logradouro']
    complemento = dic_requisicao['complemento']
    # print(dic_requisicao)

    sql = ("insert into endereco(cep, lagradouro, complemento) values (%s,%s,%s);")
    data = (cep,lagradouro, complemento)
    meucursor.execute(sql,data)
    banco.commit()
    meucursor.close()
    banco.close()
else:
    print("CEP INVÁLIDO")

