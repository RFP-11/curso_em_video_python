"""
Crie um programa que vai ler vários números e colocar em uma lista.
Crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""

lst = []
while True:
    lst.append(int(input('Digite um valor inteiro positivo: ')))
    opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if opcao != 'S':
        break

par = []
impar = []
for c in lst:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print('-=' * 30)
print(f'Os valores digitados foram: {lst}')
print(f'Os valores pares são: {par}')
print(f'Os valores ímpares são: {impar}')
