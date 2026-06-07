# Heap — estrutura de dados nativa do Python para fila de prioridades
# Sempre mantém o menor valor no topo (min-heap)
# Útil quando você precisa processar itens em ordem de prioridade (1 = mais urgente)

from heapq import *  # importa heappush e heappop sem precisar usar o prefixo heapq.


fila_prioridade = []  # lista comum que o heapq transforma internamente numa heap

# heappush(heap, item) — insere o item mantendo a ordem de prioridade
# cada item é uma tupla (prioridade, tarefa): menor número = maior urgência
heappush(fila_prioridade, (2, 'Atender cliente VIP'))
heappush(fila_prioridade, (1, 'Situação crítica'))
heappush(fila_prioridade, (3, 'Responder e-mails'))
heappush(fila_prioridade, (1, 'Apagar incêndio'))  # prioridade 1 empata com 'Situação crítica'

# heappop(heap) — remove e retorna sempre o item de menor prioridade
# o loop processa todas as tarefas do mais urgente para o menos urgente
while fila_prioridade:
    prioridade, tarefa = heappop(fila_prioridade)  # desempacota a tupla retornada
    print(f'Executando: {tarefa} - Prioridade: {prioridade}')
