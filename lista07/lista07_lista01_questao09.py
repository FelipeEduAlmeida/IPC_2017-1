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
# Criar um algoritmo que leia os elementos de uma matriz inteira 10 x 10 e escreva
# somente os elementos acima da diagonal secund�ria.

matriz = []

for i in range (10):
    
    matriz.append([0]*10)
    
    for j in range (10):
        
        matriz[i][j] = int(input())
        
for i in range (10):
    
    for j in range (10):
        
        if i + j < 9:
            
            print(matriz[i][j])
