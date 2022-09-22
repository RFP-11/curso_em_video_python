"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

a = float(input('Digite um número: '))
b = float(input('Digite um segundo número: '))
c = float(input('Digite um terceiro número: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O menor número é: {menor}')
print(f'O maior número é: {maior}')
