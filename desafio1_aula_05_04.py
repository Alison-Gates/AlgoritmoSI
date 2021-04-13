#python 3.7.1

nameStudent = input('Digite o nome do aluno: ')
nameMatter = input('Digite a disciplina: ')
testGrade = float(input('Digite a nota da prova: '))
workGrade = float(input('Digite a note do trabalho: '))
projectGrade = float(input('Digite a nota do projeto final: '))

average = (testGrade + workGrade + projectGrade) / 3

if average >= 7:
  print(f'O aluno {nameStudent} está APROVADO na disciplina de {nameMatter} com média {average:.2f}')
else:
  print(f'O aluno {nomeStudent} está REPROVADO na disciplina de {nameMatter} com média {average:.2f}')
  
  
  
