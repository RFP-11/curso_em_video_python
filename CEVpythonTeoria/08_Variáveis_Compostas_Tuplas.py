# Aula 16
# Variáveis compostas - Tuplas:
"""
OBS: Tuplas são imutáveis dentro do programa.
Para mudar uma tupla vc deve alterar manualmente no programa e salvar novamente.
Uma mesma tupla aceita tanto numeros quanto nomes ou qualquer tipo de "string".
"""

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')  # = (0, 1, 2, 3, 4) ou = (-5, -4, -3, -2, -1)
print(lanche)  # mostra a tupla inteira
print(lanche[1])  # mostra o elemento 1 dentro da tupla: no caso mostra "Suco"
print(lanche[0])  # mostra o elemento 0 dentro da tupla: no caso mostra "Hamburguer"
print(lanche[:2])  # mostra do elemento 0 até 1: "Hambusguer" e "suco"
print(lanche[1:])  # mostra do elemento 1 até o final da tupla
print(lanche[-1])  # o sinal de menos indica começar de trás para frente. Assim, mostra o elemento 4
print(lanche[-2:])  # começa de trás para frente, mostra do elemento -2 até terminar a tupla
print(lanche[:-1])  # mostra do início da tupla até o final, mas não mostra o último termo
print(lanche[:4])  # mostra o mesmo que o comando anterior.
print(lanche[1:3])  # mostra do elemento 1 até o 2: "Suco" e "Pizza"

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi muito!')

for comida in lanche:  # Podemos usar for sem o range dessa forma nas tuplas!
    print(f'Eu vou comer {comida}')
print('Comi muito!')

# Se precisar que apareça a posição dos elementos pode fazer:
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi muito!')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi muito!')

# Para ordenar uma tupla vc pode usar o comando sorted():
print(lanche)
print(sorted(lanche))

# Somar tuplas significa juntar ela numa terceira tupla:
a = (2, 5, 4)
b = (5, 8, 1, 3)
c = a + b  # teremos c = (2, 5, 4, 5, 8, 1, 3)
d = b + a  # teremos d = (5, 8, 1, 3, 2, 5, 4)
print(c)
print(d)
print(len(c))
print(c.count(5))  # Conta quantas vezes aparece o número 5 na tupla c.
print(c.index(8))  # Mostra qual a posição do número 8 na tupla c.
print(c.index(5, 1))  # Mostra a qual a posição do número 5 a partir da posição 1 na tupla c.

# Uma tupla aceita tanto "strings" quanto "numerais".
pessoa = ('Rafael', 25, 'M', 75, 'Brasileiro')
print(pessoa)

# Uma tupla é imutável no programa. Mas vc pode apagar ela toda no programa.
pessoa = ('Rafael', 25, 'M', 75, 'Brasileiro')
del pessoa
print(pessoa)  # Vai dar um erro ao rodar esse print pois a tupla pessoa foi apagada no comando anterior.
