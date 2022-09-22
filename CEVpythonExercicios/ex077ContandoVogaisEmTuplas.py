"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

tpl = ('Aprender', 'Python', 'Estudar', 'Pragramar', 'Computador', 'Linguagem', 'Futuro', 'Mercado', 'Trabalhar')
for palavra in tpl:
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
