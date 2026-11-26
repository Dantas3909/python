import random

p1 = input("Digite o nome do primeiro aluno: ")
p2 = input("Digite o nome do segundo aluno: ")  
p3 = input("Digite o nome do terceiro aluno: ")
p4 = input("Digite o nome do quarto aluno: ")
lista = [p1, p2, p3, p4]
random.shuffle(lista) # o método shuffle() do módulo random é usado para embaralhar aleatoriamente os elementos de uma lista. Neste caso, ele embaralha a lista "lista" contendo os nomes dos quatro alunos digitados pelo usuário.
print(f"Os alunos são: {lista}")