#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz qadrada.

n = int(input('Digite um valor: '))
print('O dobre é {} \n O tripo é {} \n A raiz quadrada é {:.2}'.format(n*2,n*3,n**(1/2)))


#n = int(input('Digite um valor'))
#print('O dobro do valor é {}, o triplo é {}, e a raiz quadrada é {}'.format (n*2,n*3,int(n**0.5)))

# arredondar ou converter para inteiro, você está modificando o valor real da raiz quadrada. Se precisar de precisão, é melhor manter o formato float.