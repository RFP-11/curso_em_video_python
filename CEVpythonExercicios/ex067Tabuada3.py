"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
"""

print('-=' * 20)
print(f'{"Construindo a Tabuada!":^40}')
print('-=' * 20)

print('Informe um valor negativo para interromper o programa!')
while True:
    n = int(input('Quer saber a tabuada de qual número? '))
    if n < 0:
        break
    print('==' * 10)
    for c in range(1, 11):
        print(f'{n} x {c:>2} = {n * c}')
    print('==' * 10)
print('Pragrama de tabuada encerrado. \nVolte sempre!')
