"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]  # comandos: sem espaços, maiúsculo, só a 1ª letra.
while sexo != 'M' and sexo != 'F':
    print('Entrada INVALIDA! Tente novamente.')
    sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]

# Pode-se fazer ainda da seguinte forma:
sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dado inválido! Por favor, informe o sexo [M/F]: ')).strip().upper()[0]
print(f'Sexo {sexo} informado com sucesso.')
