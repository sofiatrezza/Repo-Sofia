num =int(input("Please enter a number: "))
if num > 1:
    cont = 0 #es lo que cuenta los resultados de los modulos
    i= 2 #va a comenzar en 2
    while i<num and cont==0:
        module = num % i 
        if module == 0:
            cont += 1 #si el modulo es cero, el contador aumenta a 1 y se rompe el ciclo
    i += 1 #aumenra en uno para ir probando
if cont ==0: #i no se encuentra un numero en el que se pueda dividir, entonces:
    print(f"The number {num} is prime")
else:
    print(f"The number {num} is not prime")