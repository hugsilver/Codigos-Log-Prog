

tabuleiro = [
    ['',  '', ''],
    ['',  '', ''],
    ['',  '', ''],

]
#print(tabuleiro)

jogador = 'X'

def exibeTab():
    for linha in tabuleiro:
        print(' | '.join(linha)) # Join é um método - Junta coisas de uma lista com o separador escolhido
        #print(f'{linha[0]} | {linha[1]} | {linha[2]}')
        print('-'*10)

def jogada(linha, coluna):
    #Acessar váriavel global
    #global jogador # Não recomendavel - Ficar dentro de uma função alterando valor de uma váriavel global
    #Melhor fazer um return
    tabuleiro[linha][coluna] = jogador
    if jogador == 'X':
        return 'O'
    else:
        return 'X' 

jogador = jogada(1, 1)
jogador = jogada(1, 1)
jogador = jogada(1, 5)
exibeTab()

#Outro método
'''
tabuleiro2 = [ [' ' for _ in range(0, 3)] for _ in range(0, 3)] # undeline (_) - Usar e descartar
print(tabuleiro2)
'''