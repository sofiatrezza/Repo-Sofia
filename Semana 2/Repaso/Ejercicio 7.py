weight = (input("Please enter how much you weight in kg "))
height = (input("Please enter your height in meters "))
imc = round(float(weight)/float(height)**2)
print(f"Your imc is {imc}")
