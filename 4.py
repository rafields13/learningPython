# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre ele.

x = input('Digite algo, por favor: ')
print(f'O tipo primitivo desse valor é: {type(x)}.')
print(f'É um valor alfanumérico? {x.isalnum()}.')
print(f'É um valor alfabético? {x.isalpha()}.')
print(f'É um valor da tabela ascii? {x.isascii()}.')
print(f'Esse valor é um dígito? {x.isdigit()}.')
print(f'Esse valor está escrito somente em letras minúsculas? {x.islower()}.')
print(f'É um valor decimal? {x.isdecimal()}.')
print(f'Esse valor é identificável? {x.isidentifier()}.')
print(f'É um valor numérico? {x.isnumeric()}.')
print(f'Esse valor é "printável"? {x.isprintable()}.')
print(f'Esse valor só possui espaços? {x.isspace()}.')
print(f'Esse valor está capitalizado? {x.istitle()}.')
print(f'Esse valor está escrito somente em letras maiúsculas? {x.isupper()}.')
