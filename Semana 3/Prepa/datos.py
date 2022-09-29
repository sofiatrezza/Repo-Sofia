info = {}
info["name"] = input("Please enter your full name: ")
info["last_name"] = input("Enter your last name: ")
info["age"] = input("Enter your age: ")
print(info)

# ejemplo quiz: listas, tuplas, diccionarios combinados
o_quiz = {"e1": {"e2": "pepe", "e3": "jose"}, "e4": [1,2,3]}

# tambien se puede escribir asi
o_quiz = {
    "e1": {"e2": "pepe", "e3": "jose"}, 
    "e4": [1,2,3]
    }
# para sacar un dato, para imprimirlo. ej: quiero imprimir "pepe"
o_quiz = ["e1"]["e2"]
# para sacar un dato, para imprimirlo. ej: quiero imprimir el "3"
o_quiz = ["e4"][2]
