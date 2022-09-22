# Aula 22
# Módulos e Pacotes:
"""
Modularização: é a capacidade de construir módulos. Tem como foco dividir um programa grande em várias partes.
Com a modularização, aumenta-se a legibilidade do código e facilita-se a sua manutenção.

Até aqui quando criavamos uma função, colocavamos ela no início do código.
Mas se tivermos que criar muitas funções fai ficar muito grande e poluido o nosso código, nada simples né...
Daí a ideia da modularização — Colocar todas as funções num "arquivo.py" separado, para apenas chamar quando necessário.
E para chamar a função fazemos da mesma forma que chamamos as funções nativas do python.
Ou seja, simplesmente usamos: "import arquivoX", ou, "from arquivoX import funçãoX, funçãoY".
Daí chama-se: "arquivoX.funçãoX()", ou, "funçãoX()", ou, "funçãoY()", se usado o "from".



Pacotes: é quando agrupamos vários módulos numa pasta, ou ainda, vária pastas de módulos dentro de outra pasta.
OBS: o arquivo na pasta deve ser chamadado "__init__.py" impreterivelmente.
E para chamar o pacote fazemos da mesma forma que chamamos os pacotes nativas do python.
Ou seja, simplesmente usamos: "from pacoteX import moduloX".
Daí chama-se: "moduloX.funçãoX()"

"""

# Exemplo usando modularização:
# Criamos o arquivo "uteis.py" para as armazemar as funções criadas:
import uteis  # Agora importando o arquivo criado com as funções, simplificamos muito o nosso código.

num = int(input('Digite um número inteiro: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {uteis.dobro(num)}')
print(f'O triplo de {num} é {uteis.triplo(num)}')


# Exemplo usando Pacotes:
from utilidades import numeros  # Criamos um pacote chamado "utilidades" contendo as pastas: numeros, strings e cores.
# Cada uma das pastas no pacote "utilidades" possui um arquivo "__init__.py" onde podem ser armazenadas as funções.

num = int(input('Digite um número inteiro: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
print(f'O triplo de {num} é {numeros.triplo(num)}')

# A vantagem de utilizar os pacotes é para melhor organização dos módulos criados.
