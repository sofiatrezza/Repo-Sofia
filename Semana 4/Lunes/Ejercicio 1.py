number = int(input('Please enter a number: '))

count = 1

while count < number:
    count += 1
    if count*(count+1) ==  number:
        print(f"The number {number} is a pronic number")
        break

