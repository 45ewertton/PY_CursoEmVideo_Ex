#Métodos para dissecar strings...

something = input('Digite algo: ')

print(f'O tipo primitivo de {something} é {type(something)}')
print(f'Só tem espaços? {something.isspace()}')
print(f'É um número? {something.isnumeric()}')
print(f'É alfabético? {something.isalpha()}')
print(f'É alfanumérico {something.isalnum()}')
print(f'Está em maiúsculas? {something.isupper()}')
print(f'Está em minúsculas? {something.islower()}')
print(f'Está capitalizada? {something.istitle()}')