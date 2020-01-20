'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

Rafael Bispo
14/01/2020
'''
numero1 = int(input('Digite o 1° número: '))
numero2 = int(input('Digite o 2° número: '))
numero3 = int(input('Digite o 3° número: '))

if numero1 >= numero2:
    if numero1 >= numero3:
        if numero2 >= numero3:
            menor = numero3
        else:
            menor = numero2
        maior = numero1
    else:
        maior = numero3
        menor = numero2

else:
    if numero2 >= numero3:
        if numero1 >= numero3:
            menor = numero3
        else:
            menor = numero1
        maior = numero2
    else:
        maior = numero3
        menor = numero1

print('O menor número é {}\nO maior número é {}'.format(menor, maior))
