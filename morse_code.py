# Morse Code Translator

# Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}

# Welcome message
print("Welcome to the Morse Code Translator!")

# Ask user for input
option = input("Choose an option:\n1. Text to Morse code\n2. Morse code to text\nEnter your choice (1/2): ")

# Process user's choice
if option == '1':
    text = input("Enter the text to convert to Morse code: ").upper()
    morse_code = ''
    for char in text:
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
    print("Morse code:", morse_code)
elif option == '2':
    morse_code = input("Enter the Morse code to convert to text (separate letters with space): ")
    morse_code = morse_code.split(' ')
    text = ''
    for code in morse_code:
        for key, value in morse_code_dict.items():
            if code == value:
                text += key
    print("Text:", text)
else:
    print("Invalid option! Please choose 1 or 2.")

# End of the program
print("Thank you for using the Morse Code Translator!")
