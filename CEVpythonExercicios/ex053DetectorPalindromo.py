"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Exemplos de palíndromos:
    — APOS A SOPA;
    — A SACADA DA CASA;
    — A TORRE DA DERROTA;
    — O LOBO AMA O BOLO;
    — ANOTARAM A DATA DA MARATONA.
"""

frase = str(input('Digite uma frase: ')).strip().upper()
lst = frase.split()  # Separa as palavras da frase dentro de uma lista;
junta = ''.join(lst)  # Junta todas as palavras da lista, removendo qualquer espaço interno.
inverso = ''
for c in range(len(junta) - 1, -1, -1):  # Conta a letra da última posição até 0. Ou seja, lê de trás para frente.
    inverso += junta[c]
print(f'{junta}  X  {inverso}')
if inverso == junta:
    print('A frase é um palindromo!')
else:
    print('A frase não é um palindromo!')

# Usando a tecnica de fatiamento o programa fica assim:
frase = str(input('Digite uma frase: ')).strip().upper()
lst = frase.split()  # Separa as palavras da frase dentro de uma lista;
junta = ''.join(lst)  # Junta todas as palavras da lista, removendo qualquer espaço interno.
inverso = junta[::-1]
print(f'{junta}  X  {inverso}')
if inverso == junta:
    print('A frase é um palindromo!')
else:
    print('A frase não é um palindromo!')
