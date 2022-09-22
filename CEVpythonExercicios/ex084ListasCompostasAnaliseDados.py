"""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo numa lista.
No final, mostre:
    A) Quantas pessoas foram cadastradas.
    B) Uma listagem com as pessoas mais pesadas.
    C) Uma listagem com as pessoas mais leves.
"""

lst = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')).strip().title())
    dados.append(float(input('Peso [kg]: ')))
    if len(lst) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lst.append(dados[:])
    dados.clear()
    print('Dados cadastrados com sucesso! ', end='')
    opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if opcao != 'S':
        break
print('-=' * 30)
print(f'Foram cadastrados {len(lst)} pessoas.')
print(f'Listagem cadastrada: {lst}')
print(f'O maior peso registrado foi {maior} kg. Peso de ', end='')
for p in lst:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso registrado foi {menor} kg. Peso de ', end='')
for p in lst:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
print()
