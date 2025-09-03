# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    user_input = input("Please enter a letter: ").lower()
    if len(user_input) != 1:
        print("Enter only one character.")
        return
    if not user_input.isalpha():
        print("Please enter a valid letter.")
        return
    vowels = ['a', 'e', 'i', 'o', 'u']
    if user_input in vowels:
        print(f"The letter {user_input} is a vowel.")
    else:
        print(f"The letter {user_input} is a consonant.")

    
    # Call the function
    check_letter()

