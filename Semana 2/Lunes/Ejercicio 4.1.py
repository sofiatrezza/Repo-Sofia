number = float(input("Please enter a number: "))
is_valid = True
if number.isnumeric():
    if number%2==0:
        print(f"The {number} is even")
    else:
        print("The number {} is odd".format(number))
