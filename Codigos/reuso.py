def olaMundo():
    print('Olá, Mundo')

def olaPessoa(nome):
    print(f'Olá, {nome}!')

def dobro(num):
    return num*2

def mut(a=2, b=2):#Ou apenas do segundo ou em todos
    '''
    Docstring para mut - Multiplica dois números
    
    :param a: Descrição
    :param b: Descrição
    '''
    return(a*b)

olaMundo()
olaPessoa('Hugo')
print(dobro(5)+2)
print(mut(3, 6))
print(mut(3))

x=5 #Váriavel global
def soma():
    x = 10 #Váriavel local
    print(x)
    return x + 1

soma()
print(x)
