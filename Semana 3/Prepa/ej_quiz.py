password_list = []
while True:
    password = input("Please enter a password: ")
    if len(password) <8:
        print(f"It should have more than 8 characters")
    if password.isalnum() == False: #isalnum() chequea si hay numeros y caracteres especiales
            print(f"It should have at least one number and a special character")
    for character in password:
        if character.lower():
                lower = True
        if character.upper():
                upper = True
        if lower != True or upper != True:
            print(f"The password must have a capital or lowercase letter")
    
        else:
            print("Password have been saved")
            password_list.append(password)
            break
print(password[0])



        
    