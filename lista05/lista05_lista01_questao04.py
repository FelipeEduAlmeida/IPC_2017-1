#----------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Evandro Padilha Barroso Filho     1715310009 
# Gabriel Barroso da Silva Lima     1715310011
# Frederico Victor Alfaia Rodrigues 1515200030 
# Felipe Eduardo Silva de Almeida   1715310031 
# Felipe Guerreiro De Mello         1315120052 
# Silas castro de Mendonça          1715310066
#
# Supondo que a população de um país A seja da ordem de 80000 habitantes 
# com uma taxa anual de crescimento de 3% e que a população de B seja 200000 
# habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule 
# e escreva o número de anos necessários para que a população do país A ultrapasse 
# ou iguale a população do país B, mantidas as taxas de crescimento.
#----------------------------------------------------------------

population_a = 80000
grow_a = 0.03
population_b = 200000
grow_b = 0.015
c = 0
while population_a <= population_b:
    population_a = population_a + (population_a * grow_a)
    population_b = population_b + (population_b * grow_b)
    c = c + 1
print("Será preciso", c ,"anos para o país A ser mais populoso que o país B")