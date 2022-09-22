"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
"""
import random

n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))
lst = [n1, n2, n3, n4]
print(f'\n'
      f'O aluno sorteado foi: {random.choice(lst)}\n')

# Agora vá além. Faça o exercício de forma genérica.

n = int(input('Digite a quantidade de alunos: '))
c = 1
m = []
while c <= n:
    m.append(str(input(f'Digite o nome do {c}° aluno: ')))
    c += 1

print(f'\n'
      f'O aluno sorteado foi: {random.choice(m)}')
