"""
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""

soma = c = maior = menor = 0
escolha = 's'
while escolha in 'Ss':
    n = int(input('Digite um numero inteiro: '))
    if c == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    soma += n
    c += 1
    escolha = str(input('Deseja continuar? [S/N]: ')).strip()[0]
print(f'Você digitou {c} números e a média foi {soma / c:.2f}')
print(f'O maior valor digitado foi {maior} e o menor foi {menor}')
