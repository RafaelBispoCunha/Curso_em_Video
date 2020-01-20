'''
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

Rafael Bispo
14/01/2020
'''
numero = int(input('Digite um númeo e descubra se ele é par ou ímpar: '))

if numero % 2 == 0:
    print('O número {} é Par'.format(numero))
else:
    print('O número {} é Ímpar'.format(numero))
print('\nFIM')