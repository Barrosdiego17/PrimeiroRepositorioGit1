T = int(input('Qual tabuada você deseja? '))
L = int(input('Até que número sua tabuada finalizará? '))
for c in range(0, L, T):
    print('..', end='')
    print(c, end=' ')
