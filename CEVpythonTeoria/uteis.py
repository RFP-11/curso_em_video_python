# Aprendendo sobre — Modularização:
# Arquivo criado para armazenar funções que criamos na aula 22, que não são nativas do python.

def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f


def dobro(n):
    return n * 2


def triplo(n):
    return n * 3
