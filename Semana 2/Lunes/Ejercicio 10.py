option = int(input("Please enter a valid option: \n1- Vegetarian\n2- Non Vegetarian\n->"))
if option == 1:
    ingredient = int(input("Please enter the ingredient you want: \n1- Pimiento\n2- Non Tofu\n->"))
    if ingredient == 1:
        ingredient = "Pimiento"
    else:
        ingredient = "Tofu"
    print(f"The pizza is vegetarian a have these ingredients Tomato, Mozarella and {ingredient}")
elif option == 2:
    ingredient = int(input("Please enter the ingredient you want: \n1- Pepperoni\n2- Jamon\n3- Salmon\n->"))
    if ingredient == 1:
        ingredient = "Pepperoni"
    elif ingredient == 2:
        ingredient = "Jamon"
    else:
        ingredient = "Salmon"
    print(f"The pizza is non vegetarian a have these ingredients Tomato, Mozarella and {ingredient}")

else:
    print("Invalid Option")
