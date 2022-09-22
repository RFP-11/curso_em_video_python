# Aula 10 e 12
# Condições:
"""
Comandos condicionais: if, elif, else.
Que significam: (se, senão se, senão)

    - Podemos usar apenas "if" - (condição simples), para quando necessário uma única condição;

    - Podemos usar em conjunto "if" e "else" - (condição composta), para impor até duas condições;

    - Podemos usar em conjunto "if", "elif" e "else" - (condições alinhadas), para impor mais de duas condições.
"""

# Ex. de condição simples:

# Fazendo uma saldação:
nome = str(input('Digite seu nome: ')).strip().title()
print(f'Olá, prazer em te conhecer {nome}.')
if nome == 'Rafael':
    print('Nome bonito!')
print('Bom dia!')

print('\n')

# Ex. de condições compostas:

# Fazendo uma saldação:
nome = str(input('Digite seu nome: ')).strip().title()
print(f'Olá, prazer em te conhecer {nome}.')
if nome == 'Rafael':
    print('Nome bonito!')
else:
    print('Esse é um nome muito popular.')
print('Bom dia!')
# O mesmo esquema acima, usando condições simplificadas, fica assim:
print('Nome bonito!' if nome == 'Rafael' else 'Esse é um nome muito popular.')
print('Bom dia!')

print('\n')

# Média entre duas notas:
a = float(input('Digite a nota da P1: '))
b = float(input('Digitr a nota da P2: '))
c = (a + b) / 2
if c <= 5:
    print(f'Sua nota é: {c}. \nEstude mais.')
else:
    print(f'Sua nota é: {c}. \nParabéns!')
# O mesmo esquema acima, usando condições simplificadas, fica assim:
print(f'Sua nota é: {c}')
print('Estude mais.' if c <= 5 else 'Parabéns!')

print('\n')

# Ex. de condições multiplas:

# Fazendo uma saldação:
nome = str(input('\nQual é o seu nome? ')).strip().title()
print(f'Prazer em te conhecer {nome}!')
if nome[:6] == 'Rafael':
    print('Nossa! Que nome bonito.')
elif nome[:5] == 'Pedro' or nome[:5] == 'Maria' or nome[:5] == 'Lucas':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana, Cláudia, Jéssica, Juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')
lst = nome.split()
print(f'Tenha um bom dia, {lst[0]}.')

print('\n')

# Calculando a média:
print('Vamos calcular uma média aritimética bimestral de 3 provas! ')
n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
n3 = float(input('Digite a 3ª nota: '))
m = (n1 + n2 + n3) / 3
if m < 6:
    print(f'Sua nota é: {m:.1f}. \nVocê está abaixo da média. Precisa estudar mais.')
elif 6 <= m <= 7:
    print(f'Sua nota é: {m:.1f}. \nVocê está na média. Mas, atenção nos estudos.')
elif 7 <= m <= 8:
    print(f'Sua nota é: {m:.1f}. \nVocê está acima da média.')
else:
    print(f'Sua nota é: {m:.1f}. \nParabéns!')
