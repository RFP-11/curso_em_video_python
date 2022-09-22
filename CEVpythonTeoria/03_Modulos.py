# Aula 08
# Módulos:
"""
Aprendendo o comando "import".
O comando import serve para importar bibliotacas/modulos para dentro do python.

Se usado sozinho o comando "import" irá importa todas as funções do módulo desejada;

Se usado junto com "from" então ele irá importa apenas a função especificada.

Apertando "ctrl + epaço" na frente do comando "import" digitado usando ou não o "from" aparecem as opções das funções
da biblioteca que desejar usar. Vejamos alguns exemplos:
"""

import math  # importa toda a biblioteca matamática.
from math import sqrt, floor  # importa apenas as funções sqrt e floor.
import random  # importar a biblioteca "random" para cria números aleatórios.
import emoji  # importar a biblioteca 'emoji' que mostra emojis.

num = int(input('Digite um número inteiro: '))
raiz = math.sqrt(num)  # como importou tudo temos que especificar usando math.função_desejada, no caso aqui math.sqrt.
print(f'A raiz quadrada de {num} é igual a {raiz}')
print(f'A raiz quadrada de {num} com duas casas decimais é igual a {raiz:.2f}')
# Lembre-se que {:.2f} é usado para apresentar o número com duas casas flutuantes.
print(f'A raiz quadrada de {num} arredondada para cima é igual a {math.ceil(raiz)}')
# O comando "math.ceil()" arredonda o valor para cima.
print(f'A raiz quadrada de {num} arredondada para baixo é igual a {math.floor(raiz)}')
# O comando "math.floor()" aredonda o valor para baixo.

print('\n')

# from math import sqrt, floor  # importa apenas as funções sqrt e floor.

num = int(input('Digite um número inteiro: '))
raiz = sqrt(num)  # como já foi especificado não precisa usar math.
print(f'A raiz quadrada de "{num}" arredondado para baixo com duas casas decimais é igual a {floor(raiz):.2f}')
print(f'A raiz quadrada de "{num}" arredondado para cima com duas casas decimais é igual a {math.ceil(raiz):.2f}')
# como não especificou-se o "ceil" no "import", então tem que usar "math.ceil()".

print('\n')

# importar a biblioteca "random" para cria números aleatórios.
# import random

print('Vamos estudar números aleatórios:\n')

num = random.random()  # produz número alaatório entre 0 e 1.
print(f'Essa função produz um número aleatório entre 0 e 1: \n{num} \n')

num2 = random.randint(1, 10)  # produz número aleatória inteiro entre 1 e 10.
print(f'Essa função produz um número aleatório inteiro entre 1 e 10: \n{num2}')

print('\n')

# importar a biblioteca 'emoji' que mostra emojis.
# import emoji

print('Vamos aprender a mostrar emojis no python:\n')
print(emoji.emojize('"Olá, mundo" :sunglasses:', language='alias'))
print(emoji.emojize('"Olá, mundo" :heart:', language='alias'))
print(emoji.emojize('"Olá, mundo" :thumbsup:', language='alias'))
print(emoji.emojize('"Olá, mundo" :polegar_para_cima:', language='pt'))
print(emoji.emojize('"Olá, mundo" :sunny:', language='alias'))
# para ver a lista completa de emojis acesse o link: https://www.webfx.com/tools/emoji-cheat-sheet/
