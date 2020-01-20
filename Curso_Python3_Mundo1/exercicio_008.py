'''
Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros.
Rafael Bispo
11/01/2020
'''
metros = float(input('Digite os metros: '))
centimetros = metros / 0.01
print('{} metros convertido para centimetro é: {} '.format(metros, centimetros))
milimetros = metros / 0.001
print('{} metros convertido para milimetros é: {} '.format(metros, milimetros))