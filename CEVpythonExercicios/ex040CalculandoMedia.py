"""
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
    – Média abaixo de 5.0: REPROVADO
    – Média entre 5.0 e 6.9: RECUPERAÇÃO
    – Média 7.0 ou superior: APROVADO
"""

print('-=-' * 15)
print(f'{"Calculando a média!":^40}')
print('-=-' * 15)
print('Informe as notas no intervalo de 0 a 100 pontos!')
n1 = float(input('1ª nota: '))
n2 = float(input('2ª nota: '))
media = (n1 + n2) / 2
print(f'Sua nota final é: {media:.1f}')
if media < 50:
    print('Você está REPROVADO!')
elif 70 > media > 50:
    print('Você está de RECUPERAÇÃO!')
else:
    print('Parabéns, você foi APROVADO!')
