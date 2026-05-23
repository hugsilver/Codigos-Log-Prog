tabuleiro = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]

jogador = 'X'


def temGanhador():
    # Verificar linhas
    for linha in range(3):
        if (tabuleiro[linha][0] != ' ' and
                tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2]):
            return tabuleiro[linha][0]

    # Verificar colunas
    for coluna in range(3):
        if (tabuleiro[0][coluna] != ' ' and
                tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna]):
            return tabuleiro[0][coluna]

    # Verificar diagonais
    if (tabuleiro[1][1] != ' ' and (
        tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] or
        tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]
    )):
        return tabuleiro[1][1]

    return None


def temEmpate():
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == ' ':
                return False
    return True


def exibeTab():
    print()
    print('       0   1   2')
    print('     +---+---+---+')
    for i, linha in enumerate(tabuleiro):
        print(f'  {i}  | {" | ".join(linha)} |')
        print('     +---+---+---+')
    print()


def jogada(linha, coluna):
    if (not 0 <= linha <= 2 or
            not 0 <= coluna <= 2 or
            tabuleiro[linha][coluna] != ' '):
        return None
    tabuleiro[linha][coluna] = jogador
    return 'O' if jogador == 'X' else 'X'


print()
print('  =========================')
print('      J O G O  D A  V E L H A')
print('  =========================')
print('  Linha e coluna: valores de 0 a 2')
exibeTab()

while True:
    print(f'  Jogador da vez: [ {jogador} ]')
    try:
        linha = int(input('    Linha  (0-2): '))
        coluna = int(input('    Coluna (0-2): '))
    except ValueError:
        print('  Entrada invalida! Digite apenas numeros.\n')
        continue

    proximo = jogada(linha, coluna)
    if proximo is None:
        print('  Jogada invalida! Posicao fora do limite ou ja ocupada.\n')
        continue

    jogador = proximo
    exibeTab()

    ganhador = temGanhador()
    if ganhador:
        print(f'  Parabens! Jogador [ {ganhador} ] GANHOU!')
        print()
        break

    if temEmpate():
        print('  EMPATE! Foi um bom jogo!')
        print()
        break
