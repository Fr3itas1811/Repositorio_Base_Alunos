from os import system

def limpa_tela():
    system("cls")

def adiciona_nome(lista_nomes,nome):
    lista_nomes.append(nome)

def remover_nome(lista_nomes,nome):
        print()

def mostrar_nomes(lista_nomes):
            for nome in lista_nomes:
                print(nome)
nomes = []
while True:
    limpa_tela()
    menu = input("escolha sua opção:\n[1] - listar nomes\n[2] - adicionar nomes\n[3] - remover nomes\n[4 procua]\nsua opção: ")
    if menu == "0":
          break
    elif menu == "1":
          mostrar_nomes (nomes)
          input('aperte enter para continuar')
    elif menu == '2':
          nome_salvar = input("digite o nome que deseja salvar: ")
          adiciona_nome (nomes,nome_salvar)
    elif menu == "3":
          remover_nome = input("digite o nome que deseja remover: ")
          nomes.remove(nome_salvar)
    else:
          print("opção invalida. ")
          input("aperte enter para cntinuar")

nome_procurado = input("Digite o nome que deseja procurar: ").strip()
if nome_procurado in nomes:
        
    print(f"O nome '{nome_procurado}' está na lista.")
else:
    print(f"O nome '{nome_procurado}' não está na lista.")