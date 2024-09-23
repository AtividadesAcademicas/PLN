import numpy as np

alunos = int(input("Digite a quantidade de alunos avaliados: "))
qtd_avaliacoes = int(input("Digite a quantidade de avaliações: "))
pesos = []
soma_pesos = 0

matriz = np.zeros((alunos, qtd_avaliacoes), dtype=np.int32)

for x in range(qtd_avaliacoes):
    aux = False
    while(aux != True):
        peso = int(input("Digite o peso da {}° avaliação: ".format(x+1)))
        if(soma_pesos + peso > 10):
            print("A soma de todos os pesos deve ser igual a 10.")
        else:
            soma_pesos =+ peso
            pesos.append(peso)
            aux = True

del soma_pesos

for x in range(alunos):
    nota = 0
    for y in range(qtd_avaliacoes):
        nota = input("Digite a {}° nota do {}° aluno: ".format(y+1, x+1))
        matriz[x,y] = nota

def nota_final(matriz_notas, vetor_pesos):
    notas_finais = []
    for x in range(alunos):
        final = []
        for y in range(qtd_avaliacoes):
            final.append(matriz[x,y]*pesos[y])
        nota = np.sum(final) / 10
        notas_finais.append(nota)
    return np.array(notas_finais)

notas_finais = nota_final(matriz, pesos)

print('\nResultado:')

for x in range(len(notas_finais)):
    print("Média final do {}° aluno: ".format(x+1), notas_finais[x])