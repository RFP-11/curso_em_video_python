# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

C = float(input('Digite a temperatura em °C: '))
print(f'\n'
      f'A temperatura de {C} °C em Fahrenheit corresponde a: {(9*C/5)+32} °F\n')
print(f'A temperatura de {C} °C em Kelvin corresponde a: {C+273.15} K.')
