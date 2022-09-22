"""
Faça um programa que leia uma frase pelo teclado e mostre:
    - quantas vezes aparece a letra "A".
    - em que posição ela aparece pela primeira vez.
    - em que posição ela aparece na última vez.
"""

frase = str(input('Digite uma frase: ')).strip().upper()

print(f'A letra "A" aparece na frase {frase.count("A")} vezes.')
print(f'A primeira letra "A" aparece na posição {frase.find("A") + 1}')
print(f'A última letra "A" aparece na posição {frase.rfind("A") + 1}')
