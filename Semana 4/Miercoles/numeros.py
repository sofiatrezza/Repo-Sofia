'''Se propone que se implemente un algoritmo que, dado un número introducido por el usuario*,
diga si ese número es primo de Fermat.
Definiciones:
 Número de Fermat: todo número natural de la forma (2^(2^n)) + 1 para algún n. Si ese
número resulta ser primo, se denomina primo de Fermat.

*debe validarse que el input sea un número natural.'''


n = input('Por favor ingrese un numero: ')
n = int(n)

for i in range(0, n):
    if n == (2**2**i + 1):
        print(f'El numero {n} es un numero primo Fermat')
        break
else:
    print(f'El numero {n} NO es un numero primo Fermat')
