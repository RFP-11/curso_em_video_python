"""
Faça um programa que tenha uma função "notas()" que pode receber várias notas de alunos e vai retornar
um dicionário com as seguintes informações:
    — Quantidade de notas;
    — A maior nota;
    — A menor nota;
    — A média da turma;
    — A situação (opcional).
"""


def notas(*n, sit=False):
    """
    --> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos [aceita várias].
    :param sit: [opcional] indica a situação da turma.
    :return: dicionário com várias informações sobre a turma: quantidade de alunos, média, maior e menor nota, situação.
    """
    dados = dict()
    maior = menor = soma = 0
    dados['total'] = len(n)
    cont = 0
    for c in n:
        soma += c
        if cont == 0:
            maior = menor = c
            cont += 1
        else:
            if c > maior:
                maior = c
            if c < menor:
                menor = c
    dados['maior'] = maior
    dados['menor'] = menor
    media = round((soma / len(n)), 1)
    dados['média'] = media
    if sit:
        if media >= 9:
            dados['situação'] = 'Excelente!'
        elif 9 > media >= 7:
            dados['situação'] = 'Boa!'
        elif 7 > media >= 6:
            dados['situação'] = 'Razoável!'
        else:
            dados['situação'] = 'Ruim!'
    return dados


turma1 = notas(8.2, 9.3, 9.7, 9.1, 10, 9.5, 9.2, 10, 8.4, 9.1, 10, 9, sit=True)
print(turma1)

turma2 = notas(9.2, 6.3, 7.7, 3.1, 8, 8.5, 9.2, 10, 7.4, 4.1, 4.8, 10, sit=True)
print(turma2)

turma3 = notas(5.2, 6.3, 2.7, 3.1, 7, 8.5, 9.2, 10, 7.4, 4.1, 1.8, 9, sit=True)
print(turma3)

turma4 = notas(3.4, 4.3, 2.8, 3.1, 6, 7.5, 9.1, 9.3, 7.4, 4.1, 1.8, 9, sit=True)
print(turma4)

turma5 = notas(5.2, 6.3, 2.7, 3.1, 7, 8.5, 9.2, 10, 7.4, 4.1, 0.8, 2, sit=False)
print(turma5)

turma6 = notas(5.2, 6.3, 2.7, 3.1, 7, 6.5, 1.2, 4.1, 1.8, 3)
print(turma6)

help(notas)


# outra forma, mais rápida de fazer é usando outras funções nativas do python:
def NOTAS(*n, sit=False):
    """
    --> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos [aceita várias].
    :param sit: [opcional] indica a situação da turma.
    :return: dicionário com várias informações sobre a turma: quantidade de alunos, média, maior e menor nota, situação.
    """
    turma = dict()
    turma['Alunos'] = len(n)
    turma['Maior'] = max(n)
    turma['Menor'] = min(n)
    turma['Média'] = round(sum(n)/len(n), 1)
    if sit:
        if turma['Média'] >= 9:
            turma['situação'] = 'Excelente!'
        elif 9 > turma['Média'] >= 7:
            turma['situação'] = 'Boa!'
        elif 7 > turma['Média'] >= 6:
            turma['situação'] = 'Razoável!'
        else:
            turma['situação'] = 'Ruim!'
    return turma


turma7 = notas(8.2, 9.3, 9.7, 9.1, 7.8, 9.5, 9.2, 9.8, 8.4, 9.1, 8.7, 9, 7.2, 9.1, 5.1, sit=True)
print(turma7)
