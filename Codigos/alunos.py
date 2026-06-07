estudantes = {
    1 : {'nome': 'Joana', 'idade': 45, 'curso': 'Computação'},
    2 : {'nome': 'Ivan', 'idade': 70, 'curso': 'Matemática'},
    3 : {'nome': 'Jaqueline', 'idade': 12, 'curso': 'Computação'}
}

cursos = {'Computação', 'Matemática', 'Física'}
estudantes_cursos = {
    'Computação': {1, 3},
    'Matemática': { 2 }
}

def adicionarEstudante(matricula, nome, idade, curso):
    pessoa = {'nome': nome, 'idade': idade, 'curso': curso }
    estudantes[matricula] = pessoa
    if curso not in estudantes_cursos:# Se curso não está na lista
        estudantes_cursos[curso] = set() #Adiciona um conjunto vázio
    estudantes_cursos[curso].add(matricula)

#print(estudantes_cursos)
#adicionarEstudante(5, 'João', 89, 'Computação')
#print(estudantes_cursos)
#adicionarEstudante(6, 'maria', 55, 'Física')
#print(estudantes_cursos)

#print(f'Todas a pessoas matriculas em algum curso: {estudantes_cursos['Matemática'] | estudantes_cursos['Computação']}')
print(f'Todas a pessoas matriculas em algum curso: {estudantes_cursos['Matemática'] - estudantes_cursos['Computação']}')