'''
Escreva um programa que converta uma temperatura digitada em °C e converta para °F
Rafael Bispo
13/01/2020
'''
cel = float(input('Digite a Temperatura em °C: '))
fah = 32 + (cel * 9) / 5
print('A temperatura em Celsius é de {} em Fahrenheit é {}'.format(cel, fah))