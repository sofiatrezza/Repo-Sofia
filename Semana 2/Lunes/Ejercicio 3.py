numerador= float(input("Please enter yhe first number: "))
denominador = float(input("Please enter another number: "))
is_valid= True

if numerador. isnumeric():
    numerador = float(numerador)
else:
    is_valid = False

if denominador. isnumeric():
    if denominador == 0:
        print("Error")
else:
    print(numerador/denominador)

