#Utilizando o método trunc() da lib math para pegar apenas a parte inteira de um número

from math import trunc

num = float(input("Digite um número: "))

new_num = trunc(num)

print(f'O número digitado foi {num} e sua parte inteira é {new_num}')