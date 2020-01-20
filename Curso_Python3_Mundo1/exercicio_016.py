'''
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira.
13/01/2020
'''
from math import trunc

numero = float(input('Digite um valor qualquer: '))
print('A porção inteira do numero {} é de {}'.format(numero, trunc(numero)))
