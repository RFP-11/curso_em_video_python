"""
Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
"""

# Fazendo uma única pesquiza:
n = int(input('Digite um número para pesquizar sua tabuada: '))
for c in range(0, 11):
    print(f'{n} X {c:2} = {n * c}')
print('Fim!')

# Optmizando o processo para várias pesquizas:
escolha = "S"
while escolha == 'S':
    n = int(input('Digite um número para pesquizar sua tabuada: '))
    for c in range(0, 11):
        print(f'{n} X {c:2} = {n * c}')
    print('Fim!')
    escolha = str(input('Deseja fazer outra pesquiza: (S = Sim; N = Não) ')).strip().upper()
print('Fim!')
