n = input('Ingrese un numero: ')
n = int(n) #validando que es un numero
N = n
divisores = []
for i in range(1 , int(n/2)+1):
    if n%i == 0:
        divisores.append(i)
        print(divisores)

sum_divisores = sum(divisores)
print(sum_divisores)
if sum_divisores == N:
    print(f'El numero {N} es un numero perfecto')
elif sum_divisores != N:
    print(f'El numero {N} NO es un numero perfecto')
else:
    print('error')
