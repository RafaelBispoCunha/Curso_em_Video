'''
Crie um programa que leia quanto dinheiro tem na carteira e mostre quantos Dólares ela pode comprar.
Considera:
US$ 1.00 = R$ 3.27
Rafael Bispo
11/01/2020
'''
valor = float(input('Digite o valor: '))

dolar = valor / 3.27

print('Posso compar US$ {:.2f}'.format(dolar))