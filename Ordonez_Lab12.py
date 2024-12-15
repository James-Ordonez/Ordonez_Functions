
# Display Menu

def display(menu):
    print("\nMenu: \n ")
    for food, price in menu.items():
        print(f"{food}: ₱{price:.2f}")

# Ordering Food

def order(menu):
    cost = 0 # Adding up cost
    ordered_food = [] # List selected items

    while True: 
            # User Input 
            choice = input("\nEnter the name of your order, type 'done' to finish\n")
            
            # User is done ordering
            if choice.lower() == "done":
                 break
            
            # Check if food in menu
            if choice in menu:
                 cost += menu[choice] # Add food cost to total cost
                 ordered_food.append(choice) # Append food to order
                 print(f"{choice} has been added to your ordered list. Current total is: ₱{cost:.2f}")

            else:
                 print("Invalid choice. Select an item from the menu")

    return cost, ordered_food

def payment(cost):
     while True:
          pesos = float(input(f"\n The total amount is ₱{cost:.2f}. Please enter the amount you are paying:"))

          if pesos >= cost:
               print(f"Payment done! Your change is {pesos - cost:.2f}. Thank you!")
               break
          else:
               print(f"Insufficient amount. Another ₱{cost - pesos:.2f} is required. ")

def main():
    menu = {
        "Spaghetti" : 99.99,
        "Cheesy Burger" : 79.99,
        "Normal Burger" : 59.99,
        "Fried Chicken" : 119.99,
        "Sundae" : 39.99
    }

    display(menu)

    cost, ordered_food = order(menu)

    if ordered_food:
        print("\nYou ordered:")
        for food in ordered_food:
            print(f"- {food}")
        print(f"Total cost: ₱{cost:.2f}")
        payment(cost)
    else:
        print("You did not order anything. Goodbye!")

if __name__ == "__main__":
    main()