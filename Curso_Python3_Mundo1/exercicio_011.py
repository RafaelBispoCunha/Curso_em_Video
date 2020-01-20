'''
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
Rafael Bispo
11/01/2020
'''
base = float(input('Digite a base: '))
altura = float(input('Digite a altura: '))
area = base * altura
print('Area {} m²'.format(area))
lata = area / 2

print('Você precisa de  {} L de tinta para pintar a parede'.format(lata))