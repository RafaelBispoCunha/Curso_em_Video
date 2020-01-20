'''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
Rafael Bispo
11/01/2020
'''
preco = float(input('Digite o preço do produto: '))
novoPreco = preco - (preco * 0.05)

print('O preço é {} e com desconto fica {} :'.format(preco, novoPreco))