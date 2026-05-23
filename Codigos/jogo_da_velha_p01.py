

tabuleiro = [
    [' ',  ' ', ' '],
    [' ',  ' ', ' '],
    [' ',  ' ', ' '],

]
#print(tabuleiro)

jogador = 'X'

def exibeTab():
    for linha in tabuleiro:
        print(' | '.join(linha)) # Join é um método - Junta coisas de uma lista com o separador escolhido
        #print(f'{linha[0]} | {linha[1]} | {linha[2]}')
        print('-'*10)

def jogada(linha, coluna):
    if (not 0 <= linha <= 2 or 
        not 0 <= coluna <= 2 or
        #Se linha ou coluna não fazem parte desse Range 
        tabuleiro[linha][coluna] != ' ' #Se não estiver vazio
    ):
        print('Jogada Invalida')
        return jogador #Retorna o jogador atual
    #Acessar váriavel global
    #global jogador # Não recomendavel - Ficar dentro de uma função alterando valor de uma váriavel global
    #Melhor fazer um return
    tabuleiro[linha][coluna] = jogador
    '''
    if jogador == 'X':
        return 'O'
    else:
        return 'X'
    '''
    return 'O' if jogador == 'X' else 'X' #Retorna O se jogador já for X, se ele for O return X ] - Retorna outro jogador

'''
jogador = jogada(1, 1)
jogador = jogada(1, 2)
jogador = jogada(1, 2)
'''

while True:
    print(f'Jogador da vez: {jogador}')
    try: 
        linha = int(input('Digite a linha: '))
        coluna = int(input('Digite a coluna: '))
        jogador = jogada(linha, coluna)
    except (ValueError, IndexError): #Podendo tratar os erros de forma separada - Para mostar mensagens mais coerentes para cada exesão  
        print('Digite valores numéricos entre 0 e 2') #Não quebra e trata o erro 



    exibeTab()
exibeTab()

#Outro método
'''
tabuleiro2 = [ [' ' for _ in range(0, 3)] for _ in range(0, 3)] # undeline (_) - Usar e descartar
print(tabuleiro2)
'''

#if ternario
#Tratamento de exceções 