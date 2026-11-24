#Os principais tipos primitivos em Python são: int (números inteiros), float (números decimais), str (cadeias de caracteres) e bool (valores booleanos).
#Exemplos de cada tipo primitivo:
#numero_inteiro = 10
#numero_decimal = 10.5
#texto = "Olá, mundo!"
#valor_logico = True or False
#exemplo de como podemos verificar o tipo de uma variável usando a função type():
n1 = int(input("Digite um número inteiro: "))
n2 = float(input("Digite um número decimal: "))
print(f"O tipo do valor {n1} é {type(n1)}")
print(f"O tipo do valor {n2} é {type(n2)}")
#boleanos são valores lógicos que podem ser True ou False, e são usados para representar condições ou estados. Podemos criar uma variável booleana e atribuir um valor a ela usando o sinal de igual (=).   
n3 = bool(input("Digite um valor booleano (True ou False): "))
print(f"O tipo do valor {n3} é {type(n3)}")
