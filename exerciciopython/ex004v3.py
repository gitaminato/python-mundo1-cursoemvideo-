#Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

x = input('Digite algo: ')
print("""
  É AlphaNumérico?{}
  É Decimal? {}
  É Alpha? {}
  É um dígito? {}
  É um número?{}
  tipo: {}
  """. format(x.isalnum(), x.isdecimal(), x.isalpha(), x.isdigit(), x.isnumeric(), type(x)))

#As aspas triplas """ foram usadas para delimitar a string de múltiplas linhas no print(), permitindo uma melhor formatação do texto.

#O método .format() é uma alternativa mais antiga ao literal de string formatado (f-string) introduzido no Python 3.6.

