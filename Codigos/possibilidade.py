
#Quantos números de 4 dígitos eu posso fomrar com números de 0 a 9?
#
# 10 10 10 10
#
# Comninatória : 10X 10X 10 X 10 = 100000
#
#Permutação:
#
# 10 9 8 7
#
# Permutação : 10 X 9 X8 X 7 = 5040

#Simulação: Executar as possibilidades:
#
# PA - 1 2 3 4 5 6 7 8 .... 100 101 102 103
#
#Se eu jogar dois dados 1000 vezes, quantas vezes dará a soma 7?

import random

numero_de_vezes = 0

for n1 in range(1000): #n1 podendo ser substutuido por_
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2
    if soma == 7 or soma == 1:
        numero_de_vezes += 1

print(f'A soma dos dados deu 7 {numero_de_vezes} vezes')



contador = 0

'''
for n1 in range(10): #For dentro de for - Multiplica o número de vezes que o código vai rodar
    for n2 in range(10):
        for n3 in range(10):
            for n4 in range(10):
                #print(f'{n1}{n2}{n3}{n4}')
                contador += 1
'''

for n1 in range(10): #For dentro de for - Multiplica o número de vezes que o código vai rodar
    for n2 in range(10):
        if n2 == n1:
            continue
        for n3 in range(10):
            if n3 == n1 or n3 == n2:
                continue
            for n4 in range(10):
                if n4 == n1 or n4 == n2 or n4 == n3:
                    continue
                contador += 1 




print(contador)