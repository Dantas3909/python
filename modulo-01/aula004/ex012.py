#faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input("Digite o preço do produto: R$ "))
descconto = produto * 5/100
valor = produto - descconto
print(f"o valor do produto é R$ {produto:.2f} com 5% de desconto é R$ {valor:.2f}")