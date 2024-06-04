#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um valor: '))
print(f"""
  O dobro de {n} é igual a {n*2}
  O triplo de {n} é igual a {n*3}
  A raiz quadrada de {n} é igual a {pow(n,(1/2)):.4}
  """)