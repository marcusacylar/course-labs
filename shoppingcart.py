# Create a variable named "money" and assign it the value 50 (integer)
money = 50
# Create a second variable named "shopping_cart" which will be an empty list
shopping_cart = []
# Create a dictionary with the following values:
# fruits = {"Apple": 5. "Raspberry": 10, "Lemon": 20}
fruits = {"Apple": 5, "Raspberry": 10, "Lemon": 20}
# Create an infinite while loop using the True condition
while True:
    # Within the loop, create a condition that checks if the amount of money assigned in the previous step is
    # less than or equal to 0
    if money <= 0:
        # If it is less than or equal to 0, print a thank you message to the user and break the loop
        print("You don't have anymore money. Thanks for shopping!")
        break
    # Add an else block to the if condition and ask the user for a fruit of his choice.
    # Note: Use the .title() function at the end of the input to cause it to begin with a capital letter
    else:
        player_choice = input(f"Select a fruit {fruits}: ").title()
        # In the else block, create a new if statement to check if the user chose a fruit that exists in the dictionary
        if player_choice in fruits:
            # Create a third if statement in the user's choice condition that checks if the user has enough money to
            # buy the fruit
            if money >= fruits[player_choice]:
                # Adding code to simulate a shopping cart
                shopping_cart.append(player_choice)
                money = money - fruits[player_choice]
                print(f"Shopping cart: {shopping_cart} \nMoney left: {money}")
                # break
            else:
                print("You don't have enough money to make this purchase.")
        # If the user's choice is not in the fruits dictionary, print an error message
        else:
            print("Invalid choice.")
