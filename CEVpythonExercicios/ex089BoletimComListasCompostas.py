"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo numa lista composta. No final:
    — Mostre um boletim contendo a média de cada um;
    — Permita que o usuário possa escolher que seja mostrado as notas de cada aluno individualmente.
"""

print('==' * 20)
print(f'{"Cadastro Escola Python":^40}')
print('==' * 20)

lst = []
dados = []
while True:
    dados.append(str(input('Nome: ')).strip().title())
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    dados.append(n1)
    dados.append(n2)
    dados.append(media)
    lst.append(dados[:])
    dados.clear()
    opcao = str(input('Deseja fazer um novo cadastro? [S/N]: ')).strip().upper()[0]
    if opcao != 'S':
        break
print('==' * 20)
print(f'{"N°":<4}', end='')
print(f'{"Nome":<10}', end='')
print(f'{"Média":>5}')
print('--' * 12)
for L in range(0, len(lst)):
    print(f'{L:<4}', end='')
    for c in range(0, 4):
        if c == 0:
            print(f'{lst[L][c]:<10}', end='')
        elif c == 3:
            print(f'{lst[L][c]:>5.1f}')
print('--' * 12)
while True:
    n = int(input('Mostrar notas de qual aluno? (999 interrompe!). N°: '))
    if n == 999:
        print('Finalizado!')
        break
    if n <= len(lst) - 1:
        print(f'As notas de {lst[n][0]} são: {lst[n][1:3]}')
    print('--' * 20)
print(f'{"<<< Volte sempre >>>":^30}')

"""
Podemos ainda fazer o programa de outra forma:
"""
# Outra forma de fazer é:
ficha = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>8}')
print('--' * 15)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('--' * 15)
    opc = int(input('Mostrar qual aluno? (999 interrompe). N°: '))
    if opc == 999:
        print('FINALIZANDO!')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE! >>>')
