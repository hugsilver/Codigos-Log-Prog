

frase = ' O curso de Lógica de programação é supimpa! '

'''
Exemplos de métodos úteis para strings:

print(type(frase))                          # Mostra o tipo: <class 'str'>

print(f'Primeira letra: {frase[0]}')        # Acessa pelo índice 0 (primeiro caractere)
print(f'Última letra: {frase[-1]}')         # Índice -1 = último caractere
print(f'Tamanho da frase: {len(frase)} caracteres')  # len() conta todos os caracteres

print(f'Maiúsculas: {frase.upper()}')       # Converte tudo para MAIÚSCULO
print(f'Minúscula: {frase.lower()}')        # Converte tudo para minúsculo

print(f'Fatiando: {frase.split()}')         # split() sem argumento separa por espaço
print(f'Fatiando: {frase.split("a")}')      # split("a") separa onde encontrar a letra "a"
print(f'Frase original: {frase}')           # string original não é alterada pelos métodos

print(f'Tamanho da string limpa: {len(frase.strip())}')  # strip() remove espaços do início e fim
'''


def analisadorDeTexto(texto):
    palavras = texto.split()                                        # divide o texto numa lista de palavras separadas por espaço
    num_palavras = len(palavras)                                    # conta o total de palavras
    num_caracteres = len(texto)                                     # conta todos os caracteres, incluindo espaços
    num_caracteres_sem_espacos = num_caracteres - texto.count(' ')  # subtrai a quantidade de espaços

    # Python permite retornar múltiplos valores de uma vez (retorna uma tupla)
    return num_palavras, num_caracteres, num_caracteres_sem_espacos


# Desempacotamento: cada variável recebe um valor do retorno da função
num_p, num_c, num_cse = analisadorDeTexto(frase)

print(f'Numero de palavras: {num_p}')
print(f'Numero de caracteres: {num_c}')
print(f'Numero de caracteres sem espaço: {num_cse}')

'''
return num_palavras, num_caracteres, num_caracteres_sem_espacos — Python permite retornar múltiplos valores ao mesmo tempo; internamente isso cria uma tupla
num_p, num_c, num_cse = analisadorDeTexto(frase) — isso se chama desempacotamento: cada variável da esquerda recebe um valor correspondente do retorno da função, na ordem
'''
