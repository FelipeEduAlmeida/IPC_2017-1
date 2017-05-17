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
# Criar um algoritmo que leia uma matriz ANxN (N <= 10) e verifique (informe) se tal
# matriz � ou n�o sim�trica (At = A).

matriz = []
N = int(input())

for i in range (N):
    
    matriz.append([0]*N)
    
    for j in range (N):
        
        matriz[i][j] = int(input())
        
i = 0

while i < N:
    
    j = 0
    
    while j < N:
        
        if matriz[i][j] != matriz[j][i]:
        
            i = N
            j = N
        
        else:
            
            j += 1
        
    i += 1
    
if i == N:
    
    print("Matriz sim�trica")
    
else:
    
    print("Matriz n�o sim�trica")
