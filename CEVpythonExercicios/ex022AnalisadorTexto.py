"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
    - O nome com todas as letras maiúsculas e minúsculas.
    - Quantas letras no total tem o nome (sem considerar espaços).
    - Quantas letras tem o primeiro nome.
"""

nome = str(input('Digite seu nome completo: ')).strip()

print(f'\nOlá, senhor {nome.title()}. \nVamos analisar o seu nome:')
print(f'Seu nome em maiusculo é: {nome.upper()}')
print(f'Seu nome em minusculo é: {nome.lower()}')
print(f'O seu nome possui {len(nome)} caracteres.')
print(f'O seu nome possui {len(nome) - nome.count(" ")} letras.')
lst = nome.split()
print(f'O seu primeiro nome "{lst[0]}" possui {len(lst[0])} letras.')

# Outra forma de contar as letras do primeiro nome:
print(f'O seu primeiro nome possui {nome.find(" ")} letras')
# Ao encontrar o primeiro espaço, irá retornar sua posição na string, que corresponderá a quantidade de letras até ali.
# Pois lembre, o contador em python se inicia no 0.
