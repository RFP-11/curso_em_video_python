"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
"""

print('-=' * 20)
print(f'{"Somando números pares!":^40}')
print('-=' * 20)

c = 0
s = 0
for m in range(1, 7):
    n = int(input(f'Digite o {m}° número inteiro: '))
    if n % 2 == 0:
        s += n
        c += 1
print(f'Você informou {c} números PARES cuja soma é {s}')

# Otimizando o programa e inda além:
soma1 = 0
par = []
cont1 = 0
impar = []
cont2 = 0
soma2 = 0
vezes = int(input('Quantos números inteiros você quer informar? '))
for L in range(1, vezes + 1):
    num = int(input(f'Digite o {L}° número inteiro: '))
    if num % 2 == 0:
        par.append(num)
        soma1 += num
        cont1 += 1
    else:
        impar.append(num)
        soma2 += num
        cont2 += 1
print(f'Você informou {cont1} números PARES: {par}; e sua soma é: {soma1}')
print(f'Você informou {cont2} números ÍMPARES: {impar}; e sua soma é: {soma2}')
