import os

os.system('cls')
num = int(input('Digite um numero: '))
os.system('cls')
while num >= 0:
    r = 1
    print('')
    while r <= 10:
        print(f'| {r:<2} + {num:<5} = {(r+num):<7} |  ', end='')
        print(f'| {r:<2} - {num:<5} = {(r-num):<7} |  ', end='')
        print(f'| {r:<2} x {num:<5} = {(r*num):<7} |  ', end='')
        print(f'| {r:<2} / {num:<5} = {(r/num):<7.0f} |')
        r = r+1
    print('\n')
    num = int(input('Digite um numero: '))
print('Fim do programa.')

