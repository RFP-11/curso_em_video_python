"""
 Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""
import math

g = int(input('Digite um ângulo em graus: '))
r = math.radians(g)
print(f'\n'
      f'"{g}°" equivale a "{r} rad".\n')

print(f'sen({g}°) = {math.sin(r):.2f} \n')
print(f'cos({g}°) = {math.cos(r):.2f} \n')
print(f'tan({g}°) = {math.tan(r):.2f}')

"""
OBS: As funções trigonométricas utilizadas por padrão utilizam o radiano para fazer os calculos.
Por isso a necessidade das converções entre graus e radianos.
Uma vez que é mais comodo pedir na entrada o valor em graus, devido a facilidade pelo usuário na digitação.
"""
