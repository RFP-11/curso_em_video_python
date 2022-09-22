# Aulas 17 e 18
# Variáveis compostas - Listas:
"""
Como vimos, as "tuplas" são imutáveis. Agora, como veremos, as "listas" não são imutáveis.
Para "Tuplas" são usados os parênteses ();
Para as "Listas" usamos os colchetes [];
Mais a frente veremos que para os "Dicionários" usamos as chaves {};

Numa mesma "lista" pode-se atribuir tanta números/valores quanto nomes/strings, assim como nas "tuplas".

Podemos crias "listas vazias" usando "list()" ou simplesmente "[]".
"""
# Criando uma lista qualquer:
rafael = list()
Rafael = []
lst = []

# VC pode criar listas com número de elementos definidos:
exemplo = list(range(4, 11))  # Cria lista com 7 casas, cada casa com um número de 4 até 10.
print(exemplo)

# Modificando e adicionando elementos numa lista: OBS — Listas saõ mutáveis!!!
lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita']  # Exemplo de lista.
print(lanche)
lanche[3] = 'Picolé'  # As listas são mutáveis. Então o programa faz esse comando, e troca Pudim por Picolé.
lanche.append('Biscoito')  # Adiciona Biscoito no final da lista.
lanche.insert(0, 'Bolo')  # Adiciona Bolo na posição 0, e reposiciona o resto da lista.
print(lanche)

# Removendo elementos da lista, e reposicionando os demais elementos:
del lanche[3]  # Remove o que estiver na posição 3.
lanche.pop()  # Remove o último elemento da lista, e o retorna isoladamente.
lanche.pop(3)  # Remove o elemento 3 da lista.
lanche.remove('Pizza')  # No comando ".remove" vc tem que indicar qual elemento vc quer remover da lista.

if 'Espaguete' in lanche:
    lanche.remove('Espaguete')
# Usando o comando "if", vc consegue verificar se tem o elemento que vc quer remover na lista, e então poder remove-lo.
# Caso não use o "if", e o elemento não esteja na lista, vai dar erro. Por isso, usa-se o "if".

num = [2, 5, 9, 1, 8, 7, 1, 3, 0, 4, 6]  # Exemplo de uma lista.
print(num)

print(len(num))  # Mostra quantos elementos tem na lista num.

num[2] = 7  # Altera para 7 o número da posição 2.
print(num)

num.append(3)  # Adiciona o número 3 no final da lista.
print(num)

num.sort()  # Coloca a Lista em ordem crescente.
print(num)

num.sort(reverse=True)  # Coloca a Lista em ordem decrescente.
print(num)

num.insert(2, 0)  # Incere o valor 0 na posição 2. E refaz a lista jogando os outros elementos pra frente.
print(num)

num.pop(2)  # remove o numero 2 da Lista. Se não tiver o número que vc pede pra remover dá um erro..
print(num)

# para contornar o erro que pode dar como o comando pop vc pode fazer:
if 4 in num:
    num.remove(4)  # Se tiver o número 4 na lista ele será removido.
else:
    print('Não achei nenhum número 4 para remover.')

# Adicionar valores nas listas e saber as posições:
valores = []  # Cria uma lista vazia.
valores.append(5)  # Adiciona o valor 5 na lista.
valores.append(9)  # Adiciona o valor 9 no final da lista.
valores.append(4)  # Adiciona o valor 4 no final da lista.
print(valores)

for v in valores:
    print(v)  # Vai mostrar cada elemento da lista valores.

for c, v in enumerate(valores):  # vai contar com c cada posição.
    print(f'Na posição {c} encontrei o valor {v}.')
print('Cheguei ao final da lista.')

# Para criar uma lista pedindo entrada ao usuário:
entrada = list()
for cont in range(0, 5):
    entrada.append(int(input('Digite um valor: ')))
print(f'A lista criada foi: {entrada}.')

# Ligação entre listas:
a = [2, 3, 4, 7]
b = a
b[2] = 8  # a e b estão ligadas. Qualquer mudança em uma reflete na outra.
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# Cópia entre listas:
a = [2, 3, 4, 7]
b = a[:]  # A lista b recebe todos os itens da lista a.
b[2] = 8  # a e b não estão mais ligadas, b é uma cópia de a.
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# É possível alterar os estilos dentro das listas, por exemplo de str para float ou para int ou vice-verso:
import math as ma

cont = ['6.563e-19', '8.204e-19', '11.50e-19', '13.13e-19', '16.48e-19', '18.08e-19', '19.71e-19', '22.89e-19',
        '26.13e-19']

lst = []
for c in range(0, len(cont)):
    lst.append(float(cont[c]))
# Atribui para dentro de lst cada elemento da lista cont transformado de string para um número flutuante.
print(lst, '\n')
print(f'A soma da lista acima é: {ma.fsum(lst)} \n')

x = cont[:]  # X recebe uma cópia da lista cont.
x[0] = str('Vamos Alterar Elementos da Lista')
x[1] = float(2.45)
x[2] = str('Olá Mundo!')
x[6] = int(234)
print(x)

'''Listas Compostas'''
# Listas compostas = (Listas dentro de outra lista):
dados1 = list()
dados1.append('João')
dados1.append(25)
dados2 = list()
dados2.append('Maria')
dados2.append(19)
dados3 = list()
dados3.append('Pedro')
dados3.append(32)

pessoas = list()
pessoas.append(dados1[:])  # [:] indica fazer uma cópia de dados1
pessoas.append(dados2[:])  # [:] indica fazer uma cópia de dados2
pessoas.append(dados3[:])  # [:] indica fazer uma cópia de dados3
print(pessoas)

# ou ainda:
pessoas = [['João', 25], ['Maria', 19], ['Pedro', 32]]
print(pessoas)
print(pessoas[0][0])  # mostra o 1º item da 1ª lista: João;
print(pessoas[1][1])  # mostra o 2º item da 2º lista: 19;
print(pessoas[2][0])  # mostra o 1º item da 3ª lista: Pedro;
print(pessoas[1])  # mostra a 2ª lista inteira: ['Maria', 19];

# Alguns outros exemplos:
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])  # Lembre: [:] faz uma cópia da lista especificada.
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 45], ['Maria', 23]]
print(galera[0])  # Mostra ['João', 19]
print(galera[2][1])  # Mostra 45
print(galera[3][0])  # Mostra 'Maria'
print(galera[1][1])  # Mostra 33
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

galera = list()
dado = list()
totmaior = totmenor = 0
for c in range(0, 5):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()
print(galera)

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade.')
