# Desenvolva um script em python que leia as duas notas de um aluno, calcule e mostre sua média.

n1 = float(input('Digite a 1ª nota do aluno: '))
n2 = float(input('Digite a 2ª nota do aluno: '))
print(f'\n'
      f'A média aritimética do aluno é: {(n1 + n2) / 2}')

print('\n')

# Agora faça além. Pergunte a quantidade de provas e mostre a média.

provas = int(input('Informe a quantidade de provas: '))
c = 0
bruto = 0
while c <= (provas - 1):
    bruto += float(input(f'Digite a nota da P{c+1}: '))
    c += 1
print(f'\n'
      f'A média do Aluno é: {bruto/c}')
