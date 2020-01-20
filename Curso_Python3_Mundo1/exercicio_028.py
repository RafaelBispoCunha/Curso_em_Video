'''
Escreva um programa de que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

Rafael Bispo
14/01/2020
'''
from random import randint
numeroAleatorio = randint(0, 5)
numero = int(input('O computador gerou um número entre 0 e 5: \nAdivinhe que número foi: '))

if numero == numeroAleatorio:
    print('Parabéns Você acertou o número {}' .format(numeroAleatorio))
else:
    print('Infelizmente Você acertou o número \nO número certo é: {}'.format(numeroAleatorio))
print('\nFIM')