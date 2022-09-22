"""
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""

lst = []
for c in range(0, 5):
    num = int(input(f'Digite o {c + 1}° valor inteiro: '))
    if c == 0 or num > lst[-1]:
        lst.append(num)
        print('Adicionado ao final da lista!')
    else:
        p = 0
        while p < len(lst):
            if num <= lst[p]:
                lst.insert(p, num)
                print(f'Adicionado na posição {p} da lista!')
                break
            p += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram: {lst}')
