'''
Faça um programa que leia um comprimento do cateto oposto e do cateto adjacente de um triângulo retangulo,
calcule e mostre o comprimento da hipotenusa.
13/01/2020
'''
from math import hypot
cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto oposto: '))
print('O comprimento da Hipotenusa é: {:.2f}'.format(hypot(cateto_oposto, cateto_adjacente)))