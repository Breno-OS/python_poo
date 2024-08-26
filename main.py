import pickle
import traceback

from common import *

FILE_ELEITORES = 'eleitores.pkl'
FILE_CANDIDATOS = 'candidatos.pkl'


def menu_candidato():
    print("1-Novo Candidato")
    print("2-Listar Candidatos")

    op = int(input("Digite a opcao [1,2]? "))
    while op not in (1, 2):
        op = int(input("Digite a opcao [1,2]? "))
    return op

def menu_eleitor():
    print("1-Novo Eleitor")
    print("2-Atualizar Eleitor")
    print("3-Sair")

    op = int(input("Digite a opcao [1,2,3]? "))
    while op not in (1, 2, 3, 4):
        op = int(input("Digite a opcao [1,2,3]? "))
    return op

def inserir_eleitor(eleitores):
    titulo = int(input("Digite o Títlulo: "))

    if titulo in eleitores:
        raise Exception("Titulo já existente!")

    nome = input("Digite o nome: ")
    RG = input("Digite o RG: ")
    CPF = input("Digite o CPF: ")
    secao = input("Digite a secao: ")
    zona = input("Digite a zona: ")

    eleitor = Eleitor(nome, RG, CPF, titulo, secao, zona)
    eleitores[eleitor.get_titulo()] = eleitor

    with open(FILE_ELEITORES, 'wb') as arquivo:
        pickle.dump(eleitores, arquivo)

    print('Eleitor gravado com sucesso!')
    print(eleitor)

def atualizar_eleitor(eleitores):
    titulo = int(input('Digite o titulo do eleitor: '))

    if titulo in eleitores:
        eleitor = eleitores[titulo]
        print(eleitor)
        secao = input("Digite a nova secao: ")
        zona = input("Digite a nova zona: ")
        eleitor.secao = secao
        eleitor.zona = zona

        with open(FILE_ELEITORES, 'wb') as arquivo:
            pickle.dump(eleitores, arquivo)

        print('Atualizados dados do eleitor!')
        print(eleitor)
    else:
        raise Exception('Titulo inexistente')

def inserir_candidato(candidatos):
    numero = int(input("Digite o Número: "))

    if numero in candidatos:
        raise Exception("Candidato já existente!")

    nome = input("Digite o nome: ")
    RG = input("Digite o RG: ")
    CPF = input("Digite o CPF: ")

    candidato = Candidato(nome, RG, CPF, numero)
    candidatos[candidato.get_numero()] = candidato

    with open(FILE_CANDIDATOS, 'wb') as arquivo:
        pickle.dump(candidatos, arquivo)

    print('Candidato gravado com sucesso!')
    print(candidato)

def listar_candidatos(candidatos):
    for c in candidatos.values():
        print(c)

if __name__ == "__main__":
    eleitores = {} #dicionário a chave será o titulo
    candidatos = {}  # dicionário a chave será o titulo
    try:
        print("Carregando dados ...")

        with open(FILE_ELEITORES, 'rb') as arquivo:
            eleitores = pickle.load(arquivo)
        with open(FILE_CANDIDATOS, 'rb') as arquivo:
            candidatos = pickle.load(arquivo)
    except FileNotFoundError as fnfe:
        print(fnfe)
        print("Arquivo nao encontrado, nenhum eleitor carregado!")

    opcao = 1
    while opcao in (1,2,3):
        try:
            op_usr = 0
            while op_usr not in ("1", "2"):
                op_usr = input("Menu Eleitor - 1\nMenu Candidato - 2\n\nDigite a opção: ")
            if op_usr == "1":
                opcao = menu_eleitor()
                if op_usr == 1:
                    inserir_eleitor(eleitores)
                elif opcao == 2:
                    atualizar_eleitor(eleitores)
                elif opcao == 3:
                    print("Saindo!")
                    break
            else:
                opcao = menu_candidato()
                if opcao == 1:
                    inserir_candidato(candidatos)
                elif opcao == 2:
                    listar_candidatos(candidatos)
                else:
                    print("Saindo!")
                    break

        except Exception as e:
            #traceback.print_exc()
            print(e)