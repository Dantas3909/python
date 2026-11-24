#O input() é uma função que permite ao usuário digitar um valor e o retorna como uma string.
#podemoos ultilizar de varias formas o comando de format, como {} ou f"{}" para exibir o valor digitado pelo usuário na tela ou podemos armazenar o valor digitado em uma variável e depois exibir essa variável na tela. por exemplo: print("Olá, {}".format(nome)) ou print("Olá, " + nome) ou print(f"Olá, {nome}!")
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
peso = input("Digite seu peso: ")
print(f"Meu nome é {nome}!, tenho {idade} anos e peso {peso} kg.")