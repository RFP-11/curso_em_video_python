"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
e mostre seu status, de acordo com a tabela abaixo:
    – IMC abaixo de 18,5: Abaixo do Peso
    – Entre 18,5 e 25: Peso Ideal
    – 25 até 30: Sobrepeso
    – 30 até 40: Obesidade
    – Acima de 40: Obesidade Mórbida
"""

print('-=-' * 15)
print(f'{"Calculando IMC!":^40}')
print('-=-' * 15)

peso = float(input('Informe "peso" em Kg: '))
altura = float(input('Informa altura em metros: '))
imc = peso / altura ** 2
print(f'O IMC desta pessoa é de {imc:.1f} \nClássificação: ', end='')
if imc <= 18.5:
    print('Abaixo do Peso!')
elif imc <= 25:
    print('Peso Ideal!')
elif imc <= 30:
    print('Sobrepeso!')
elif imc <= 40:
    print('Obesidade!')
else:
    print('Obesidade Mórbida!')
