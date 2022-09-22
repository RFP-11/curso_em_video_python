#  Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cit = str(input('Em que cidade você nasceu? ')).strip()
print(cit[:5].upper() == 'SANTO')

print('\n')

# Outra forma de fazer, mas sem saber se começa com a palavra, mas se tem a palavra no nome.
cidade = str(input('Em que cidade você nasceu? ')).strip().lower()
print("santo" in cidade)
