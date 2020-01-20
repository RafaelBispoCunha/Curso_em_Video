'''
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

Rafael Bispo
14/01/2020
'''
reta1 = int(input('Digite a 1° Reta: '))
reta2 = int(input('Digite a 2° Reta: '))
reta3 = int(input('Digite a 3° Reta: '))

if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta3 + reta1 > reta2 :
    print('As 3 retas podem Formar um trinângulo')
else:
    print('As 3 retas não podem Formar um trinângulo')