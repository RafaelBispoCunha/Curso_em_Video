'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

13/01/2020
'''
from math import  sin, cos, tan ,radians
angulo = float(input('Digite o angulo: '))
print('\nO angulo de {:.2f} tem:'.format(angulo))
radiano = radians(angulo)

print('O seno de {:.2f}.'.format(sin(radiano)))
print('O cosseno de {:.2f}'.format(cos(radiano)))
print('A tangente de {:.2f}.'.format(tan(radiano)))

