'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
1 - O nome com todas as letras maiúscula;
2 - O nome com todas minúsculas;
3 - Quantas letras ao todo(sem considerar espaços);
4 - Quantas letras tem o primeiro nome.

Rafael Bispo
14/01/2020
'''
nome = input('Digite seu nome: ').strip()
print('O nome com todas as letras maiúscula {}' .format(nome.upper()))
print('O nome com todas minúsculas {}' .format(nome.lower()))
print('letras ao todo sem considerar espaços {}'.format(len(nome) - nome.count(' ')))
print('Quantidade de letras que tem o primeiro nome {}'.format(nome.find(' ')))