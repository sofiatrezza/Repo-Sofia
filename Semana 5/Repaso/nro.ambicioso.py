'''def suma (numusuario):
        listnum=[]
        for num in range (1,numusuario):
            divisor= numusuario%num
            if divisor==0:
                listnum.append(num)
        total= sum(listnum)
        return total
def es_perfecto(numusuario):
        return suma(numusuario)==numusuario
def main():
    numusuario= int(input('ingrese un numero entero positivo: '))
    
    esambicioso= False

    while not es_perfecto(numusuario) and numusuario != 1:
        numusuario=suma(numusuario)
        if es_perfecto(numusuario):
            esambicioso = True
            break

    if esambicioso == True:
        print ('el numero ingresado es ambicioso')
    else:
        print ('el numero ingresado no es ambicioso')
main ()'''

n = input('Ingrese un numero: ')
n = int(n)

def numero_perfecto(numeroin):
    divisores = []
    while True:
        for i in range(1, numeroin):
            if n % i == 0:
                divisores.append(i)
            if sum(divisores) == n:
                print(f'El numero {numeroin} es perfecto')
            
    

    
            


