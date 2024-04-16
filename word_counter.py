# Welcome message
print("Welcome to the Word Counter!")

# Ask user for input
sentence = input("Enter a sentence or paragraph: ")

# Count the number of words
words = sentence.split()
word_count = len(words)

# Display the result
print("Number of words:", word_count)

# End of the program
print("Thank you for using the Word Counter!")
