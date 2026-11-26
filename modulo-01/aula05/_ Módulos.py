# Módulos é uma forma de organizar o código em arquivos separados, permitindo a reutilização de funções, classes e variáveis em diferentes partes do programa. Conecida como blibliotecas, os módulos podem ser importados para serem utilizados em outros arquivos Python, facilitando a manutenção e a legibilidade do código.

#são essas com a priemria nomecladura de módulos, que são arquivos com a extensão .py, contendo código Python que pode ser reutilizado em outros programas. Para utilizar um módulo, você pode importá-lo usando a palavra-chave "import" seguida do nome do móduloou usando a sintaxe "from módulo import função". Por exemplo, se você tiver um módulo chamado "meu_modulo.py", você pode importá-lo em outro arquivo Python assim:

#import é um comando que agrupa varias funçãos 

# O comando from iimporta funçoes específicas de um módulo

# import math é para importar o módulo math, que contém funções 

# matemáticas como seno, cosseno, logaritmo, etc. Por exemplo, você pode usar a função sqrt() do módulo math para calcular a raiz quadrada de um número:

#ceil é uma função do módulo math que arredonda um número para cima, retornando o menor inteiro maior ou igual ao número fornecido. Por exemplo, math.ceil(4.2) retornará 5.

# floor é uma função do módulo math que arredonda um número para baixo, retornando o maior inteiro menor ou igual ao número fornecido. Por exemplo, math.floor(4.2) retornará 4.

#trunc é uma função do módulo math que remove a parte decimal de um número, retornando apenas a parte inteira. Por exemplo, math.trunc(4.7) retornará 4.

#pow é uma função do módulo math que calcula a potência de um número. Por exemplo, math.pow(2, 3) retornará 8, que é 2 elevado à potência de 3.

#sqrt é uma função do módulo math que calcula a raiz quadrada de um número. Por exemplo, math.sqrt(16) retornará 4, que é a raiz quadrada de 16.

#factorial é uma função do módulo math que calcula o fatorial de um número inteiro não negativo. Por exemplo, math.factorial(5) retornará 120, que é o fatorial de 5 (5! = 5 * 4 * 3 * 2 * 1).

# import random é para importar o módulo random, que contém funções para gerar números aleatórios. Por exemplo, você pode usar a função randint() do módulo random para gerar um número inteiro aleatório dentro de um intervalo específico:

# import datetime é para importar o módulo datetime, que contém classes e funções para trabalhar com datas e horários. Por exemplo, você pode usar a classe datetime.datetime para obter a data e hora atual:

# import os é para importar o módulo os, que contém funções para interagir com o sistema operacional. Por exemplo, você pode usar a função os.listdir() para listar os arquivos em um diretório específico

# Pode usar tambem o comando "from os import path" para importar apenas a função path do módulo os, que permite manipular caminhos de arquivos e diretórios.
import math 
num = int(input("Digite um número: "))
raiz = math.sqrt(num) #a função sqrt() calcula a raiz quadrada de um número. 
print(f"A raiz de {num} é {raiz}")
