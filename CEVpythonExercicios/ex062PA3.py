"""
Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
"""

print('-=-' * 15)
print(f'{"Progressão Aritimétrica":^40}')
print('-=-' * 15)

primeiro = int(input('Informe o pirmeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
print('Os 10 primeiros termos da PA são: ')
seguinte = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{seguinte}, ', end='')
        seguinte += razao
        cont += 1
    print('...')
    mais = int(input('Quantos termos você quer que sejam mostrados a mais? '))
print(f'Programa finalizado com {total} termos apresentados.')
