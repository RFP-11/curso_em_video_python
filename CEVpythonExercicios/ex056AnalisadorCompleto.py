"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
    — a média de idade do grupo;
    — qual é o nome do homem mais velho;
    — quantas mulheres têm menos de 20 anos.
"""

soma = 0
velho = 0
Hvelho = ''
cont = 0
for c in range(1, 5):
    print(f'{f" {c}° pessoa ":-^25}')
    nome = str(input(f'Nome: ')).strip().title()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo [M/F]: ')).strip().upper()
    soma += idade
    if sexo == 'M':
        if c == 1:
            velho = idade
            Hvelho = nome
        else:
            if idade > velho:
                velho = idade
                Hvelho = nome
    elif sexo == 'F':
        if idade < 20:
            cont += 1
    else:
        print('Entrada INVALIDA! Tente novamente.')
        exit()
print('\n')
print(f'A média de idades do grupo é de {soma / 4:.1f} anos')
print(f'O homen mais velho tem {velho} anos e se chama {Hvelho}')
print(f'Ao todo são {cont} mulheres abaixo dos 20 anos')

# A estrutura de repetição acima pode ser rescrita da seguinte forma:
somaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    print(f'----- {c}° pessoa -----')
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F}: ')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
print('\n')
print(f'A média de idades do grupo é de {somaidade / 4} anos')
print(f'O homen mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'Ao todo são {totmulher20} mulheres abaixo dos 20 anos')
