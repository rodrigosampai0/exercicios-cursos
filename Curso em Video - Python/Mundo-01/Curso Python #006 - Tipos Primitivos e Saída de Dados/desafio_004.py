# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
    # primitivo e todas as informações possíveis sobre ele.

from funcoes import limpa, title, result

limpa()
title()
info = input('Escreva algo: ')
limpa()
result()
print(f'Você digitou "{info}" e seu tipo primitivo é: {type(info)}\n')
print(f'- É um valor numerico? {info.isnumeric()}')
print(f'- É um valor alfabetico? {info.isalpha()}')
print(f'- É um valor alfanumerico? {info.isalnum()}')
print(f'- Esta em forma decimal? {info.isdecimal()}')
print(f'- Esta em maiúsculo? {info.isupper()}')
print(f'- Esta em minúscula? {info.islower()}')
print(f'- Esta captalizada? {info.istitle()}')
print(f'- É somete espaço? {info.isspace()}\n')
