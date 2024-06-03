import math
import time
n1 = int(input('Qual número inteiro deseja calcular o seu fatorial? '))
c = n1
fatorial = math.factorial(n1)
print('Calculando a fatorial de {}....'.format(n1))
time.sleep(2)
while c > 0:
    print('{} '.format(c), end='')
    print('x ' if c > 1 else ' = ', end='')
    c -= 1
print(fatorial, end='')
