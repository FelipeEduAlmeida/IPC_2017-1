# Biblioteca de funções para os vetores

import random


# lista 1 questão 1
def imprimir_questao1(n):
    res = ""
    c = 1

    for i in range(n):
        res += c * (str(i + 1) + " ") + "\n"
        c += 1

    return res


# lista 1 questao 10
# função que sorteia valores com dois dados
def jogar_dados():
    dados = [random.randint(1, 6), random.randint(1, 6)]
    dados = dados[0] + dados[1]
    return dados


# função para retornar uma lista a partir de uma entrada em sequência
# Ex.: Em um input: 4 10 PM, retornará a lista: ['4', '10', 'PM']

def get_as_uri(valores):
    valores = valores.split()

    return valores


# função para retornar uma lista de inteiros a partir de uma entrada em sequência
# Ex.: Em um input: 4 5 6 3 2, retornará a lista: [4, 5, 6, 3, 2]

def get_as_uri_inteiros(valores):
    valores = valores.split()
    valores_int = []

    for i in valores:
        valores_int.append(int(i))

    return valores_int


# usada na lista 2 questão 22
# função para criar vetor de tamanho n
def cria_vetor(n):
    vetor = []
    for j in range(n):
        # serão inseridos valores aleatórios na matriz (entre 1 e 4)
        value = random.rand(1, 4)
        vetor.append(value)
    return vetor


# função que gera números decimais aleatórios entre n e n
def gera_aleatorio_float(n, m):
    res = float('%2.1f' % (random.random() * random.randint(n, m)))
    return res


# função para criar vetor de tamanho n
def cria_vetor_numeros_decimais(n):
    vetor = []
    for j in range(n):
        # serão inseridos valores aleatórios na matriz (entre 1 e 4)
        value = gera_aleatorio_float(1, 4)
        vetor.append(value)
    return vetor


# função que encontra o maior elemento em um vetor
def maior_valor_do_vetor(vetor):
    maior = vetor[0]
    for i in vetor:
        if i > maior:
            maior = i
    return maior


# função que divide todos os elementos de um vetor por um número
def divide_todos_por_numero(vetor, numero):
    novo_vetor = []
    for i in vetor:
        novo_vetor.append("%2.3f" % (i / numero))
    return novo_vetor