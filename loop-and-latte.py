menu = {
    'drinks': ['water', 'tea', 'coffee'],
    'foods': ['bagel', 'cake', 'sandwich'],
    'books': ['Macbeth', 'Oliver Twist', 'Sherlock Holmes']         
}

customers = {}

def display_menu(food, drink, book):
    print("On todays food menu we have: ", menu['foods'])
    print("On todays drinks menu we have: ", menu['drinks'])
    print("And in our bookshop we have: ", menu['books'])

print(menu)

def display_items(food_item, drink_item, book_item=None):
    order = {"food order:": food_item, "drink order:": drink_item}
    if book_item:
        order["book_item"] = book_item
    return order


while True:
    food = input("\nWhat food would you like to order? Or enter 'quit' to exit. ")
    if food.lower() == 'quit':
        break
    if food in menu['foods']:
        print(f"You have selected {food}")
    else:
        print(f"Sorry, {food} isn't available.")
    drink = input("What drink would you like? ")
    if drink in menu['drinks']:
        print(f"You have selected {drink}")
    else:
        print(f"Sorry {drink} is not available.")
    book = input("If you would like, what book would you like to order? Or enter 'none'")
    if book in menu['books']:
        print(f"You have selected {book}")
    else:
        book = None
    order = display_items(food, drink, book)
    print(f"your order was: {order}")
    break 
