#Hacer un programa en PseInt que lea un número entero positivo, a fin de
# determinar si el número pertenece a la serie Fibonacci. El programa deberá
# desplegar en pantalla, un mensaje indicando si el número pertenece o no a la
# serie. El programa debe preguntar si el usuario desea volver a verificar con otro
# número.

numero = input('Ingrese un numero: ')
numero = int(numero)
if numero == 0:
    print(f'El numero {numero} pertenece a la sucesion de Fibonacci')
elif numero == 1:
    print(f'El numero {numero} pertenece a la sucesion de Fibonacci')

def fibonacci(x):
    sucesion = [0,1]
    while sucesion[-1]<x:
        sucesion.append(sucesion[-1]+sucesion[-2])
    return(sucesion)

fibo = fibonacci(numero)
print(fibo)
if numero in fibo:
    print(f'El numero {numero} pertenece a la sucesion de Fibonacci')
else:
    print(f'El numero {numero} no pertenece a la sucesion de Fibonacci')



