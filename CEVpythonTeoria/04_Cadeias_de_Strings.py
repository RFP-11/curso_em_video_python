# Aula 09
# Manipulando cadeias de texto ou caracteres ou string:
"""
Uma “string” sempre tem posição inicial em 0, e os espaços também são contados.

Dica legal: para fazer "print" de várias linhas em simultâneo, como um parágrafo num texto,
pode-se usar aspas triplas simples ou duplas. Ex.: print('''texto''')
"""

print('Exemplo de "print" usando aspas triplas:')
print("""
-------------------------------------
*************************************
-------------------------------------
""")

# técnica de fatiamento:
print('\n'
      'Técnica de "Fatiamento":\n')

frase = 'Curso em Vídeo Python'  # string com 21 caracteres, começando de 0 até 20, contando os espaços também.

print(f'Frase: "{frase}"\n')

print(f'A frase possuí {len(frase)} caracteres')
# A funçõo "len()" mede o espaço da string. Ou seja, conta os caracteres que compõe a string.

print(f'O 9ª caractere é: {frase[9]}')  # seleciona a letra de número 9 da string.

print(f'As letras de 9ª a 13ª posição são: {frase[9:14]}')
# seleciona as letras de 9 a 14, mas exclui a 14, ou seja, não inclui o ultimo valor.

print(f'As letras de 9ª a 20ª posição, pulando de 2 em 2 são: {frase[9:21:2]}')
# seleciona de 9 até 21 pulando de 2 em 2, mas lembre que não seleciona o 21.

print(f'As letras até o 4ª caractere são: {frase[:5]}')
# seleciona de 0 até 5. Quando não indicamos o limite inicial ele começa do primeiro caractere.

print(f'As letras a partir do 15ª caracter são: {frase[15:]}')
# seleciona de 15 até o final. Quando não indicamos um limite final, ele lê até o último caractere.

print(f'As letras a partir do 9ª caractere, pulando de 3 em 3 são: {frase[9::3]}')
# seleciona de 9 até o final, pulando de 3 em 3.

print('''
***********************************
***********************************
''')

"""
Técnica de análise:

"len()" mede o tamanho ou comprimento de uma string, ou seja, o número de quantos caracteres tem a string.

".count('o')" conta quantas vezes aparece a letra 'o' na string.
Ex.: '.count('t',0,13)' faz a contagem com fatiamento, ou seja, conta quantos 't' existem de 0 até 12.

".find('o')" encontra a posição onde começou a aparecer a string 'o'.
Se ".find()" retornar -1 é porque a string pesquizada não existe.

podemos usar o operador 'in' para saber se existe uma palavra desejada numa string.
Ex.: 'curso' in frase , ou, 'a' in frase.
Procura dendro da lista frase se existe as strings 'curso' ou 'a', e retorna True ou False.
"""

print('\n'
      'Técnica de "Análise":\n')

Frase = input('Digite uma frase: ')

print(f'Frase: {Frase}\n')

print(f'A frase possui {len(Frase)} caracteres')
print(f'Na frase as letras pulando de 2 em 2 são: {Frase[::2]}')
print(f'Na frase as letras até o 10ª caractere, pulando de 2 em 2 são: {Frase[:11:2]}')
print(f'A frase possui {Frase.count("a")} caracteres "a"')
print(f'A frase possui {Frase.count("b", 0, 10)} caracteres "b" entre a posição 0 e 10.')
print(f'Na frase a palavra "zebra" começam na posição {Frase.find("zebra")}.')
print(f'A frase possui a palavra "vida"?  {"vida" in Frase}.')
print(f'A letra "A" aparece na frase {frase.count("A")} vezes.')
print(f'A primeira letra "A" aparece na posição {frase.find("A") + 1}')
print(f'A última letra "A" aparece na posição {frase.rfind("A") + 1}')

print('''
***********************************
***********************************
''')
"""
Técnica de Formatação:

".replace('a','b')" é usada para trocar/substitui elementos na string, no caso aqui: 'a' por 'b'.

".upper()" é usada para por elementos da string em Maiusculo. Troca tudo de minusculo para Maiusculo.

".lower()" é usada para por elementos da string em minusculo. Troca tudo de Maiusculo para minusculo.

".capitalize()" é usada para mudar toda string para minusculo, exceto a primeira letra da string.

".title()" é usada para mudar a primeira letra de todas as palavras da string para Maiusculo.

".strip()" é usada para remover espaços desnecessários na string, como espaços no início ou no final da frase.

".rstrip()" é usada para remover só os ultimos espaços desnecessários da string, os do final da frase.

".lstrip()" é usada para remover só os primeiros espaços desnecessários da string, os do início da frase.
"""

print('\n'
      'Técnica de "Formatação":\n')

frase = '    Curso em Vídeo Python   '

print(f'Frase: "{frase}":\n')

print(f'trocando "Curso" por "Aprender" na frase: "{frase.replace("Curso", "Aprender")}"')
print(f'trocando as letras para Maiusculo na frase: "{frase.upper()}"')
print(f'trocando as letras para minusculo na frase: "{frase.lower()}"')
print(f'trocando as letras para minusculo, exceto a primeira: "{frase.capitalize()}"')
print(f'trocando as primeiras letras de cada palavra para Maiusculo: "{frase.title()}"')
print(f'retirando todos os espaços desnecessários da frase: "{frase.strip()}"')
print(f'retirando os espaços desnecessários no final da frase: "{frase.rstrip()}"')
print(f'retirando os espaços desnecessários no início da frase: "{frase.lstrip()}"')

print('''
***********************************
***********************************
''')

"""
Técnicas de divisão e junção:

".split()" divide a string dentro de uma "lista" com cada palavra da frase sendo um elemento da lista.

"'-'.join(frase)" substitue os espaços entre as palavras por '-' ou outra coisa que esteja entre aspas simples.
"""

print('\n'
      'Técnica de "Divisão e Junção":\n')

frase = 'Curso em Vídeo Python'

print(f'Frase: {frase}\n')

print(f'Usando a função split na frase: "{frase.split()}"')
print(f'Usando a função join na frase: "{"-".join(frase)}"')
print(f'Usando a função join na frase: {"@".join(frase)}')
print(f'Usando a função join na frase: {"%".join(frase)}')

print('''
***********************************
***********************************
''')

"""
Dica:
Pode-se fazer atribuições de funções ao declarar uma variável. Por Ex.:
Ex.1: lista = frase.split().
Ex.2: maiuculo = frase.upper()
Enfim, pode-se fazer várias manipulação, incluindo composição entre as funções:
"""

print('\n'
      'Agora algumas dicas a mais:\n')

frase = 'Curso em Vídeo Python'

troca = frase.replace('Curso', 'Aprender')
print(troca)

Maiusculo = frase.upper().replace('Python', 'Android')
print(Maiusculo)

minusculo = troca.lower()
print(minusculo)

lista = frase.split()
print(lista[0])  # aqui será mostrado o primeiro item da lista criada.
print(lista[1])  # aqui será mostrado o segundo item da lista criada.
print(lista[2])  # aqui será mostrado o terceiro item da lista criada.
print(lista[3])  # aqui será mostrado o quarto item da lista criada.
print(lista[0][3])  # aqui será mostrado a terceira letra do primeiro item da lista criada.
print(lista[2][1])  # aqui será mostrado a segunda letra do terceiro item da lista criada.

print('\n'
      'FIM DA AULA...')
