# Horoscope

print("Welcome to Horoscope!")

# Dictionary containing horoscopes
horoscopes = {
    "aries": "You will have a great day today!",
    "taurus": "Good news is coming your way!",
    "gemini": "Be prepared for unexpected opportunities!",
    "cancer": "Your creativity will shine today!",
    "leo": "You will meet someone special!",
    "virgo": "Focus on your goals, success is near!",
    "libra": "A new adventure awaits you!",
    "scorpio": "Trust your intuition, it will guide you!",
    "sagittarius": "It's a day for exploration and learning!",
    "capricorn": "Your hard work will pay off!",
    "aquarius": "Expect surprises in your social life!",
    "pisces": "Take some time for self-care today!"
}

# Ask for user's horoscope sign
sign = input("Enter your horoscope sign: ").lower()

# Display the horoscope
if sign in horoscopes:
    print("Your horoscope for today:", horoscopes[sign])
else:
    print("Horoscope not found for the given sign!")
