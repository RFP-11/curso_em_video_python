# Crie um script em python que leia algo pelo teclado e,
# mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

d = input('Digite algo: ')
print(f'"{d}" tem seu tipo primitivo sendo: {type(d)}')
print(f'"{d}" é um número? {d.isnumeric()}')
print(f'"{d}" é Alfa numérico? {d.isalnum()}')
print(f'"{d}" é alfabético? {d.isalpha()}')
print(f'"{d}" tem todos os caracteres sendo ASCII? {d.isascii()}')
print(f'"{d}" é um decimal? {d.isdecimal()}')
print(f'"{d}" é apenas digito? {d.isdigit()}')
print(f'"{d}" é valido para escrever um identificador? {d.isidentifier()}')
print(f'"{d}" pode ser impresso? {d.isprintable()}')
print(f'"{d}" é um espaço? {d.isspace()}')
print(f'"{d}" começa com letra maiuscula ou é capitalizado? {d.istitle()}')
print(f'"{d}" está em maiusculo? {d.isupper()}')
print(f'"{d}" está em minusculo? {d.islower()}')
