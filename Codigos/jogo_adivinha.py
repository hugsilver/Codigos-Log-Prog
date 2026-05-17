perguntas = [['Seu animal gosta de bananas','macaco']]

while True:
    print('Pense em um animal...')

    acertou = False

    for pergunta in perguntas:
        resp = input(f'{pergunta[0]} (s/n): ').upper()
        if resp == 'S':
            print(f'Você pensou em {pergunta[1]}!')
            acertou = True
            break

    if not acertou: #acertou == False
        animal = input('Desisto! Em qual animal você pensou? ')
        novapergunta = input('Qual pergunta você faria para diferenciar esse animal? ')
        perguntas.append([novapergunta, animal])

    resposta = input('Quer jogar novamente (s/n): ')
    if resposta.lower() != 's':
        print('OK! Foi bom jogar com você.')
        break
