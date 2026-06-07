# =============================================================================
# HASHES — O QUE SÃO?
#
# Uma função hash transforma qualquer dado (texto, arquivo, senha) num valor
# fixo e único chamado "hash" ou "digest". Características principais:
#
#   1. Determinística  — o mesmo input sempre gera o mesmo hash
#   2. Irreversível    — não é possível recuperar o original a partir do hash
#   3. Efeito avalanche — mudar 1 caractere muda o hash completamente
#   4. Tamanho fixo    — independente do tamanho do input, o hash tem tamanho fixo
#
# Aplicações em segurança:
#   - Senhas: bancos de dados guardam o hash da senha, nunca a senha em si
#   - Integridade: verificar se um arquivo foi alterado (ex: downloads)
#   - Assinaturas digitais: certificar autoria de documentos
#   - Blockchain: cada bloco contém o hash do bloco anterior
#
# Algoritmos comuns: MD5 (obsoleto), SHA-1 (obsoleto), SHA-256 (seguro), SHA-3
# =============================================================================

# =============================================================================
# HASH TABLE (TABELA HASH) — estrutura de dados
#
# O dicionário do Python (dict) é internamente uma hash table:
# quando você faz tabela['A'], Python aplica uma função hash na chave 'A'
# para encontrar instantaneamente onde o valor está na memória — O(1).
# É por isso que buscar em dicionário é muito mais rápido do que em listas.
# =============================================================================

texto = 'As drosófilas, popularmente conhecidas como moscas-das-frutas, são pequenos insetos dípteros pertencentes ao gênero *Drosophila*, com mais de 1.500 espécies descritas. A espécie mais estudada, *Drosophila melanogaster*, tornou-se um dos organismos-modelo mais importantes da biologia, graças ao seu ciclo de vida curto (cerca de duas semanas), facilidade de criação em laboratório e grande prole. Seu tamanho reduzido — em torno de 3 mm — e o fato de se alimentarem principalmente de frutas em fermentação as tornam frequentes em cozinhas e pomares ao redor do mundo.\
\
Do ponto de vista genético, as drosófilas têm importância histórica inestimável. Foi com *D. melanogaster* que Thomas Hunt Morgan, no início do século XX, demonstrou que os genes estão localizados nos cromossomos e estabeleceu os princípios da ligação gênica, trabalho que lhe rendeu o Prêmio Nobel de Fisiologia ou Medicina em 1933. O genoma da espécie, sequenciado em 2000, possui apenas quatro pares de cromossomos e cerca de 13.600 genes, dos quais aproximadamente 75% têm homólogos funcionais em humanos — o que torna esses insetos extraordinariamente úteis para o estudo de doenças humanas.\
\
No campo do desenvolvimento embiológico, as drosófilas revelaram mecanismos fundamentais que regem a formação dos corpos animais. Os genes *Hox*, descobertos inicialmente nessas moscas, controlam a identidade dos segmentos corporais ao longo do eixo ântero-posterior e são conservados em praticamente todos os animais bilateralmente simétricos. Mutações nesses genes produzem fenótipos dramáticos, como o aparecimento de patas no lugar de antenas (*Antennapedia*), ilustrando de maneira direta o papel dos genes no desenvolvimento morfológico.\
\
As drosófilas também são amplamente utilizadas em estudos de neurociência e comportamento. Apesar de seu sistema nervoso simples, com cerca de 100.000 neurônios, esses insetos exibem comportamentos complexos como aprendizado, memória, ritmos circadianos e corte sexual elaborada. Pesquisas com *D. melanogaster* contribuíram diretamente para a compreensão dos mecanismos moleculares do sono e do relógio biológico, área que rendeu o Nobel de Fisiologia ou Medicina de 2017 a Jeffrey Hall, Michael Rosbash e Michael Young.\
\
Do ponto de vista ecológico, as drosófilas desempenham papéis relevantes nos ecossistemas como polinizadoras secundárias e como componentes de cadeias alimentares, servindo de presa para aranhas, pássaros e outros insetos. Algumas espécies invasoras, como *Drosophila suzukii*, representam sérias pragas agrícolas, pois, ao contrário da maioria do gênero, atacam frutos intactos antes da fermentação, causando prejuízos significativos na produção de morangos, uvas e cerejas em diversas partes do mundo. O estudo contínuo dessas moscas segue revelando novos aspectos da biologia fundamental e aplicada.'

# split() quebra o texto em lista de palavras usando espaço como separador
palavras = texto.split()

# dict usado como hash table: chave = letra inicial, valor = lista de palavras
# Python aplica hash() internamente em cada chave para acesso em O(1)
tabela = {}

for palavra in palavras:
    indice = palavra[0].upper()       # pega a primeira letra e padroniza em maiúsculo
    if indice not in tabela:
        tabela[indice] = []           # cria a entrada para essa letra se não existir
    tabela[indice].append(palavra)    # agrupa a palavra sob sua letra inicial

# exibe cada letra e a quantidade de palavras que começam com ela
for chave, valor in tabela.items():
    print(f'{chave}: {len(valor)}')

print(f'Total de palavras: {len(texto.split())}')

# =============================================================================
# DEMONSTRAÇÃO — Hash criptográfico com hashlib (biblioteca nativa do Python)
# =============================================================================
import hashlib

senha = 'minha_senha_123'

# SHA-256: algoritmo seguro, gera 64 caracteres hexadecimais (256 bits)
# encode('utf-8') converte a string para bytes — hashlib exige bytes como input
hash_senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()

print(f'\nSenha original : {senha}')
print(f'Hash SHA-256   : {hash_senha}')

# Efeito avalanche: mudar 1 caractere gera um hash completamente diferente
senha_alterada = 'minha_senha_124'
hash_alterado = hashlib.sha256(senha_alterada.encode('utf-8')).hexdigest()
print(f'\nSenha alterada : {senha_alterada}')
print(f'Hash alterado  : {hash_alterado}')

# Na prática, bancos de dados nunca guardam a senha — guardam o hash.
# No login, o sistema gera o hash do que o usuário digitou e compara com o hash salvo.
print(f'\nSenhas batem? {hash_senha == hash_alterado}')  # False — hashes diferentes
