w = float(input('Digite a largura em metros: '))
h = float(input('Digite a altura em metros: '))
a = (w*h)
#Cada litro de tinta pinta uma área de 2m²
print('Você vai precisar de {:.2f} litros de tinta para pintar uma parede com essas medidas'.format(a/2))