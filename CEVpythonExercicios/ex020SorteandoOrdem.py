"""
O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

import random

n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
lst = [n1, n2, n3, n4]
random.shuffle(lst)  # Embaralha a ordem da lista.
print(f'\n'
      f'A ordem sorteada foi: \n{lst}\n')

# Agora vá além. Generalise o programa.

n = int(input('Digite a quantidade de alunos: '))
c = 1
lista = list(range(0, n))
while c <= n:
    lista.append(str(input(f'Digite o nome do {c}° aluno: ')))
    c += 1

random.shuffle(lista)
print(f'\n'
      f'A ordem de apresentaçção sorteada foi: \n{lista}')
