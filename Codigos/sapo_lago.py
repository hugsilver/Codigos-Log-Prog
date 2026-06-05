# N=1 -> [ 1 ] = 1
# N=2 -> [1, 1], [2] = 2
# N=3 -> [1, 1, 1], [1, 2], [2, 1] = 3
# N=4 -> [1, 1, 1, 1], [2, 1, 1], [1, 2, 1], [1, 1, 2], [2, 2] = 5
# N=5 -> [1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 2, 1], [1, 2, 1, 1], [2, 1, 1, 1], [ 1, 2, 2], [2, 1, 2], [ 2, 2, 1] = 8
# Padrão -> Sequência Fibonaci

def contar_caminhos(num_pedras):
    if num_pedras <= 1:
        return 1
    return contar_caminhos(num_pedras - 1) + contar_caminhos(num_pedras - 2)
    
print(contar_caminhos(57))
#Nem sempre a recursividade é boa, pois pode gera processamento desperdisçado.
#Podendo usar uma forma iterativa/Loop
