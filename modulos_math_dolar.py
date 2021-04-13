#python 3.7.1

import math

dolar = 5.51
reais = float(input('Quantos reais você tem? '))
quantidadeDolar = reais / dolar

print(f'A quantidade de dólar que você vai comprar é de ${math.floor(quantidadeDolar):.2f}')




