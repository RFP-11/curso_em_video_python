# Aula 07.
# Operadores Aritiméticos:

"""
+   simbolo de adição;                          Ex: 5 + 2 == 7
-   simbolo de subtração;                           5 - 2 == 3
*   simbolo de multiplicação;                       5 * 2 == 10
/   simbolo de divisão;                             5 / 2 == 2.5
**  simbolo de potência, ou exponenciação;          5 ** 2 == 25
//  simbolo de divisão inteira;                     5 // 2 == 2
%   simbolo de resto da divisão, ou modulo;         5 % 2 == 1
=   simbolo de atribuição, ou "recebe";
==  simbolo de igual;
!=  Simbolo de diferente;

Ordem de precedência:   1º: ()
                        2º: **
                        3º: *,/,// e %
                        4º: + e -
"""

# OBS: podemos usar " end=' ' " para evitar uma quebra de linhas entre dois prints em linhas distintas.
# E usar " \n " para fazer uma quebra de linha dentro de um mesmo print.

print('\n'
      'Apresentando as operações.')

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
print(f'As operações básicas de "{n1}" com "{n2}", são, respectivamente: '
      f'\n Soma: {n1 + n2} \n Subtração: {n1 - n2} \n Divisão: {n1 / n2} '
      f'\n Multiplicação: {n1 * n2} \n Potênciação: {n1 ** n2}')

print('\n'
      'OBS: algumas coisas interesantes! \n'
      'Podemos manipular os caracteres, da seguinte forma: \n')

nome = input('Digite um nome: ')
print(f'Prazer em te conhecer {nome}!')  # exemplo usando fstring
print(f'Prazer em te conhecer {nome:20}!')  # Preenche 20 espaços contando com o nome
print(f'Prazer em te conhecer {nome:>20}!')  # Preenche 20 espaços posicionando o nome a direita
print(f'Prazer em te conhecer {nome:<20}!')  # Preenche 20 espaços posicionando o nome a esquerda
print(f'Prazer em te conhecer {nome:^20}!')  # Preenche 20 espaços ao centralizar o nome
print(f'Prazer em te conhecer {nome:=^20}!')  # Preenche 20 espaços com o nome centralizado, completando-os com "="

print('\n'
      'No ambiente matemático também podemos manipular os caracteres!')
print(f'Numa dizima, por ex.: {4 / 3}')
print(f'Podemos limitar o número de casas. Como: {4 / 3:.2f}')  # Aqui :.2f significa 2 casas flutuantes.
