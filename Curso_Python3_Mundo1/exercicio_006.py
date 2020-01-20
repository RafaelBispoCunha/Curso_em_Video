'''
Faça um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
Rafael Bispo
11/01/2020
'''
numero = int(input('Digite um número: '))
print('O dobro é: {} \nSeu triplo é: {} \nSua raiz quadrada é: {:.2f}'.format(numero * 2, numero * 3, numero ** (1/2)))
