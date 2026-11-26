from math import hypot

co = int(input("Digite o comprimento do cateto oposto: "))
ca = int(input("Digite o comprimento do cateto adjacente: "))
h  = hypot(co, ca) #a função hypot() calcula a hipotenusa de um triângulo retângulo a partir dos comprimentos dos catetos oposto e adjacente.
print(f"A hipotenusa vai medir {h:.2f}")