# Lista encadeada
# Cada nó tem duas partes: valor e ponteiro para o próximo nó
# Para inserir: novo nó aponta para o próximo ANTES de ser ligado à lista
# Para remover: o nó anterior passa a apontar para o nó seguinte ao removido

lista = {
    'valor': 5,
    'proximo': None
}

print(lista)


'''
novo = {'valor': 8, 'proximo': None}
lista['proximo'] = novo
print(lista)
'''

def exibeLista(lista):
    if not lista:
        print('Lista vazia.')
        return
    elemento = lista                              # começa pelo primeiro nó
    while elemento is not None:                   # percorre até o fim (None)
        print(f" {elemento['valor']}", end=' ')   # exibe o valor sem quebrar linha
        elemento = elemento['proximo']            # avança para o próximo nó
    print('.')


def adicionaNoFim(elemento):
    global lista
    novo_no = {'valor': elemento, 'proximo': None}

    if not lista:                                 # lista vazia: novo nó vira o primeiro
        lista = novo_no
        return

    atual = lista
    while atual['proximo'] is not None:           # percorre até o último nó
        atual = atual['proximo']
    atual['proximo'] = novo_no                    # liga o último ao novo nó


#exibeLista(lista)
#lista = adicionaNoFim(lista, 15)
exibeLista(lista)
print('Adicionando o 5...')
adicionaNoFim(5)
exibeLista(lista)
print('Adicionando o 8...')
adicionaNoFim(8)
exibeLista(lista)
print('Adicionando o 13...')
adicionaNoFim(13)
exibeLista(lista)
