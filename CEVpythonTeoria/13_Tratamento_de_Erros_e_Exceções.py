# Aula 23
# Tratamento de erros e exceções em python:
"""
Para tratar erros e exceções usamos o comando "try" == "tente fazer isso".
Caso ocorra um erro ou exceção então é executado o "except".
Os comandos "else" e "finally" são opcionais. Mas se utilizado, "finally" sempre será executado.
"""
# Forma mais simples:
try:
    a = int(input('Digite o numerador: '))
    b = int(input('Digite o denominador: '))
    d = a / b
except:
    print('Infelismente tivemos um problema :(')
else:
    print(f'O resuntado da divisão de {a} por {b} é {d}')
finally:
    print('Muito obrigado! Volte sempre.')

# Especificando a classe do erro:
try:
    a = int(input('Digite o numerador: '))
    b = int(input('Digite o denominador: '))
    d = a / b
except Exception as erro:
    print(f'O problema encontrado foi {erro.__class__}')
else:
    print(f'O resuntado da divisão de {a} por {b} é {d}')
finally:
    print('Muito obrigado! Volte sempre.')

# Personalisando os tipos de erro:
try:
    a = int(input('Digite o numerador: '))
    b = int(input('Digite o denominador: '))
    d = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resuntado da divisão de {a} por {b} é {d}')
finally:
    print('Muito obrigado! Volte sempre.')
