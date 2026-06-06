# Lista: mutável, usa colchetes — pode adicionar, remover e alterar itens
lista = [1, 2, 3, 4]

# Tupla: imutável, usa parênteses — não pode ser alterada após criada
tupla = (1, 2, 3, 4)

# Lista de tarefas começa vazia; será preenchida pelas funções abaixo
tarefas = []


def adicionaTarefa(tarefa):
    # Cria uma tupla (nome, status) e adiciona na lista de tarefas
    novaTarefa = (tarefa, 'Pendente')
    tarefas.append(novaTarefa)


def exibeTarefas():
    # Percorre cada tarefa e exibe o nome e o status atual
    for tarefa in tarefas:
        print(f'{tarefa[0]} - Status: {tarefa[1]}')


def concluirTarefa(tarefa):
    global tarefas  # acessa a variável global para poder substituí-la
    tarefa = [(t[0], 'concluída') if t[0] == tarefa else t for t in tarefas] #Entender mais

    '''
     novaLista = []
    for t in tarefas:
        # Se o nome bate com a tarefa buscada, substitui o status; senão mantém igual
        novaLista.append(t if t[0] != tarefa else (tarefa, 'Concluída'))
    tarefas = novaLista  # substitui a lista antiga pela nova com o status atualizado
    '''


adicionaTarefa('Arrumar a cama')
adicionaTarefa('Lavr a louça')
exibeTarefas()

print('Agora vou concluir')
concluirTarefa('Arrumar a cama')
exibeTarefas()


# List Comprehension — cria uma lista nova de forma compacta - NÃO CONHECIA - ABRE MUITAS POSSIBILIDADE - VER MAIS OBRE - ESTUDAR
# Sintaxe: [expressão  for item in lista  if condição]
lista = [1, 5, 9]
novaLista = [n * 2 for n in lista if n > 7]  # pega só os n > 7 e dobra o valor - Método permite que faça filtros muito rápido
print(novaLista)  # resultado: [18]  (só o 9 passa pelo filtro: 9 * 2 = 18)


