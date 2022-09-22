# Aula 13
# Estruturas de repetição com variável de controle — for (do inglês: para, por):
"""
Estrutura de controle.
Laços de repetições.
Estrutura "for"  =>  for c in range(início, fim, condição a mais):

Dentro do "for" precisamos de um contador "c" e de um "range".
    - O contador pode ser qualquer nome, mas escolhemos "c" por simplicidade.
    - O range define como será a repetição desejada.
"""

# O contador do "for" em python não conta o último número. Então de 1 a 6 ele conta 5 repetições, por exemplo:
for c in range(1, 6):
    print('Oi')
print('Fim!')

# Então se começar de 0 até 6 teremos as 6 repetições, por exemplo:
for c in range(0, 6):
    print('Oi')
print('Fim!')

# Contar sequêncialmente para frente de 0 a 6 fazemos:
for c in range(0, 6):
    print(c)
print('Fim!')

# A terceira casa dentro do range diz ao programa uma condição a mais para fazer.
# Contar para trás é só adicionar -1 na terceira casa do range, por exemplo:
for c in range(6, 0, -1):
    print(c)
print('Fim!')
# Contar pulando de dis em dos é ´so adicionar 2 na terceira casa do range, por exemplo:
for c in range(0, 10, 2):
    print(c)
print('Fim!')

# Exemplo mais elaborado:
print('Vamos imprimir os números em ordem crescente, defina:')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim!')

# Exemplo mais elaborado:
print('Vamos calcular um somatório, defina:')
f = int(input('Quantos valores quer somar: '))
s = 0
for c in range(0, f):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório dos valores é igual a: {s}.')
