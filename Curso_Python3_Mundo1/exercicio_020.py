'''
O mesmo professor do desafio anterioe quer sortear a ordem de apresentação de trabalho dos alunos.
Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.
Rafael Bispo
13/01/2020
'''
import random
primeiro_aluno = input('Digite o nome do 1° Aluno: ')
segundo_aluno  = input('Digite o nome do 2° Aluno: ')
terceiro_aluno = input('Digite o nome do 3° Aluno: ')
quarto_aluno   = input('Digite o nome do 4° Aluno: ')

lista_alunos = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
print('A ordem para apresentação é:')
random.shuffle(lista_alunos)
print(lista_alunos)
