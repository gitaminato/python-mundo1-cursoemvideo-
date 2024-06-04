#Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

x = input('Digite algo: ')
print(f"""
  É AlphaNumérico? {x.isalnum()}
  É Decimal? {x.isdecimal()}
  É Alpha? {x.isalpha()}
  É um dígito? {x.isdigit()}
  É um número?{x.isnumeric()}
  tipo: {type(x)}
  """)

#As aspas triplas """ foram usadas para delimitar a string de múltiplas linhas no print(), permitindo uma melhor formatação do texto.