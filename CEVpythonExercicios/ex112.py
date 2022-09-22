"""
No pacote "Exercicios_107_a_112" que criamos no "desafio 111", temos um módulo chamado "dados".
Crie uma função chamada "leiaDinheiro()" que consiga funcionar como a função "input()", mas com uma validação
de dados para aceitar apenas valores que sejam monetários.
"""

from Exercicios_107_a_112 import dados, moeda

n = dados.leiaDinheiro('Digite um valor: ')
print(f'Você digitou o valor {moeda.fmoeda(n)}')
moeda.resumo(n, 25, 15)
