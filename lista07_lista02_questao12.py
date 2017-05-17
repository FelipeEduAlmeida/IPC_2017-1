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
# Deseja-se fazer a emiss�o da folha de pagamento
# de uma empresa. Para cada um dos n funcion�rios
# da empresa s�o dadas as seguintes informa��es:
#
# NOME 
# SAL (sal�rio) 
# HED (horas extras diurnas) 
# HEN (horas extras noturnas) 
# ND (n�mero de dependentes) 
# FAL (faltas em horas) 
# DE (descontos eventuais) 
# REF (gastos com refei��es feitas na empresa) 
# VAL (vales retirados durante o m�s).
# 
# Emitir as seguintes informa��es:
#     
# nome, 
# sal�rio, 
# horas extras = HED * SAL/160 + HEN * 1.2 * SAL/160, 
# sal�rio fam�lia = ND * 0.05 * sal�rio m�nimo vigente, 
# sal�rio bruto = sal�rio + horas extras + sal�rio fam�lia.
# 
# Descontos efetuados:
#    
# INAMPS = 0.08 * SAL, 
# faltas = FAL * SAL/160, 
# refei��es, 
# vales, 
# descontos eventuais, 
# imposto de renda = 0.08 * sal�rio bruto.
# 
# Sal�rio l�quido = sal�rio bruto - desconto total. 

matriz = []
n = int(input())

for i in range (n):
    
    matriz.append([0]*9)
    
    matriz[i][0] = input("nome: ")
    matriz[i][1] = int(input("sal�rio: "))
    matriz[i][2] = int(input("horas extras diurnas: "))
    matriz[i][3] = int(input("horas extras noturnas: "))
    matriz[i][4] = int(input("n�mero de dependentes: "))
    matriz[i][5] = int(input("faltas em horas: "))
    matriz[i][6] = int(input("descontos eventuais: "))
    matriz[i][7] = int(input("gastos com refei��es feitas na empresa: "))
    matriz[i][8] = int(input("vales retirados durante o m�s: "))

print(".")

for i in range (n):
    
    exhoras = (matriz[i][2] * matriz[i][1]) / 160  + (matriz[i][3] * 1.2 * matriz[i][1]) / 160
    salfami = matriz[i][4] * 937 * 0.05
    salbruto = matriz[i][1] + exhoras + salfami
    INAMPS = 0.08 * matriz[i][1] 
    faltas = (matriz[i][5] * matriz[i][1])/160
    impren = salbruto * 0.08
    destot = faltas + INAMPS + impren + matriz[i][6] + matriz[i][7] + matriz[i][8]
    salliq = salbruto - INAMPS - faltas
    
    print("--//--//--//--//--//--//--//--//--//--//--//--")
    print("funcion�rio", n)
    print("sal�rio:", matriz[i][1])
    print("horas extras:", exhoras)
    print("sal�rio fam�lia:", salfami)
    print("sal�rio bruto:", salbruto)
    print("...........................")
    print("Descontos efetuados")
    print("INAMPS:", INAMPS)
    print("faltas:", faltas)
    print("imposto de renda:", impren)
    print("descontos totais:", destot)
    print("...........................")
    print("sal�rio l�quido:", salliq)
    print("--//--//--//--//--//--//--//--//--//--//--//--")