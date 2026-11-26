import random

a1 = input("nome do aluno: ")
a2 = input("nome do segundo aluno: ")
a3 = input("nome do terceiro aluno: ")
a4 = input("nome do quarto aluno: ")
lsita = [a1, a2, a3, a4] # para fazer uma lista de coisa basta colocar os elementos entre colchetes e separados por vírgula. Neste caso, a lista "lsita" contém os nomes dos quatro alunos digitados pelo usuário.

sorteio = random.choice(lsita) # o método choice() do módulo random é usado para selecionar aleatoriamente um elemento de uma lista. Neste caso, ele seleciona um aluno da lista "lsita" e armazena o resultado na variável "sorteio".

print(f"O aluno sorteado foi: {sorteio}")