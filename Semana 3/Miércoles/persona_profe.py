info = {}
while True:
    key_name = input("What data do you want to save? eg: name, last name, phone, etc: ")
    value = input("Please enter the data value: ")
    info[key_name] = value

    for key, value in info.items():
        print(f"Your {key} is {value}")

    if input("Do you want to exit?: \nY- Yes \nN - No \n")== "Y":
        break