#Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

d = float(input('Uma distância em metros: '))
print(f"""
  A medida de {d}m corresponde a
  {d/pow(10,3)}km
  {d/pow(10,2)}hm
  {d/10}dam
  {d*10:.0f}dm
  {d*pow(10,2):.0f}cm
  {d*pow(10,3):.0f}mm
  """)
