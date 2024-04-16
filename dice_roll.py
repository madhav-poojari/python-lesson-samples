import random

# Welcome message
print("Welcome to the Dice Rolling Simulator!")

# Ask user for input to roll the dice
roll_again = "yes"
while roll_again.lower() == "yes":
    # Roll the dice
    dice_value = random.randint(1, 6)

    # Display the result
    print("You rolled:", dice_value)

    # Ask if the user wants to roll again
    roll_again = input("Do you want to roll again? (yes/no): ")

print("Thank you for playing!")
