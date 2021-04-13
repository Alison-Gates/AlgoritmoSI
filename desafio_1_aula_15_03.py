#python 3.7.1

largura = float(input('Digite a largura da parede em metros: ' ))
altura = float(input('Digite a altura da parede em metros: ' ))
areaParede = largura * altura
coberturaTinta = 2
quantidadeLitros = areaParede / 2

print(f'\nA área total da parede é de {areaParede}m²')
print(f'\nA quantidade de litros de tinta que você precisa para pintar é {quantidadeLitros}')


