from emoji import emojize
from math import sqrt
def linha():
    print('-=-' * 14)

linha()
print('\033[34m Informações de Números!!\033[m')
print('-=-' * 14)
n=int(input(' Digite um número para sua tabuada: '))
limite_n = int(input(' Limite da Tabuada : '))

raiz= sqrt(n)
linha()
print(f' Sua raiz é {raiz}')

print(emojize(' Sua tabuada é :pencil:' , use_aliases= True))    
linha()
for c in range(1, limite_n + 1):
    print(' {} x {:2} = {:2}'.format (n, c, n * c))
linha()

u = n //  1 %  10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(emojize(' analizando o número {}...:mag_right: '.format(n), use_aliases = True))
print( ' Sua unidade é {}'.format(u))
print(' Sua dezena é {}'.format(d))
print(' Sua centena é {}'.format(c))
print(' Seu milhar é {}'.format(m))
linha()

res = n % 2 
if res == 0:
    print(' O numero {} é PAR'.format(n))
else:
    print(' O numero {} é IMPAR'.format(n))