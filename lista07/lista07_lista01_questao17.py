#----------------------------------------------------------------------------------------------------------------------
# Introdu��o a Programa��o de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Diogo Duarte  1715310056
# Dayana Pican�o 1715310058
# Walter Nobre 
matriz = []

for i in range(5):
    linha = []
    linha.append(raw_input("Nome da funcion�ria: "))
    linha.append(int(input("quantas 'm�os' ela f�z: "))*10)
    linha.append(int(input("quantos p�s: "))*15)
    linha.append(int(input("quantos servi�os de podologia: "))*30)
    matriz.append(linha)
for i in range(5):
    print("salario da %s: ") % matriz[i][0]
    print(matriz[i][1]+matriz[i][2]+matriz[i][3])
