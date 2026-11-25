#faça um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input("Digite o salário do funcionário: R$ "))
aumento = salario * 15/100
novo_salario = salario + aumento
print(f"O salário do funcionário é R$ {salario:.2f} com 15% de aumento é R$ {novo_salario:.2f}")