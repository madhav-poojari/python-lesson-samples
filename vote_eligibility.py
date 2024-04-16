# Check Voting Eligibility

# Ask for user's age
age = int(input("Enter your age: "))

# Check if the user is eligible to vote
if age >= 18:
    print("You are eligible to vote!")
else:
    print("Sorry, you are not eligible to vote yet.")