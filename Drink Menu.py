class Drink: 
    def __init__(self, name, price, color, description): # creator for the Drink class, adds attributes for drinks
        self.name = name
        self.price = price
        self.color = color
        self.description = description

class Order:
    def __init__(self): # creates an empty list to store drinks
        self.items = []

    def add_item(self, drink): #adds drinks to the order
        self.items.append(drink)

    def calculate_total(self):
        return sum(drink.price for drink in self.items) # calculates the total cost of all items in the order

def display_menu(drinks):
    print("Menu:")
    for i, drink in enumerate(drinks, start=1):
        print(f"{i} - {drink.name}: ${drink.price:.2f}") # Displays the menu with drink names and prices

def get_drink_info(drink):
    print(f"\n{drink.name} - {drink.description}\nColor: {drink.color}\n") # displays request information on the drink

def main():
    drinks = [
        Drink('Cola', 1.99, 'Brown', 'Refreshing cola drink'),
        Drink('Orange Juice', 2.49, 'Orange', 'Freshly squeezed orange juice'),
        Drink('Coffee', 3.29, 'Brown', 'Hot brewed coffee'),
        Drink('Iced Tea', 1.79, 'Amber', 'Chilled iced tea'),
        Drink('Lemonade', 2.99, 'Yellow', 'Homemade lemonade'),
        Drink('Mango Smoothie', 4.99, 'Yellow', 'Blended mango goodness'),
        Drink('Green Tea', 2.49, 'Green', 'Hot brewed green tea'),
        Drink('Sparkling Water', 1.29, 'Clear', 'Bubbly sparkling water'),
        Drink('Chai Latte', 3.79, 'Brown', 'Spicy chai latte'),
        Drink('Strawberry Lemonade', 3.49, 'Pink', 'Sweet strawberry lemonade'1),
    ] # adds drinks to the drink class

    order = Order()
     # Create an instance of the order class to manage the user's order
    while True:
        # Display options to the user
        print("\n1 - Start Order")
        print("2 - Get Drink Information")
        print("3 - Exit")
        #get the user's choice
        choice = input("Enter your choice (1, 2, or 3): ")
         #check to see what option the user chose
        if choice == "1":
            # User chose to start an order
            display_menu(drinks)
            while True:
                # loop to start an order
                drink_number = input("Enter the number of the drink you want to add to the order (or 'done' to finish): ")
                if drink_number.lower() == 'done':
                    break # end the loop if the user is done adding drinks

                try:
                    selected_drink = drinks[int(drink_number) - 1]
                    order.add_item(selected_drink)  #add the chosen drink to the order
                except (ValueError, IndexError):
                    print("Invalid input. Please enter a valid drink number.")
        elif choice == "2":
            # User chose to get information about the drink
            display_menu(drinks) # display the drinks menu
            drink_number = input("Enter the number of the drink you want more information about: ")
            try:
                selected_drink = drinks[int(drink_number) - 1]
                get_drink_info(selected_drink) # Display info on the selected drink
            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid drink number.")
        elif choice == "3": # user chose to end the program
            break # Exit main loop
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    total = order.calculate_total() # calculate total cost of the order
    print("\nReceipt:")
    # display receipt
    for item in order.items:
        print(f"{item.name}: ${item.price:.2f}")
    print(f"\nTotal: ${total:.2f}")

if __name__ == "__main__":
    main()