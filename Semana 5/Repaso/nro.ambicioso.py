n = input('Ingrese un numero: ')
n = int(n)

divisores = []
numeros_perfectos = []
while True:
    for i in range(1, n):
        if n % i == 0:
            divisores.append(i)
        if sum(divisores) == n:
            numeros_perfectos.append(sum(divisores))
            print(f'El numero {n} es perfecto')
            print(numeros_perfectos)

        elif sum(divisores) in numeros_perfectos:
            print(f'El numero {n} es ambicioso')
        else:
            print(f'El numero {n} no es ambicioso')
    break 


