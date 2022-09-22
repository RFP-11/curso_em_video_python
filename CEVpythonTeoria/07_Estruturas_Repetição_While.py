# Aula 14 e 15
# Estrutura de repetição com teste lógico — while (do inglês: enquanto, durante):
"""
Estrutura de controle.
Laços de repetições.
Estrutura "while"  =>  while condição:

Dentro do "while" precisamos apenas indicar uma condição, que enquanto verdadeira permanece no laço.
"""

# Semelhança com o comando "for":
# Quando SE SABE o intervalo de repetições podemos usar o "for" ou "while", ambos retornam o mesmo resultado.
# Porém, quando NÃO SE SABE o intervalo de repetições não é possível usar o comanando "for", mas sim o "while".
for c in range(0, 10):
    print(c)
print('Fim!')

c = 0
while c < 10:
    print(c)
    c += 1
print('Fim!')

cont = 1
while cont <= 10:
    print(cont, '-->', end='')
    cont += 1
print('Acabou')

# O comando "while" fornece novas possibilidades de utilização que o comando "for" não possíbilita.
# Uma delas é a possíbilidade de fazer repetições com limites desconhecidos.
print('Digite 0 para parar.')
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim!')

print('Testando com string.')
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
print('Fim!')

sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]  # comandos: sem espaços, maiúsculo, só a 1ª letra.
while sexo not in 'MmFf':
    sexo = str(input('Dado inválido! Por favor, informe o sexo [M/F]: ')).strip().upper()[0]
print(f'Sexo {sexo} informado com sucesso.')

# Exemplo mais elaborado.
print('Digite 0 para terminar.')
n = 1
par = impar = 0
while n != 0:
    n = int(input("Digite um valor: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares!')

# O comando "break" usado dentro de um laço de repetição é usado para interromper apenas esse laço.
# Para criar um loop infinito use "True" no comando "while".
print("Calcula um somatório. Digite 999 para interromper.")
n = s = 0
while True:
    n = int(input("Digite um valor: "))
    if n == 999:
        break
    s += n
print(f'A soma dos números é igual a: {s}')
