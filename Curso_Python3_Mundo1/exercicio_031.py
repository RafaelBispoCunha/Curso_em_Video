'''
Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule  o preço da passagem, cobrando R$ 0,50
por Km para viagens até 200 Km e R$ 0,45 para viagens mais longas.

Rafael Bispo
14/01/2020
'''
km = float(input('Digite Quantos Kms têm a viagem: '))

if km <= 200:
    print('O preço por {:.0f} Km é de R$ {:.2f}'.format(km, km * 0.50))
    valor = 0.50
else:
    print('O preço por {:.0f} Km é de R$ {:.2f}'.format(km, km * 0.45))
    valor = 0.45
print('OBS: R$ {:.2f} por Km'.format(valor))