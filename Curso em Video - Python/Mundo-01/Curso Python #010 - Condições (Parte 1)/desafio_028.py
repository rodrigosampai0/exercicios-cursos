# Escreva um programa que faça o computador "pençar" em um número inteiro entre 0 e 5
    # e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
        # * O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

numero = int(input('Digite um número de 1 a 5: '))
rep = randint(1, 5)
if rep == numero:
    print('Você acertou!')
else:
    print('Você errou!')
