#List all drinks, foods and books.
menu = {
    'drinks': ['water', 'tea', 'coffee'],
    'foods': ['bagel', 'cake', 'sandwich'],
    'books': ['Macbeth', 'Oliver Twist', 'Sherlock Holmes']         
}

#Will be used to add new customers.
customers = {}

#Displays menu to customer includes food, drinks and books.
def display_menu():
    print("On todays food menu we have: ", menu['foods'])
    print("On todays drinks menu we have: ", menu['drinks'])
    print("And in our bookshop we have: ", menu['books'])

display_menu()

def display_items(food_item, drink_item, book_item):
    order = {"food order:": food_item, "drink order:": drink_item, "book order":book_item}

    if book_item:

        order["book_item"] = book_item

    return order

# Allows customers to select a item(food), drink and then a book
while True:
    food = input("\nWhat food would you like to order? Or enter 'quit' to exit.")
    if food.lower() == 'quit':
        break

    if food in menu['foods']:
        print(f"You have selected {food}")

    elif food not in menu['foods']:
         food = input(f"\nSorry we do not have {food}. \nPlease choose out of {menu['foods']} ")    

    drink = input("What drink would you like? ")

    if drink in menu['drinks']:
        print(f"You have selected {drink}")

    elif drink not in menu['drinks']:
        print(f"Sorry {drink} is not available. \n Please choose out of {menu['drinks']}")
        drink = input(f"\nSorry we do not have {drink}. \nPlease choose out of {menu['drinks']} ")

    book = input("If you would like, what book would you like to order? Or enter 'none'")

    if book in menu['books']:
        print(f"You have selected {book}")

    elif book not in menu['books']:
        book = input(f'Sorry we the book {book} requested is out of stock')
    order = display_items(food, drink, book)

    customer_order = (f"Your order is: {order}. The total cost of your order is: £-")
    print(customer_order)

    break 

#Allows employees to add more stock to the existing list. 
def employee():
    
    employee_r = "richie"
    employee_password = "*****"



    while True:
        employee_username = input("Username: ")
        employee_pass = input("Password: ")
        if employee_r == employee_username and employee_pass == employee_password: 
            print("\nHello Richie, items you would like to add...")

            add_item = input("Please enter food you would like to add: ")
            addition = menu['foods'].append(add_item)
            print(f"You have added {add_item} to {menu['foods']}")

            break
            #add ability to add to list 
        if employee_r != employee_username and employee_pass != employee_password:
            print("Wrong username or password try again.")

          

            

employee()



