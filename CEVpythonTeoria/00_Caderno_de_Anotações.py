"""
Este é meu caderno de anotações.
Aqui vou escrever todos os comandos usados com frequência ou observações importantes.
"""

import math
raiz1 = math.sqrt(9)  # Calcula a raiz quadrada de 9;

import random
a = random.randint(0, 5)  # Produz um número aleatório entre 0 e 5;

import time
time.sleep(3)  # Dá uma pausa de 3 segundos;

from math import sqrt, sin
raiz2 = sqrt(9)  # Calcula a raiz quadrada de 9;
angulo = math.radians(90)  # Transforma o angulo de 90° para "\pi/2" rad;
seno2 = sin(angulo)  # Calcula o seno de "\pi/2", por padrão calcula em radianos;

from random import randint
c = randint(0, 5)  # Produz um número aleatório entre 0 e 5;

from time import sleep
sleep(5)  # Dá uma pausa de 5 segundos;

from datetime import date
ano = date.today().year  # Mostra o ano atual puchando do computaodor.

import matplotlib.pyplot as plt
x = (1, 2, 3, 4, 5)
y = (1, 4, 9, 16, 25)
plt.plot(x, y, 'ro')
plt.show()  # Produz um gráfico 2d;

import numpy as np
t = np.arange(-2, 2.1, 0.1)  # Produz lista com intervalo de -2 a 2 e densidade de 0.1 entre pontos
print(t)

# Para juntar todas as letras de uma frase, eliminando qualquer espaço, podemos fazer:
frase = str(input('Digite uma frase: ')).strip().upper()
lst = frase.split()  # Separa as palavras da frase dentro de uma lista;
junta = ''.join(lst)  # Junta todas as palavras da lista, removendo qualquer espaço interno.

# Laços de repetição:
letra = str(input('Informe M ou F: '))
while letra != 'M':
    letra = str(input('Dado invalida! Por favor, informe M ou F: '))
while letra not in 'MmFf':
    letra = str(input('Dado invalida! Por favor, informe M ou F: '))

nome = 'Rafael'
print(f'Prazer em te conhecer {nome:20}!')  # Preenche 20 espaços contando com o nome
print(f'Prazer em te conhecer {nome:>20}!')  # Preenche 20 espaços posicionando o nome a direita
print(f'Prazer em te conhecer {nome:<20}!')  # Preenche 20 espaços posicionando o nome a esquerda
print(f'Prazer em te conhecer {nome:^20}!')  # Preenche 20 espaços ao centralizar o nome
print(f'Prazer em te conhecer {nome:=^20}!')  # Preenche 20 espaços com o nome centralizado, completando-os com "="

"""
Diferença entre os comandos "or" e "and":
    - "or": se uma das condições ou premisas forem verdadeiras o laço é executado;
    - "and" todas as premissas devem ser verdadeiras para o laço ser executado.
"""
#

from random import randint
tpl = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print('Os valores sorteados foram: ', end='')
for c in tpl:
    print(f'{c}', end=' ')
print(f'\nO maior número é: {max(tpl)}')
print(f'O menor número é: {min(tpl)}')


tpl = ('Aprender', 'Python', 'Estudar', 'Pragramar', 'Computador', 'Linguagem', 'Futuro', 'Mercado', 'Trabalhar')
for palavra in tpl:
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
print()

# Criando função que sorteia números aleatórios e salva numa lista.
from random import randint
def sorteia(f1=0, f2=0):
    lst = []
    for c in range(0, f1):
        lst.append(randint(0, f2))
    return lst[:]
numeros = sorteia(int(input('Quantidade de numeros aleatórios para sortear: ')),
                  int(input('Sortear números no intervalo [0, n]. Informe "n": ')))
print(f'Os números sorteados foram {numeros}')
print(f'Os números sorteados foram {sorteia(5, 100)}')
print()

# Função para validação de um número inteiro de entrada, útil para evitar os erros da unção "int()":
def leiaInt(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('ERRO! Digite um número inteiro válido')
    return num
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')
