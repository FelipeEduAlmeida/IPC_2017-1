# --------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# ULISSES ANTONIO ANTONINO DA COSTA  1515090555
# TIAGO FERREIRA ARANHA              1715310047
# VÍTOR SIMÕES AZEVEDO               1715310025
# VICTOR HUGO DE OLIVEIRA CARREIRA   1715310063
# REINALDO VARGAS                    1715310054
#
#7)Faça um programa que leia 5 números e informe o maior número.
#---------------------------------------------------------------------------

count = 1
number = 0
bigger = number

while count <= 5:
    number = float(input('Digite o número %.d ' % count))
    if number > bigger:
        bigger = number
    count = count + 1

print('O maior numero é: %.2f' % bigger)
