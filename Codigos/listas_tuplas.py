# Lista: mutável, usa colchetes — pode adicionar, remover e alterar itens
lista = [1, 2, 3, 4]

# Tupla: imutável, usa parênteses — os valores nunca mudam após a criação
tupla = (1, 2, 3, 4)

# Lista global que armazena as tarefas como tuplas (nome, status)
tarefas = []

import os

def adicionaTarefa(tarefa):
    # Empacota o nome e o status inicial numa tupla e insere na lista global
    novaTarefa = (tarefa, 'Pendente')
    tarefas.append(novaTarefa)

def exibeTarefas():
    if not tarefas:
        print('A lista está vazia')
        return
    # tarefa[0] = nome da tarefa | tarefa[1] = status atual
    for tarefa in tarefas:
        print(f'{tarefa[0]} - Status: {tarefa[1]}')

def concluirTarefa(tarefa):
    global tarefas  # necessário para reatribuir a variável global

    # List comprehension: percorre todas as tarefas e substitui o status
    # da tarefa que bate com o nome recebido; as demais ficam intactas (else t)
    tarefas = [(t[0], 'concluída') if t[0] == tarefa else t for t in tarefas]

    # Equivalente sem list comprehension (versão mais longa):
    '''
    novaLista = []
    for t in tarefas:
        novaLista.append(t if t[0] != tarefa else (tarefa, 'Concluída'))
    tarefas = novaLista
    '''

def removerTarefa(tarefa):
    global tarefas
    tarefas = [t for t in tarefas if t[0] != tarefa] #Devolver uma lista filtrada

def buscarTarefa(tarefa):
    resultado = [t for t in tarefas if t[0].lower() == tarefa.lower()]
    if resultado: #Se resultado é uma lista não vazia
        for titulo, status in resultado:
            print(f'Encontrada: {titulo} - Status: {status}')
    else:
        print(f'Tarefa não encontrada: {tarefa}')

while True:
    #Chamada de sistema
    os.system('cls')
    
    print('Boas vindas oa gerenciados de lista de tarefas')
    print()
    print('O que você quer fazer agora? ')
    print('1 - Listar tarefas')
    print('2 - Adicionar tarefa')
    print('3 - Remover tarefa')
    print('4 - Marcar tarefa como conluída')
    print('5 - Buscar tarefa')
    print('0 - Sair')
    opcao = int(input('Digite uma opção: '))

    match opcao:
        case 1:
            exibeTarefas()
        case 2:
            tarefa = input('Digite a tarefa: ')
            adicionaTarefa(tarefa)
        case 3:
            tarefa = input('Digite a tarefa: ')
            removerTarefa(tarefa)
        case 4:
            tarefa = input('Digite a tarefa: ')
            concluirTarefa(tarefa)
        case 5:
            tarefa = input('Digite a tarefa: ')
            buscarTarefa(tarefa)
        case 0:
            break
        case _: #Case qualquer outra coisa
            print('opção invalida')
    print()
    input('Pressione ENTER para continuar...')
    




'''
def buscarTarefa(tarefa):
    for t in tarefas:
        if t[0] == tarefa:
            print(f'Tarefa encontrada: {t[0]} - Status: {t[1]}')
            return #"Matar" a função
    print(f'Não achei: {tarefa}')
'''

'''
adicionaTarefa('Arrumar a cama')
adicionaTarefa('Lavar a louça')
exibeTarefas()

buscarTarefa('Arrumar a cama')
buscarTarefa('Ir ao mercado')
'''

'''
print('Agora vou concluir')
concluirTarefa('Arrumar a cama')
exibeTarefas()
print('Agora removendo')
#concluirTarefa('ir ao mercado')
removerTarefa('Arrumar a cama')
exibeTarefas()
'''


# List Comprehension — forma compacta de criar listas com filtro e transformação
# Sintaxe: [expressão  for item in lista  if condição]
'''
lista = [1, 5, 9]
novaLista = [n * 2 for n in lista if n > 7]  # filtra n > 7, depois dobra: 9 * 2 = 18
print(novaLista)  #[18]
'''
