from math import radians, cos, sin, tan
ang = float(input('Digite um ângulo qualquer:'))
rad = radians(ang)
print(f'O seno de {ang:.0f} é {sin(rad):.2f}, seu cosseno é {cos(rad):.2f}',end=' ')
print(f'e sua tangente é {tan(rad):.2f}')
