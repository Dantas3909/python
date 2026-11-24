#faça um progema que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informaçoes possíveis sobre ele 
x = input("Digite algo: ")
print(f"o tipo primitivo desse valor é {type(x)}")
print(f"é alfanumérico? {x.isalnum()}")
print(f"é alfabético? {x.isalpha()}")
print(f"é numérico? {x.isdigit()}")
print(f"é decimal? {x.isdecimal()}")
print(f"é maiúsculo? {x.isupper()}")
print(f"é minúsculo? {x.islower()}")
#função IS 