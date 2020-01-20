'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
Rafael Bispo
14/01/2020
'''
salario = float(input('Digite o valor do Salário: '))
if salario <= 1250:
    aumento = 15
    novoSalario = salario + (salario * aumento / 100)
else:
    aumento = 10
    novoSalario = salario + (salario * aumento / 100)
print('O salário de R$ {:.2f} teve um aumento de {}% e agora totaliza R$ {:.2f}'.format(salario, aumento, novoSalario))
