"""
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
    – EQUILÁTERO: todos os lados iguais
    – ISÓSCELES: dois lados iguais, um diferente
    – ESCALENO: todos os lados diferentes
"""

print('-=-' * 15)
print(f'{"Analisando Triangulos!":^40}')
print('-=-' * 15)

a = float(input('Valor de 1ª segmento: '))
b = float(input('Valor do 2ª segmento: '))
c = float(input('Valor de 3ª segmento: '))
if a < b + c and b < a + c and c < a + b:
    print(f'Os seguimentos acima PODEM FORMAR um triângulo ', end='')
    if a == b == c:
        print('EQUILÁTERO!')
    elif a != b != c != a:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print(f'Os seguimentos acima NÃO PODEM FORMAR um triângulo!')
