"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

lst = []
while True:
    num = float(input('Digite um valor numérico: '))
    if num in lst:
        print('Numero já existente!')
    else:
        lst.append(num)
    opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if opcao != 'S':
        break
lst.sort()
print(f'Você digitou os seguintes valores: {lst}')
