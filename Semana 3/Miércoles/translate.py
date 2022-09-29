translate_dict = {}
translate_input= input("Please enter the dictionary in this format <palabra>:<traduccion> separated for commas: ")
translation_list = translate_input.split(",")
#['hola':'hello', 'adios':'bye']

for translation in translation_list:
    list_of_values = translation.split(":")
    #['hola', 'hello']
    translate_key = list_of_values[0]
    translate_value = list_of_values[1]
    translate_dict[translate_key] = translate_value
print(translate_dict)
