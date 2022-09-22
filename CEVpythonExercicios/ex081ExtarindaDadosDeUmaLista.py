"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
    A) Quantos números foram digitados.
    B) A lista de valores, ordenada de forma decrescente.
    C) Se o valor 5 foi digitado e está ou não na lista.
"""

lst = []
while True:
    lst.append(int(input('Digite um número inteiro: ')))
    opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if opcao != 'S':
        break
print('-=' * 30)
print(f'Foram digitados {len(lst)} números')
lst.sort(reverse=True)
print(f'Os valores digitados em ordem decrescente foram: {lst}')
if 5 in lst:
    print('O número 5 foi encontraado na lista')
else:
    print('O número 5 não foi encontrado na lista')
