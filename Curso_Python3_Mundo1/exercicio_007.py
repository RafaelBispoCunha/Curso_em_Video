'''
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
Rafael Bispo
11/01/2020
'''
nota_01 = float(input('Digite a 1° nota do aluno: '))
nota_02 = float(input('Digite a 2° nota do aluno: '))

media = (nota_01 + nota_02) / 2
print('A média do aluno é: {}'.format(media))