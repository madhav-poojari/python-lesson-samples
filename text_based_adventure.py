# Text-Based Adventure Game

# Welcome message
print("Welcome to the Text-Based Adventure Game!")

# Start of the adventure
print("\nYou find yourself standing at a crossroads.")
print("To the left is a dark cave.")
print("To the right is a lush forest.")

# Ask the player to choose a direction
direction = input("Which direction do you want to go? (left/right): ")

# Process the player's choice
if direction.lower() == "left":
    print("\nYou enter the dark cave and discover a treasure chest!")
    print("Congratulations! You found the treasure!")

    # Additional choice inside the cave
    print("\nAs you're about to leave the cave, you notice a mysterious passage deeper inside.")
    explore_cave = input("Do you want to explore the passage? (yes/no): ")
    if explore_cave.lower() == "yes":
        print("\nYou cautiously venture deeper into the cave.")
        print("You find a hidden chamber filled with ancient artifacts.")
        print("You collect some valuable treasures and make your way back out.")
    else:
        print("\nYou decide to leave the mysterious passage for another day.")
        print("You exit the cave and return to the crossroads.")

elif direction.lower() == "right":
    print("\nYou venture into the lush forest and encounter a friendly squirrel.")
    print("The squirrel leads you to a hidden clearing with a magical fountain.")
    print("You make a wish and feel refreshed.")

    # Additional choice in the forest
    print("\nAs you explore the forest, you come across a fork in the path.")
    choose_path = input("Which path do you want to take? (left/right): ")
    if choose_path.lower() == "left":
        print("\nYou follow the left path and stumble upon a beautiful waterfall.")
        print("You take a moment to enjoy the peaceful scenery before continuing your journey.")
    elif choose_path.lower() == "right":
        print("\nYou choose the right path and encounter a pack of friendly wolves.")
        print("They guide you to a hidden grove where you find a magical flower.")
        print("You pluck the flower and continue your adventure.")
    else:
        print("\nYou're indecisive and end up wandering aimlessly through the forest.")
        print("After some time, you find your way back to the crossroads.")

else:
    print("\nInvalid choice! You stand still and contemplate your options.")

# End of the adventure
print("\nThank you for playing the Text-Based Adventure Game!")
