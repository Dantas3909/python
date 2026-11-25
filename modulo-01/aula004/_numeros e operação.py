#seguindo os exemplos anteriores(ex003), vamos falar sobre números e operações matemáticas. Em Python, podemos realizar operações matemáticas básicas como adição (+), subtração (-), multiplicação (*), divisão (/), potência (**), módulo (%) e divisão inteira (//).
#para fazer uma operação matemática, temos que indentifiar os números que vamos utilizar e o operador matemático que vamos aplicar. Por exemplo, para somar dois números, podemos fazer assim:
#jogando os tipos primitivos para dentro do input() podemos fazer a operação matemática diretamente, sem precisar armazenar os valores em variáveis. Por exemplo:
#variavel = o tipo primitivo(input("algo"))
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
s = n1/n2
print(f"A divisão de {n1} e {n2} é {s}")
print(f"O tipo do valor {s} é {type(s)}")

# O .2f formata o número para exibir 2 casas decimais (ideal para valores em dinheiro, como centavos).

# : inicia a formatação dentro da f-string.

# .2 define 2 dígitos após o ponto decimal.

# f indica um número de ponto flutuante (float).