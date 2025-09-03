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


# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    voting_age = 18
    try:
        age_input = input("Please enter your age: ")
        age = int(age_input)
        if age < 0:
            print("Age cannot be negative. Please enter a valid age.")
            return
        if age >= voting_age:
            print(f"You are {age} years old. You are eligible to vote!")
        else:
            years_until_eligible = voting_age - age
            print(f"You are {age} years old. You are not eligible to vote yet.")
            print(f"You will be eligible to vote in {years_until_eligible} year(s).")
    except ValueError:
        print("Invalid input. Please enter a valid number for age.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
check_voting_eligibility()


