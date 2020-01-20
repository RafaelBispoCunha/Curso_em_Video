'''
Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salário, com 15% de aumento.
Rafael Bispo
11/01/2020
'''
salario = float(input('Digite o salário do funcionário: '))

novoSalario = salario + (salario * 0.15)

print('O salário é de R$ {:.2f} com o aumento fica R$ {:.2f}'.format(salario, novoSalario))