# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# tiago ferreira aranha 	                1715310047
# Luiz Daniel Raposo Nunes de Mello	        1715310049
# Gabriel nascimento de Oliveira            1715310052
# Wilbert Luís Evangelista Marins           1715310055
# Mackson Garcez Moreno de Oliveira júnior  1215090300
# Edson de Lima Barros                      1715310043
# Renan de Almeida Campos                   0825060036
#
# 4 - Desenhar um polígono com 6 lados iguais. Cada lado uma cor diferente
# ----------------------------------------------------------

import turtle

quantidade_lados = 6

cores = ['orange', 'green', 'purple', 'blue', 'red', 'brown']

p = turtle.Pen()

for x in range(quantidade_lados):
    p.pencolor(cores[x])
    p.forward(80)
    p.left(360 / quantidade_lados)