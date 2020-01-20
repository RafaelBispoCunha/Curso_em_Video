'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
lendo o nome deles e escrevendo o nome do escolhido.

Rafael Bispo
13/01/2020
'''
import random
primeiro_aluno = input('Digite o nome do 1° Aluno: ')
segundo_aluno  = input('Digite o nome do 2° Aluno: ')
terceiro_aluno = input('Digite o nome do 3° Aluno: ')
quarto_aluno   = input('Digite o nome do 4° Aluno: ')

lista_alunos = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
sorteado = random.choice(lista_alunos)
print('O aluno Sorteado foi {}'.format(sorteado))