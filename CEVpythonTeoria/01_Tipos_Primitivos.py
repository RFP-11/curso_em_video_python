# Aula 06.
# Tipos primitivos:
"""
int     nº. inteiro. Ex.: 1, 5, 4823, -1, -23;
float   nº. real - "flutuante". Ex.: 1.0, 2.3, 0.001;
bool    booleano. Ex.: True, False;
str     string. Ex.: 'Olá', '123', '3a', '-12';
"""

n1 = int(input('Digite um priemiro valor: '))
n2 = int(input('Digite um Segundo valor: '))
s = n1 + n2
print(f'A soma entre "{n1}" e "{n2}" é: {s}')

print('\n'
      'Hora de um pouco de teoria. \n')

a = input('Digite algo: ')
# print(a, 'é um', type(a))
print(f'"{a}" é um {type(a)}')

b = int(input('Digite um número inteiro: '))
# print(b, 'é um', type(b))
print(f'"{b}" é um {type(b)}')

c = float(input('Digite um número real: '))
# print(c, 'é um', type(c))
print(f'"{c}" é um {type(c)}')

d = bool(input('Digite algo: '))
# print(d, 'é um', type(d))
print(f'"{d}" é um {type(d)}')

e = str(input('Digite algo: '))
# print(e, 'é um', type(e))
print(f'"{e}" é um {type(e)}')

# OBS: veja que fornecendo ou não o comando "str" o python lida o "input" como uma string.
# O que não acontece para os outros comando. Então se não especificar, por padrão será uma "str", até numeros.
