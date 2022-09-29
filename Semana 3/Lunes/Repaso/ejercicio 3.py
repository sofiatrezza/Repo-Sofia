key = "contraseña"
password = input("Please enter your password: ")
if key == password.lower():
    print("correct password")
else:
    print("Error -> Incorrect password: ")
    password = input("Please enter your password: ")
