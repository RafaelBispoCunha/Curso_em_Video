'''
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 Km/h. mostre uma mensagem dizendo que ele
foi multado. A multa vai custar R$ 7,00 por cada Km acima do limite.

Rafael Bispo
14/01/2020
'''
velocidade = float(input('Informa a velocidade do carro: '))

if velocidade > 80:
    kmAcima = velocidade - 80
    print('Você foi multado por esta á {} Km/h o valor da multa é de R$ {:.2f}.'.format(velocidade, kmAcima * 7))

print('Digija sempre com conciência')

print('\nFIM')
