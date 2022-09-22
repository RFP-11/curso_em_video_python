# Aula 19
# Variáveis Compostas - Dicionários:
"""
Para "Tuplas" são usados os parênteses ();
Para as "Listas" usamos os colchetes [];
Para os "Dicionários" usamos as chaves {};

Nos dicionários podemos personalizar o nome da posição dos seus elementos. Assim, não precisa ser 0, 1, 2, ...

Podemos criar "dicionários vazios" usando "dict()" ou simplesmente "{}".
"""

# Criando um dicionário qualquer:
rafael = dict()
Rafael = {}
dic = {}

# Inserindo ou removendo elementos do dicionário:
dados = {'nome': 'Pedro', 'idade': 25}  # Comando declarando um dicionário já com 2 elementos internos
print(dados['nome'])  # Mostra apenas "Pedro"
print(dados['idade'])  # Mostra apenas "25"
dados['sexo'] = 'M'  # Adiciona "'sexo': 'M'" na ultima posição do dicionário
print(dados)  # Mostra o dicionário completo como foi digitado
print(dados['sexo'])  # Mostra apenas "M"
del dados['idade']  # Deleta "'idade': 25" do dicionário
print(dados)  # Mostra o dicionário completo como foi digitado

# Os dicionários possuem "Valores" e "Chaves" que representam cada ítem, apresentados da seguinte forma:
filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'
         }
print(filme.values())  # Retorna todos os valores do dicionário: "Star Wars", 1977, "George Lucas"
print(filme.keys())  # Retorna as chaves de posição: "titulo", "ano", "diretor"
print(filme.items())  # Retorna todos os ítens do dicionário. Útil para ser usado em "Laços/Estruturas de repetição"
print(filme)  # Difere do comando anterior. Retorna o dicionário como foi digitado.

for k, v in filme.items():
    print(f'O {k} é {v}')  # Retorna: "O título é Star Wars"  \n   "O ano é 1977"  \n   "O diretor é George Lucas"

# Podemos ter "dicionários" dentro de "listas", por exemplo:
locadora = [{'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'},
            {'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'},
            {'titulo': 'Matrix', 'ano': 1999, 'diretor': 'Wachowski'}]
print(locadora[0]['ano'])
print(locadora[2]['titulo'])

# Entendendo os "valores" as "chaves" e os "ítens" do dicionário:
pessoa = {'Nome': 'Rafael', 'Sexo': 'M', 'Idade': 27}
print(pessoa)
print(pessoa['Nome'])  # para declarar usamos "{}", para chamar usamos "[]", fique atento!!!
print(pessoa['Idade'])
print(f'O {pessoa["Nome"]} tem {pessoa["Idade"]} anos.')
print(pessoa.keys())  # dict_keys(['Nome', 'Sexo', 'Idade'])
print(pessoa.values())  # dict_values(['Rafael', 'M', 27])
print(pessoa.items())  # dict_items([('Nome', 'Rafael'), ('Sexo', 'M'), ('Idade', 27)])
for k in pessoa.keys():
    print(k)
for v in pessoa.values():
    print(v)
for k, v in pessoa.items():  # OBS: O comando ".items()" é equivalente ao "enumerate()" usados nas "listas"
    print(f'{k} = {v}')

Pessoas = {'Nome': 'Rafael', 'Sexo': 'M', 'Idade': 27}
del Pessoas['Sexo']  # deleta "'sexo': 'M'"
Pessoas['Nome'] = 'Fábio'  # Troca 'Rafael' por 'Fábio'
Pessoas['Peso'] = 78.2  # Adiciona "'Peso': 78.2". Note, nos "dicionários" não temos o comando ".append()"
for k, v in Pessoas.items():
    print(f'{k} = {v}')

# Entendendo como funciona "dicionários" dentro de "listas":
brasil = []
estado1 = {'UF': 'Rio de Janeiro', 'sigla': 'RJ', 'região': 'Sudeste'}
estado2 = {'UF': 'São Paulo', 'sigla': 'SP', 'região': 'Sudeste'}
estado3 = {'UF': 'Amazonas', 'sigla': 'AM', 'região': 'Norte'}
brasil.append(estado1)
brasil.append(estado2)
brasil.append(estado3)
print(brasil)
print(brasil[0])
print(brasil[0]['UF'])
print(brasil[1]['sigla'])
print(brasil[2]['região'])

estado = {}
Brasil = []
for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    Brasil.append(estado.copy())  # OBS: não podeos usar "[:]" para copias como feito nas listas. Devemos usar ".copy()"
# Podemos apresentar das seguintes formas:
print(Brasil)
# ou:
for e in Brasil:
    print(e)
# ou:
for e in Brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
# ou:
for e in Brasil:
    for v in e.values():
        print(v, end=' ')
    print()

# Para organizar um dicionário em ordem crescente ou decrescente, usamos o módulo "operator"
"""
Por exemplo para o problema:

Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados num
dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
from random import randint
from time import sleep
from operator import itemgetter

dic = {}
for c in range(1, 5):
    dic[f'Jogador {c}'] = randint(1, 6)
print(f'{"<<< Valores Sorteados >>>":^40}')
for k, v in dic.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
lst = (sorted(dic.items(), key=itemgetter(1), reverse=True))  # criamos uma "lista" para organizar em ordem decrescente
print('==' * 20)
print(f'{"<<< Ranking dos Jogadores >>>":^40}')
for i, c in enumerate(lst):
    print(f'{i + 1}° lugar: {c[0]} com {c[1]}')
    sleep(1)
