#python 3.7.1

km = float(input('Digite a quilometragem percorrida: '))
dias = int(input('Digite a quantidade de dias alugado: '))

valorTotal = (60.00 * dias) + (0.15 * km)

print(f'O valor total a pagar é de R${valorTotal}')