def print_welcome():
    print("**** Welcome ****")

def get_option(studies_dict):
    for key, value in studies_dict.items():
        for key_interno, value_interno in value.items():
            print(f"{key} -{value_interno}", end= "")
            print('') #separarlo en lineas
    return input("Please enter an option: ")

def get_client_data(study): #study son los option del diccionario principal U, R, I
    client = {
        "id":input('Please enter the client id: '),
        "age": input('Please enter the age: '),
        "gender": input('Please enter your gender M or F: '),
        "study": study
        }
    return client

def get_discounts(client, studies, client_number): #se colocan ambos parametros para acceder a lod  datos de los clientes y los precios de los estudios
    discount = 0
    if client.get('gender') == 'F' and int(client.get('age')) > 55:
        discount += studies.get(client.get('study')).get('price') * 0.25
    elif client.get('gender') == 'M' and int(client.get('age')) > 65:
        discount += studies.get(client.get('study')).get('price') * 0.25
    if client_number % 2 !=  0:
        discount += studies.get(client.get('study')).get('price') * 0.02
    return discount

def get_net_amount(client, discount, studies):
    return studies.get(client.get('study')).get('price') - discount
   

def print_invoice(client, studies, net_amount): #studies es el diccionario
    print("**** RECEIPT ****")
    print("id card", client.get("id"))
    print("age", client.get("age"))
    print("gender", client.get("gender"))
    print("study", studies.get(client.get("study")).get("description")) 
 

def main():
    studies_dict = {
        'U': {
            'description': 'Ultrasonido', 
            'price': 8900
        },
        'I': {'description': 'Tomografia', 
            'price': 12640
        },
        'R': {'description': 'Resonancia', 
        'price': 15600
        }
    }
    clients =[] #data de los clientes
    print_welcome()
    while True:
        option = get_option(studies_dict)
        client = get_client_data(option)
        clients.append(client) #agregamos el cliente a la base de datos
        discount = get_discounts(client, studies_dict, len(clients)) #datos del cliente, precios, y si el cliente es impar 
        print(discount)
        total = get_net_amount(client, discount)
        print_invoice(client, studies_dict, total)
        if input("Do you want to exit: \nY Yes or \nN No") == "Y":
            break
        print_final_day(clients)


main()