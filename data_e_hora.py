#python 3.7.1

import datetime

dataAtualEn = datetime.date.today()

print(f'A data no formato americano é {dataAtualEn}')

dataAtualPtBr = dataAtualEn.strftime('%d/%m/%Y')

print(f'A data no formato brasileiro é {dataAtualPtBr}')

horaAtual = datetime.datetime.now()

print(horaAtual)