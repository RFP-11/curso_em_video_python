"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

Ex: Ana Maria de Souza
    primeiro = Ana;
    último = Souza.
"""

nome = str(input('\nDigite seu nome completo: ')).strip().title()
print(f'\nPrazer em te conhecer {nome}!')
lst = nome.split()
print(f'Seu primeiro nome é: {lst[0]}')
print(f'Seu último nome é: {lst[len(lst) - 1]}')
