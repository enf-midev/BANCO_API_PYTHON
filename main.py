from Biblioteca import *
while True:
    opcao = int(input("Escolha uma opção:\n"
                      "1 para INSERIR\n"
                      "2 para MOSTRAR\n"
                      "3 para SAIR\n"
                      "4 para PESQUISAR."))
    match opcao:
        case 1:
            cadastrar (input("Informe o texto:"))
        case 2:
            mostrar()
        case 3:
            break
        case 4:
            pesquisar(input("Qual a palavra para pesquisar? "))
        case _:
            print("Opcção errada")


