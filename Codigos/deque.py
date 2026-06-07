
# Deque (Double-Ended Queue) — fila de duas pontas
# Permite inserir e remover tanto do início quanto do final com eficiência
# Diferente de list.pop(0) que é lento, deque.popleft() é O(1)

from collections import deque  # importa deque da biblioteca padrão 'collections'


def criaFila():
    return deque()  # retorna um deque vazio pronto para uso


def insereNaFila(fila, elemento):   # 'fila' minúsculo para bater com o parâmetro
    fila.append(elemento)           # insere no final da fila


def removeDaFila(fila):             # 'fila' minúsculo para bater com o parâmetro
    return fila.popleft()           # remove e retorna o primeiro elemento (FIFO)


fila = criaFila()
print(fila)                         # deque([])

insereNaFila(fila, 8)
insereNaFila(fila, 9)
insereNaFila(fila, 10)
insereNaFila(fila, 11)
insereNaFila(fila, 12)              # fila agora: deque([8, 9, 10, 11, 12])

print(f'Removendo: {removeDaFila(fila)}')  # remove 8 (primeiro a entrar)
print(f'Removendo: {removeDaFila(fila)}')  # remove 9
print(fila)                                # deque([10, 11, 12])
