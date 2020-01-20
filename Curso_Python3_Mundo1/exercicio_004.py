'''
Faça um programa que leia algo no teclado e mostre na tela seu tipo primitivo
e todas informações possiveis sobre ele.
Rafael Bispo
11/01/2020
'''
tipo = input('Digite alguma coisa: ')
print('O tipo primitivo da variavel é: ', type(tipo))
print('O tipo é um número: ?   ', tipo.isnumeric())
print('O tipo é Alfabetico:?   ', tipo.isalpha())
print('O tipo é Alfanúmerico:? ', tipo.isalnum())
