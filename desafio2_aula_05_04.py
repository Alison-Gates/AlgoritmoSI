#python 3.7.1

numberOne = float(input('Digite o primeiro número: '))
numberTwo = float(input('Digite o segundo número: '))
numberThree = float(input('Digite o terceiro número: '))


if numberTwo > numberOne:
  higherNumber = numberTwo
if numberThree > numberTwo:
  higherNumber = numberThree
else:
  higherNumber = numberOne

print(f'O maior número digitado foi {higherNumber}')

if numberTwo < numberOne:
  smallestNumber = numberTwo
if numberThree < numberTwo:
  smallestNumber = numberThree
else:
  smallestNumber = numberOne
  
print(f'O menor número digitado foi {smallestNumber}')
