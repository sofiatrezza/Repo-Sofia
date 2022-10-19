#numero ambicioso

def divisores(numeroin):
    divisores = []
    while True:
        for i in range(1, numeroin):
            if numeroin % i == 0:
                divisores.append(i)
            suma =sum(divisores)
        return suma

def main():
    n = int(input('Ingrese un numero entero diferente de 1: '))
    ambicioso = False

    while divisores(n) != n:
        n = divisores(n)
        if divisores(n) == n:
            ambicioso = True
            break

    if ambicioso == True:
        print('El numero es ambicioso')
    else:
        print('El numero NO es ambicioso')
        

main()

            