import random

def criar_labirinto(tamanho):
    # Gera uma matriz tamanho x tamanho com 0 (caminho livre) ou 1 (parede) aleatoriamente
    labirinto = [[random.randint(0, 1) for _ in range(tamanho)] for _ in range(tamanho)]

    labirinto[0][0] = 8                          # 8 = posição inicial (entrada)
    labirinto[tamanho - 1][tamanho - 1] = 9      # 9 = posição final (saída)

    return labirinto

def exibir_labirinto(labirinto):
    # Percorre e imprime cada linha da matriz
    for linha in labirinto:
        print(linha)

def nao_pode_seguir(labirinto, linha, coluna):
    # Retorna True se a posição for inválida: fora dos limites, parede (1) ou já visitada (2)
    if (linha >= len(labirinto) or coluna >= len(labirinto) or
        linha < 0 or
        coluna < 0 or
        labirinto[linha][coluna] == 1 or   # parede
        labirinto[linha][coluna] == 2):    # já visitado
        return True
    return False  # posição válida e disponível

def explorar(labirinto, linha, coluna):
    print(f'Explorando ({linha}, {coluna})')

    # Bloqueia caminhos inválidos (fora do labirinto, paredes ou já visitados)
    if nao_pode_seguir(labirinto, linha, coluna):
        print(f'Não pode seguir ({linha}, {coluna})')
        return False

    # Chegou na saída (9)
    if labirinto[linha][coluna] == 9:
        print('Chegou ao final!')
        return True

    # Marca a posição atual como visitada para não revisitar
    labirinto[linha][coluna] = 2

    # Tenta cada direção com recursão; retorna True se qualquer caminho levar à saída
    return (
        explorar(labirinto, linha, coluna + 1) or  # Direita
        explorar(labirinto, linha + 1, coluna) or  # Baixo
        explorar(labirinto, linha, coluna - 1) or  # Esquerda  ← corrigido: era linha - 1
        explorar(labirinto, linha - 1, coluna)     # Cima      ← corrigido: era linha + 2
    )


lab = criar_labirinto(5)
exibir_labirinto(lab)

explorar(lab, 0, 1)
