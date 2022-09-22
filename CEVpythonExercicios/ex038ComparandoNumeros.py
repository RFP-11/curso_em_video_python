"""
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
    – O primeiro valor é maior
    – O segundo valor é maior
    – Não existe valor maior, os dois são iguais
"""

print('-=-' * 20)
print(f'{"Comparando qual Número é maior":^60}')
print('-=-' * 20)

a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))

if a > b:
    print('O PRIMEIRO valor é maior!')
elif b > a:
    print('O SEGUNDO valor é maior!')
else:
    print('Não existe valor maior, os dois são IGUAIS!')
