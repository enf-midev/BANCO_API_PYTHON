#self.nome = atributos/ =n: argumentos  método construtor
#todo atribuuto que tiver um valor padrãpo deve ficar por ultimo
class Pessoa():
    def __init__(self,n,p,i):
        self.nome= n
        self.peso= p
        self.idade= i
        self.comendo=False
        self.andando=False
        self.dormindo=False
    def andar(self):
        if self.comendo == False:
           if self.dormindo == False:
               if self.andando == False:
                   print(f"{self.nome}. Foi andar.")
                   self.andando = True

               else:
                   print(f"{self.nome}Já esta andando..")
           else:
               print(f"{self.nome}Não pode andar, está dormindo.")
        else:
            print(f"{self.nome} Não pode andar, está comendo.")
    def comer(self):
         if self.andando == False:
            if self.dormindo == False:
                if self.comendo == False:
                    print(f"{self.nome}. Foi comer")
                    self.comendo=True
                else:
                    print(f"Já está comendo.")
            else:
                print(f"Não pode comer, está dormindo.")
         else:
            print(f"Não pode comer, está andando.")
    def dormir(self):
        if self.andando == False:
            if self.comendo == False:
                if self.dormindo == False:
                    print(f"{self.nome}. Foi dormir")
                    self.dormindo = True
                else:
                    print(f"Já está dormindo.")
            else:
                print(f"Não pode dormir, está comendo.")
        else:
            print(f"Não pode dormir, está andando.")
    def parar_andar(self):
        if self.andando == True:
            print(f"Parou de andar.")
            self.andando = False


    def parar_comer(self):
        if self.comendo == True:
            print(f"Parou de comer.")
            self.comendo = False

    def acordando(self):
        if self.acordando == True:
            print(f"Acordou.")
            self.acordando = False




class Animal():
    def __init__(self,nome,cor):
        self.nome= nome
        self.cor= cor

    def comer(self):
        print(f"O {self.nome} está comendo..")

class Gato(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def miar(self):
        print(f"O {self.nome} está miando..")

class Cachorro(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def latir(self):
        print(f"O {self.nome} está latindo..")

    def comer(self):
        print(f"O cachorro {self.nome} esta comer..")

class Vaca(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def mungir(self):
        print(f"O {self.nome} está mugindo..")

class Coelho(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def chia(self):
        print(f"O {self.nome} está chiando..")

class Atleta():
    def __init__(self,nome,peso):
        self.aposentado=False
        self.peso=peso
        self.nome = nome
        self.aquecendo=False
    def aposentar(self):
       if self.aposentado == False:
            print(f"O {self.nome} foi aposentado com sucesso..")
            self.aposentado = True
       else:
           print(f"não pode aposentar {self.nome}, pois já está aposentado.")
    def aquecer(self):
        if self.aquecendo == False:
            if self.aposentado == False:
                print(f" {self.nome} aqueceu.")
                self.aquecendo = True
            else:
                print(f"{self.nome} não pode aquecer pq já está aposentado.")
        else:
            print(f" {self.nome} não pode aquecer pq já está aquecendo.")
class Corredor(Atleta):
    def __init__(self,nome,peso):
        super().__init__(nome,peso)
    def correr(self):
        if self.aquecendo == True:
            print(f"{self.nome} está correndo..")
        else:
            print(f"{self.nome} não pode correr, ainda não aqueceu.")
class Nadador(Atleta):
    def __init__(self,nome,peso):
        super().__init__(nome,peso)
    def nadar(self):
        if self.aquecendo == True:
            print(f"{self.nome} está nadando..")
        else:
            print(f"{self.nome} não pode nadar, ainda não aqueceu.")
class Ciclista(Atleta):
    def __init__(self,nome,peso):
        super().__init__(nome,peso)
    def pedalar(self):
        if self.aquecendo == True:
            print(f"{self.nome} está pedalando..")
        else:
            print(f"{self.nome} não pode pedalar, ainda não aqueceu.")

class Triatleta(Ciclista, Nadador, Corredor):
    def __init__(self,nome,peso):
        super().__init__(nome,peso)


def cadastrar(t):
    with open("teste01.txt", "a") as arq:
        arq.write(f"{t}\n")

def mostrar():
    with open("teste01.txt","r") as arq2:
        texto2 = arq2.read()
        print(texto2)

def pesquisar (texto):
    cont=0
    with open("teste01txt","r") as arquivo:
        for x in arquivo:
            if texto in x:
                cont+=1
    print(cont)


import requests

def endereco(cep):

    if len(cep)==8:
        link =f'https://viacep.com.br/ws/{cep}/json/'
        requisicao = requests.get(link)
        print(requisicao)
        dic_requisicao = requisicao.json()

        cep = dic_requisicao['cep']
        lagradouro = dic_requisicao['lagradouro']
        complemento = dic_requisicao['complemento']
        #print(dic_requisicao)

    else:
        print("CEP INVÁLIDO")