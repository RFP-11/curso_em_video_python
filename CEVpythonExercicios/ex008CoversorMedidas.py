# Escreva um script em python que leia um valor em metros e o exiba convertindo em centimetros e milimetros.

n = float(input('Digite a metragem em métros de uma dimenção: '))
print(f'\n'
      f'{n} metros são {n*(10 ** 2)} centimetros.\n')
print(f'{n} metros são {n*(10 ** 3)} milimetros.')
