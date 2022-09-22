"""
Escreva um programa que leia a velocidade de um carro.
    - Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
    - A multa vai custar R$7,00 por cada Km acima do limite.
"""

velocidade = float(input('Qual a velocidade atual do veículo? '))

if velocidade > 80:
    print('Multado! Você excedeu o limite de velocidade de 80 km/h.')
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar uma multa no valor de R$:{multa:.2f}')
print('Tenha um bom dia! Dirija com segurança!')
