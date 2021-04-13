#python 3.7.1
import datetime

anoNascimento = int(input('Em qual ano você nasceu? '))
anoAtual = datetime.date.today().year

idade = anoAtual - anoNascimento

print(f'A sua idade é {idade}')
