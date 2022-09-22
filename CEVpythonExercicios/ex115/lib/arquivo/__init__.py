from ex115.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[31mHouve um ERRO na criação do arquivo!\033[m')
    else:
        print(f'O arquivo {nome} foi criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mErro ao ler o Arquivo.\033[m')
    else:
        cabecalho('Pessoas cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mHouve um ERRO na abertura do arquivo.\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mHouve um ERRO na hora de escrever os dados.\033[m')
        else:
            print(f'Novo registro de {nome} adicionado!')
            a.close()
