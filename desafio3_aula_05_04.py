#python 3.7.1

houseValue = float(input('Digite o valor da casa: '))
payment = float(input('Digite o valor do salário do comprador: '))
years = int(input('Digite em quantos anos o comprador quer pagar: '))
months = years * 12
installmentValue = houseValue / months
porcent = (installmentValue * 100) / payment


if porcent < 30:
  print(f'O empréstimo foi aprovado e o valor da parcela é de R${installmentValue:.2f}')
else:
  print('O empréstimo foi reprovado, pois a parcela excede 30% do salário do comprador.')
  
