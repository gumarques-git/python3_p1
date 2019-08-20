# -*- coding: UTF-8 -*-

print('Brasil', 'ganhou', 5, 'Mundiais', sep='-', end='\n')

print('Brasil', 'ganhou', 5, 'Mundiais', end='')

print('Brasil', 'ganhou', 5, 'Mundiais', sep='-', end='!\n')

# Python nao faz conversao automatica.
# Multiplicar 10 x "20" ele faz algo chamado syntax sugar
# Q eh imprimir 10x o texto "20"

numero1 = 10
numero2 = "20"
produto = numero1 * numero2
print(produto)