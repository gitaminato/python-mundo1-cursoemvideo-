n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1+n2
m = n1*n2
d = n1/ n2
di = n1//n2
e = n1**n2
print('A soma é {}, \n o produto é {}, \n a divisão é {:.3}'.format(s,m,d), end=' ')
print('\n A divisão inteira é {},\n a Exponenciação é {}'.format(di, e))