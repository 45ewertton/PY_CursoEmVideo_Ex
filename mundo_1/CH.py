#Catetos e hipotenusa

from math import hypot
import math

cateto_o = float(input("Qual o valor do cateto oposto: "))
cateto_a = float(input("Qual o valor do cateto adjacente: "))

# hip = ((cateto_o**2) + (cateto_a**2))**(1/2) sem a lib

hip = math.hypot(cateto_o, cateto_a) #com  a lib

print(f'{hip:.2f}')