'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km Rodado.
13/01/2020
'''
km = float(input('Digite quantos Kms percorridos: '))
dias = int(input('Digite quantos dias  carro esta alugado: '))
preco = (dias * 60) + (km * 0.15)
print('O carro andou durante {} dias, {} Kms, o preço total é R$ {:.2f}'.format(dias, km, preco))