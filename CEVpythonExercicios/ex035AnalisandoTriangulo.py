"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""

print('-=-' * 20)
print('Analisando Triângulo')
print('-=-' * 20)

r1 = float(input('Tamanho da primeira reta: '))
r2 = float(input('Tamanho da segunda reta: '))
r3 = float(input('Tamanho da terceira reta: '))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('As retas podem formar um triângulo!')
else:
    print('As retas não podem formar um triângulo!')
