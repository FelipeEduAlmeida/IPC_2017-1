# ----------------------------------------------------------------------------------------------------------------------
# Introdu��o a Programa��o de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Gabriel barroso da Silva Lima                      1715310011
# Frederico Victor Alfaia Rodrigues                  1515200030
# Andr� Neves
# Diego Figueira
# Diogo Duarte
#
# Criar um algoritmo que entre com valores inteiros para uma matriz m 3 x 3 e imprima
# a matriz final rotacionada 90� graus

matriz = []

for i in range (3):
    
    matriz.append([0]*3)
    
    for j in range (3):
        
        matriz[i][j] = int(input())
        
valor = matriz[0][0]
matriz[0][0] = matriz[2][0]
matriz[2][0] = matriz[2][2]
matriz[2][2] = matriz[0][2]
matriz[0][2] = valor

valor = matriz[0][1]
matriz[0][1] = matriz[1][0] 
matriz[1][0] = matriz[2][1]
matriz[2][1] = matriz[1][2]
matriz[1][2] = valor

for i in range (3):
    
    print(matriz[i])
