"""
Faça um programa que leia a largura e altura de uma parede em métros.
Depois, calcula sua área e a quantidade de tinta necessária para pinta-lá.

OBS: sabendo-se que cada litro de tinta pinta uma área de 2 m^2.
"""

a = float(input('Digita a metragem em métros da altura: '))
L = float(input('Digite a metragem em métros da largura: '))
A = a * L
print(f'\n'
      f'A área da parede é: {A} m^2\n')
print(f'Serão necessários {A / 2} litros de tinta para a pintura da parede.')
