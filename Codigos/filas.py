#fila - Insere no final
#Remover - Aquele que estiver na vez
#Inserir da em lado e retirar do outro - FIFO - First in forst out
#fila - dados inseridos em sequência - nção pode tirar do meio - LIFO - Left In forst Out


lista = [1, 2, 3, 4, 5, 6, 7, 8]
lista.append(4) # - Método append Adiciona no final da lista
lista.pop() #Retira o ultimo elemento do final da fila

lista = [1, 2, 3, 4, 5, 6, 7, 8]
lista.pop(0) # Implementar tirar do começo

#Criar estrutura de dados
from collections import deque

#filas
def criafila():
    return deque()

def enfileirar(fila, elemento):   # renomeado: 'fila' era igual à variável abaixo
    fila.append(elemento)          # insere no final

def removeDafila(fila):
    return fila.pop()             # pop(0) remove do início — correto para FIFO

fila = criafila()
print(fila)
enfileirar(fila, 8)
enfileirar(fila, 9)
enfileirar(fila, 10)
enfileirar(fila, 11)
enfileirar(fila, 12)
print(f'Removendo: {removeDafila(fila)}')
print(f'Removendo: {removeDafila(fila)}')
print(fila)








