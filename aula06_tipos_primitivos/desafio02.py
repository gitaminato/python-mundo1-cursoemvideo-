#Crie um programa que leia dois números e mostre a soma entre eles.
a = input('Digite algo: ')
print(type(a))
print('ele é um número?', a.isnumeric())
      
print('ele é um uma letra e número?', a.isalnum())
print('ele é uma letra?', a.isalpha())
print('ele é um decimal?', a.isdecimal())
print('ele é um dígito?', a.isdigit())
print('ele é um identificador?', a.isidentifier())
print('ele está em caixa baixa?', a.islower())
print('ele é printable?', a.isprintable())
print('ele é um espaço?', a.isspace())

