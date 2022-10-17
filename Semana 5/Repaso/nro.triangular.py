n = input('Ingrese un numero: ')
n = int(n) #validando que es un numero
sum = 0
for i in range(1, n): 
    if sum == n:
        print('El numero es triangular') 
        break
    elif sum > n:
        print('El numero no es triangular')
        break
    else:
        sum += i #cada vez que no se cumpla lo anterior, se suma la siguiente variable i
