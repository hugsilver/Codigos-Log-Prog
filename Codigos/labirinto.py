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
    if (linha >= len(labirinto) or coluna >= len(labirinto) or labirinto[linha][coluna] == 1):
        return True

def explorar(labirinto, linha, coluna):
    print(f'Explorando ({linha}, {coluna})')
    if nao_pode_seguir(labirinto,  linha, coluna):
        print(f'Não pode seguir {linha}, {coluna})')
        return False
    if labirinto[linha][coluna] == 9:
        print('Chegou ao final!')
        return True
    
    return (
        explorar(labirinto, linha, coluna + 1)  or #Direita
        explorar(labirinto, linha + 1, coluna) or #Baixo
        explorar(labirinto, linha - 1, coluna) or #Esquerda
        explorar(labirinto, linha+ 2, coluna) #Cima
        

    )



lab = criar_labirinto(5)
exibir_labirinto(lab)

explorar(lab, 0, 1)
