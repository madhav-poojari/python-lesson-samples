import random

# List of fortunes
fortunes = [
    "You will have a great day!",
    "A surprise awaits you soon!",
    "Good things come to those who wait.",
    "You will make a new friend today.",
    "Adventure awaits around the corner!",
    "Your hard work will pay off soon.",
    "Believe in yourself and you will succeed."
]

# Welcome message
print("Welcome to the Fortune Cookie Simulator!")

# Ask user if they want to crack open a fortune cookie
play_again = "yes"
while play_again.lower() == "yes":
    input("Press Enter to crack open your fortune cookie...")

    # Get a random fortune
    fortune = random.choice(fortunes)

    # Display the fortune
    print("Your fortune: ", fortune)

    # Ask if the user wants to play again
    play_again = input("Do you want to crack open another fortune cookie? (yes/no): ")

print("Thank you for using the Fortune Cookie Simulator!")
