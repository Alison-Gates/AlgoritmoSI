#python 3.7.1

import random

numero = random.randint(0,5)

numeroUsuario = int(input('O computador já pensou em um número! Tente acertar ele, digite um número de 0 a 5: '))

if numeroUsuario == numero:
  print('Você acertou o número!')
else:
  print('Você errou o número... Tente novamente!')