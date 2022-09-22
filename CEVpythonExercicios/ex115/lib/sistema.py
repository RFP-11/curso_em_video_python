from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'MeuPrimeiroProjeto.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabecalho('Novo cadastro')
        nome = str(input('Nome: ')).strip().title()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema. Volte sempre!')
        break
    else:
        print('\033[0;31mErro! Digite uma opção válida.\033[m')
    # sleep(2)
