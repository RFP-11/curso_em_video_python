"""
Faça um programa que tenha uma função chamada "escreva()", que receba um texto qualquer como parâmetro e mostre
uma mensagem com tamanho adaptável.
Ex: escreva(‘Olá, Mundo!’)
    Saída:
            ~~~~~~~~~~~
            Olá, Mundo!
            ~~~~~~~~~~~
"""


def escreva(msg):
    print('-' * (len(msg) + 4))
    print(f'  {msg}')
    print('-' * (len(msg) + 4))


escreva('Olá mundo!')
escreva('Rafael Filgueira Pimentel')
escreva('Aprendendo python')
escreva('Bom dia!')
escreva('========\n  Sua vez!\n  ========')
escreva(str(input('Entre com um título: ')))
