"""
Faça um programa em python que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.
"""
import math

CO = float(input('Digite o valor numérico do cateto oposto: '))
CA = float(input('Digite o valor numérico do cateto adjacente: '))
hip1 = (CA**2 + CO**2) ** (1/2)
hip2 = math.sqrt(CA**2 + CO**2)

print(f'\n'
      f'A hipotenusa da triângulo retangulo vale: {hip1:.2f}\n')
print(f'A hipotenusa do triângulo retangulo vale: {hip2:.2f}\n')
print(f'A hipotenusa do triângulo retangura vale: {math.hypot(CO,CA):.2f}')

# OBS: analise as diferentes formas de apresentar o resultado.
