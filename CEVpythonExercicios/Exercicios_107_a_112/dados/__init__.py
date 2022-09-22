def leiaInt(msg='Digite um valor: '):
    while True:
        num = input(msg)
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')  # Vermelho: \033[0;31m"Mensagem"\033[m
    return num


def leiaDinheiro(msg='Digite um valor: '):
    while True:
        entrada = str(input(msg)).strip().replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: "{entrada}" é um valor válido!\033[m')  # Vermelho: \033[0;31m"Mensagem"\033[m
        else:
            break
    return float(entrada)
