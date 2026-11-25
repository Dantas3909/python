#crie um programa que leia quanto dinehrio uam pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$ 1,00 = R$ 3,27
carteira = float(input("Digite quanto dinheiro você tem na carteira: R$ "))
dolares =  carteira / 3.27
print(f"você pode comprar US$ {dolares:.2f} com R$ {carteira:.2f}")

# O .2f formata o número para exibir 2 casas decimais (ideal para valores em dinheiro, como centavos).

# : inicia a formatação dentro da f-string.

# .2 define 2 dígitos após o ponto decimal.

# f indica um número de ponto flutuante (float).