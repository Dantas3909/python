#frase é uma sequência de caracteres entre aspas que cada letra é um elemento da sequência. Por exemplo, a frase "Olá, mundo!" é uma sequência de caracteres que contém letras, espaços e pontuação.

#fatiamento é o processo de extrair uma parte de uma sequência de caracteres. Por exemplo, a frase "Olá, mundo!" pode ser fatiada para obter apenas a palavra "Olá" usando a sintaxe frase[0:3], que retorna os caracteres do índice 0 ao índice 2 (o índice final não é incluído).

#se eu escrevo frase[9] ele vai me retornar o caractere que está na posição 9 da frase, que é o ponto de exclamação. Se eu escrever frase[9:13], ele vai me retornar os caracteres do índice 9 ao índice 12, que são "mundo". Se eu escrever frase[:5], ele vai me retornar os caracteres do início da frase até o índice 4, que são "Olá, ". Se eu escrever frase[7:], ele vai me retornar os caracteres do índice 7 até o final da frase, que são "mundo!".

frases = "Curso em Vídeo Python"
print(frases[9]) # vai me retornar o caractere que está na posição 9
print(frases[9:13]) # vai me retornar os caracteres do índice 9 ao índice 12
print(frases[:5]) # vai me retornar os caracteres do início da frase até o índice 4
print(frases[7:]) # vai me retornar os caracteres do índice 7 ao ínicio da frase até o final da frase
print(frases[9::2]) # vai me retornar os caracteres do índice 9 ao índice 20, pulando de 2 em 2

#analise de string é o processo de examinar uma sequência de caracteres para obter informações sobre ela. Por exemplo, podemos usar o método len() para obter o comprimento da frase, o método count() para contar quantas vezes um determinado caractere aparece na frase, o método find() para encontrar a posição de um determinado caractere na frase, e o método replace() para substituir um determinado caractere por outro na frase.

#len() é uma função que retorna o comprimento de uma sequência de caracteres. Por exemplo, len(frases) retornará 21, que é o número de caracteres na frase "Curso em Vídeo Python".

#count() é um método que conta quantas vezes um determinado caractere aparece em uma sequência de caracteres. Por exemplo, frases.count("o") retornará 2, que é o número de vezes que a letra "o" aparece na frase "Curso em Vídeo Python".

#find() é um método que encontra a posição de um determinado caractere em uma sequência de caracteres. Por exemplo, frases.find("V") retornará 9, que é a posição da letra "V" na frase "Curso em Vídeo Python".

#replace() é um método que substitui um determinado caractere por outro em uma sequência de caracteres. Por exemplo, frases.replace("Python", "Java") retornará "Curso em Vídeo Java", que é a frase original com a palavra "Python" substituída por "Java".
#frase.find("Curso") vai me retornar 0, que é a posição da palavra "Curso" na frase "Curso em Vídeo Python". Se eu escrever frase.find("Java"), ele vai me retornar -1, que significa que a palavra "Java" não foi encontrada na frase.

#