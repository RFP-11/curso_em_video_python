"""
Escreva um programa em Python que leia:
    - um número inteiro qualquer;
    - peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
"""

print('-=-' * 20)
print(f'{"Convertendo Bases Numéricas!":^50}')
print('-=-' * 20)

n = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão:
1 = Binário;
2 = Octal;
3 = Hexadecimal.''')

e = int(input('Informe a sua escolha: '))

if e == 1:
      print(f'A converção de {n} para binário é: {bin(n)[2:]}')
elif e == 2:
      print(f'A conveção de {n} para octal é: {oct(n)[2:]}')
elif e == 3:
      print(f'A converção de {n} para hexadecimal é: {hex(n)[2:]}')
else:
      print('Opção invalida! Tente novamente.')
