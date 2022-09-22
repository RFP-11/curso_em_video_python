# Faça um programa em python que leia um número inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Quer saber a tabuada de qual número: '))
c = 0
while c <= 10:
    print(f'{n} x {c} = {n*c}')
    # c = c + 1
    c += 1
