# Aulas 20 e 21
# Funções em Python:
"""
Função está atrelada a palavra "ROTINA". Usamos funções sempre que precisamos repetir várias vezes um mesmo comando.
    Exemplos de funções internas/nativas do python que utilizamos sempre até aqui:
        - print(); len();  input(); int(); float(); ...

Agora podemos ainda construir as nossas próprias funções. Como veremos nesta aula.

Para criar-se uma função é preciso defini-la da seguinte forma: " def NomeDaFunção(): ".

Por questão de estética/organização no código, as funções ficam separadas por duas linhas do restante do código;
Assim, fica interesante dividirmos o código em duas partes:
    - Onde criamos as funções = cabeçalho do código;
    - Programa principal = corpo do código.

Funções de ajuda:
    - help() - você terá acesso e uma explicação detalhada do que for especificado entre parênteses.
        Exemplo: help(print) - irá aparecer o que o "print" faz.
    - docstrings - é uma funcionalidade que o usuário pode usar para especificar-se detalhes sobre a função definada.

Algo muito importante sobre as funções é o conceito de "variável local" e o de "variável global":
    - Uma "variável local" fica confinada apenas dentro da função criada, não pode ser chamada no programa principal;
    - Uma "variável global" é aquela declarada no programa principal e pode ser chamada em qualquer lugar do código.
"""


# Criando uma função linha que escreve uma linha com 30 traços:
def linha():
    print('-' * 30)


# Programa principal
linha()
print(f'{"Curso em Vídeo":^30}')  # Nome centralizado dentro de 30 caracteres.
linha()
print(f'{"Rafael":^30}')  # Nome centralizado dentro de 30 caracteres.
linha()


# Exemplo de uma "docstrings":
def contador(i=0, f=0, p=0):
    """
    --> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='')
        c += p
    print('Fim!')


# Usando o "help" quando utilizou-se uma "docstrings" para especificar detalhes do funcionamento da função:
# Assim, podemos entender o uso para os dois tipos: "help" e "docstrings".
help(contador)


# Criando uma função mensagem para escrita personalizada:
def mensagem(msg):
    print('-' * 30)
    print(f'{msg:^30}')
    print('-' * 30)


# programa principal
mensagem('Olá Mundo!')
mensagem('Rafael, vai estudar!')
mensagem('Curso em Vídeo')


"""
Parametros opcionais:
    - é quando atribuimos valor aos parâmetros das funções para evitar erro caso não sejam informados pelo usuário.
Exemplo: Criando função soma usando parâmetros opcionais: a=0 e b=0:
"""
def soma(a=0, b=0):
    s = a + b
    print(s)


# programa principal
soma(4, 5)
soma(2, 9)
soma(20, 89)


# Criando função que desempacota qualquer sequência de números:
# O uso do "*" dentro do nome da função é para indicar o desempacotamento.
def contador(*v):
    for valor in v:
        print(f'{valor}, ', end='')
    print('Fim!')


# Criando função que lê e conta qualquer sequência de números:
def cont(*t):
    tamanho = len(t)
    print(f'Recebi os valores {t} e são ao todo {tamanho} números.')


# Criando uma função soma com desempacotamento:
def soma(*valor):
    s = 0
    for numero in valor:
        s += numero
    print(f'Somando os valores {valor} temos: {s}')


# programa principal
contador(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
contador(23, 45, 67)
contador(12, 34, 54, 87)

cont(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
cont(23, 45, 67)
cont(12, 34, 54, 87)

soma(4, 5)
soma(2, 9)
soma(20, 89)


# Criando funções usando listas:
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [0, 3, 34, 65, 98, 109, 34, 72, 87]
dobra(valores)
print(valores)

"""
Podemos utilizar o "return" dentro a função criada para que seja retornado "algo" para o programa principal.
"""
# função para calcular o fatorial.
def fatorial(r=1):
    f = 1
    for c in range(r, 0, -1):
        f *= c
    return f


# programa principal
print('Este programa calcula o fatorial de um úmero.')
n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'O fatorial de 5, 4 e 0, respectivamente, são: {f1}, {f2} e {f3}')


# Função para saber se número é par ou impar:
def par(c=0):
    if c % 2 == 0:
        return True
    else:
        return False


# programa principal
num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')


# Criando uma função soma com retorno e com parâmetro opcional para não dar erro se não for informado a, b e c.
def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


# programa principal
print(soma(4, 5))
print(soma(2, 9, 3))
print(soma(c=20, a=89))
n1 = soma(3, 9, 15)
n2 = soma(2, 3)
print(f'Os resulatdos das somas foram {n1} e {n2}')
