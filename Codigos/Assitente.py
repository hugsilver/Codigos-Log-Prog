#Match case


print('Olá, Eu sou sua assistente, Pythrina. O que você     quer fazer hoje?')

comando = input('Digite um comando: ')

match comando:

    case 'oi' | 'Ola': # | Serve para colocar mais de um argumento - Pipe ou Barra 
        print('Olá, como vai você?')
    case 'tchau':
        print('Tchau, foi bom conversar com você.')
    case 'paida':
        print('Sabe qual é o padroeiro das pessoas que trabalham com TI? O São Login')
    case 'clima':
        print('Tá muito quente!! Deve ter passado dos 40°')
    case _ :#Sem aspas mesmo
        print('Não entendi o comando o comando.')


