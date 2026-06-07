#Tabelas Hashes
#Hashes Tags - # Filtrar elementos que tem mesmo assunto - Pegar conjunto de dados, aplicr uma função e aextrair dados de acordo com 
#essa hashes


nomes = [
    'João',
    'Antonio',
    'Maria',
    'Emengarda',
    'Ana',
    'Anacleto',
    'Bianca',
    'José',
    'Adão',
    'Josi'

]
#Chato percorrer uma lista - Melhor organizar

tabela = {}

for nome in nomes:
    #qtd = len(nome) #Pega o número de caracteres que tem em cada nome
    qtd = nome[0]
    if qtd not in tabela:
        tabela[qtd] = []
    tabela[qtd].append(nome)

print(tabela)
#Função de hashes de espalhamento - Muito usado quando se tem muitos dados

#procura('João')



