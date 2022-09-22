"""
Crie um módulo chamado "moeda.py" que tenha as funções incorporadas "aumentar()", "diminuir()", "dobro()" e "metade()".
Faça também um programa que importe esse módulo e use algumas dessas funções.
"""

from Exercicios_107_a_112 import moeda

num = float(input('Digite um valor R$:'))
print(f'A metade de R$:{num:.2f} é R$:{moeda.metade(num):.2f}')
print(f'O dobro de R$:{num:.2f} é R$:{moeda.dobro(num):.2f}')
print(f'Aumentando 10% de R$:{num:.2f} temos R$:{moeda.aumentar(num, 10):.2f}')
print(f'Diminuindo 10% de R$:{num:.2f} temos R$:{moeda.diminuir(num, 10):.2f}')
