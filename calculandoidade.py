from datetime import date
anoa = date.today().year
p = int(input('Digite seu ano de nascimento: '))
idade = anoa - p

print(f'Você tem {idade} anos de idade')
