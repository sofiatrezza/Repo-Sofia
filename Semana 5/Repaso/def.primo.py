N = input('Ingrese un numero: ')
N = int(N)

def primos(x):
    for i in range(2,x):
        if x%i == 0:
            print(f'No es primo, {i} es divisor')
            return False
    print('Es primo')     
    return True


    primos()