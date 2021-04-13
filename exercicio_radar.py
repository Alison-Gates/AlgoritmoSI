#python 3.7.1

import random

velocidadeCarro = random.randrange(60,120,10)

if velocidadeCarro > 80:
  multa = (velocidadeCarro - 80) * 7
  print('Você foi multado!')
  print(f'O valor da multa foi de R${multa:.2f}')
else:
  print('Velocidade OK!')

