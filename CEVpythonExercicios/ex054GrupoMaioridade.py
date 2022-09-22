"""
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""

from datetime import date

atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input(f'Digite o ano de nascimento da {c}° pessoa: '))
    print(f'Ano do nascimento: {nasc}. Idade: {atual - nasc} anos')
    if atual - nasc >= 21:
        maior += 1
    else:
        menor += 1
print(f'Dos dados informados {maior} pessoas atingiram a maioridade e {menor} pessoas são menores de idade.')
