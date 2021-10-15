#Seno, cosseno e tangente

from math import radians, sin, cos, tan

ang = float(input('Qual o ângulo desejado? '))

seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))

print(f'O ângulo é {ang} e seu seno, cosseno e tangente são: seno {seno:.2f}, cosseno {cosseno:.2f} e tangente {tangente:.2f}')