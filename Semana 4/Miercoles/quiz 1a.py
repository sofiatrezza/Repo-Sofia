def main():
    products = {

        "mobiles": {

            "Apple": [

                {

                    "id": 1,

                    "name": "iPhone 7",

                    "price": 300

                },

                {

                    "id": 2,

                    "name": "iPhone 8",

                    "price": 350

                },

                {

                    "id": 3,

                    "name": "iPhone Xr",

                    "price": 450

                },

                {

                    "id": 4,

                    "name": "iPhone Xs",

                    "price": 460

                },

                {

                    "id": 5,

                    "name": "iPhone 11",

                    "price": 900

                },

                {

                    "id": 6,

                    "name": "iPhone 12",

                    "price": 1100

                },

                {

                    "id": 7,

                    "name": "iPhone 13",

                    "price": 1300

                },

            ],

            "Samsung": [

                {

                    "id": 8,

                    "name": "Samsung Galaxy Beam",

                    "price": 150

                },

                {

                    "id": 9,

                    "name": "Samsung Galaxy S6",

                    "price": 200

                },

                {

                    "id": 10,

                    "name": "Samsung Galaxy S7",

                    "price": 300

                },

            ],

            "Xiaomi": [

                {

                    "id": 11,

                    "name": "Xiaomi Redmi Note 8",

                    "price": 250

                },

                {

                    "id": 12,

                    "name": "Xiaomi Redmi Note 8 Pro",

                    "price": 300

                },

            ]

        },

        "laptops": {

            "DELL": [

                {

                    "id": 13,

                    "name": "Dell Inspiron 15",

                    "price": 600

                },

                {

                    "id": 14,

                    "name": "Dell Latitude 14",

                    "price": 650

                },

            ],

            "MAC": [

                {

                    "id": 15,

                    "name": "MacBook Pro 13",

                    "price": 900

                },

                {

                    "id": 16,

                    "name": "MacBook M1",

                    "price": 1500

                },

            ]

        },

    }

    while True:
        option = int(input('Please enter a valid option: \n1 Show  Inventory\n2 Make a purchase\n3 Exit \n ->'))
        if option == 1:
            categories = {1:  "mobiles", 2: "laptops"}
            category = int(input('Please enter a category: \n1 mobiles\n2 laptops\n->'))
            #los keys son los types y los brands son los values apple, samsung, xiaomi
            for types, brands in products.items():
                if types == categories.get(category):
                #ahora estamos dentro de brands con los dispositivos por marca
                    for brands, list_of_products in brands.items():
                        print(brands)
                        #ahora estamos en cada producto en su diccionario
                        for product in list_of_products:
                            #imprime el inventario seccionado por variable
                            id = product.get("id")
                            name = product.get("name")
                            price = product.get("price")
                            print(f'{id}-{name}-{price}')
            
        elif option == 2:
            product_id = int(input('Please enter the product id that you want: '))
            product_selected = None
            #al principio no esta seleccionado ninguno, abajo el ususario escoge con el id
            for types, brands in products.items():
                    for brands, list_of_products in brands.items():
                        for product in list_of_products:
                            #aqui se escoge el product selected
                            if product.get("id") == product_id:
                                product_selected = product
                                break
            if product_selected:
            #si encuentra el producto entonces
                client = { 
                    "name": input('Please enter your full name: '),
                    "id": input('Please enter your id number: '),
                    "product_id" : product_id
                }
                print("***** RECEIPT *****")
                for key, value in client.items():
                    if key != "product_id":
                        print(key, value)
                    for  key, value in product_selected.items():
                        print(key, value)
                        
            else:
                #si no consige el producto la variable se queda en None e imprime false:
                print('Product not found')
        
        elif option == 3:
            if input("Do you want to exit?: \nY- Yes \nN - No \n").upper() == "Y": 
                break
        else:
            continue

main()


