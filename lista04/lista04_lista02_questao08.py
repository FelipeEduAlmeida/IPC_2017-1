# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Tiago Ferreira Aranha                     1715310047
# Victor Hugo de Oliveira Carreira          1715310063
# 
# URI Online Judge | 1048
# Salary Increase
# --------------------------------------------------------------------------------------

employees_number = input()
worked_hours = input()
amount_per_hour = input()

SALARY = worked_hours * amount_per_hour

print "NUMBER = %i" % employees_number
print "SALARY = U$ %5.2f" % SALARY
