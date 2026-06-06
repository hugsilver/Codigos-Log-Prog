# Tipos primitivos de dadso em Pyhton

# - int: números interios
# - float: números decimais (ponto flutuante)
# - str: cadeia de caracteres (texto)
# - bool: valores lógicos (True ou False)



# Operadores aritméticos: +,  -, * ...
#Operadores lógicos: and, or, not
#Operadores de strings: +, *

# Operadores de comparação
# recebem valores de diversos tipos e retornam um bool

# == igualdade
# != diferença
# > maior que
# < menor que
# >= maior ou igual a
# <= menor ou igual a

# // - Pega somentre a parte interia
# % - Resto da divisão 
# ** - Exponenciação 


#Lista - Uma estrutura de dados
#Da para desenvolver as proprias estrutura de dados
#
# Estruturtas de dados
# - Listas: conjunto de dados ordenados nutável

lista = [1, 4, 3, 4]
frutas = ['banana', 'maça']
mista = [1, 'texto', 5, True]

# - Tuplas: conunto de dados ordenados - imutável
coordenadas = (5, 6) #Corelação entre eles e a ordem faz diferença
tupla = (5, 4, 3, 2)

# - Dicionários (dict): conjunto de pares na forma chave e valor - Parecido com objeto do JS e Json
pessoas = {'nome': 'João', 'idade': 18}
carro = {
    'marca': 'Volks',
    'modelo': 'Fusca',
    'cor': 'azul',
    'ano': 1970
}

# - Conjuntos (sets): Conjunto de dados não ordenados e sem repetição - Usado principalmente no momento de ordenação
c1 = {1, 2, 3}
c2 = {3, 2, 1}
c3 = {1, 2, 2, 2, 2, 3, 3, 3}

#Usar o dir para ver capacidades do método

#
lista2 = [1,3, 56, 7, 9, 2, 3, 56]
s = set(lista2) # Retira as repetições e ordena - Não conhecia
print(s) #Conjunto
#Do método
#print(dir(set))
s = {2, 3, 4, 6, 7, 8, 42, 56}
s2 = {4, 8, 12, 16}
print(s2)

print(s&s2) # Intersseção - Está nos dois
print(s-s2)
print(s2 < s)
print(s2 <= s2) # s2 e subconjunto de s2?










