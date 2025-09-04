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



# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    try:
        dog_age_input = input("Input a dog's age: ")
        dog_age = int(dog_age_input)
        if dog_age < 0:
            print("Age cannot be negative! Please enter a valid age.")
            return
        if dog_age <= 2:
            dog_years = dog_age * 10
        else:
            dog_years = 20 + (dog_age - 2) * 7
        print(f"The dog's age in dog years is {dog_years}.")
    except ValueError:
        print("Invalid input. Please enter a valid number for the dog's age.")
    except Exception as e:
        print(f"Error occurred: {e}")

# Call the function
calculate_dog_years()





# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    """
    Provides clothing advice based on weather conditions (cold and rain).
    Uses logical operators to determine the appropriate clothing recommendation.
    """
    try:
        cold_input = input("Is it cold? (yes/no): ").lower().strip()
        rain_input = input("Is it raining? (yes/no): ").lower().strip()

        if cold_input not in ['yes', 'no'] or rain_input not in ['yes', 'no']:
            print("Please answer with 'yes' or 'no' for both questions.")
            return
        is_cold = cold_input == 'yes'
        is_raining = rain_input == 'yes'
        if is_cold and is_raining:
            print("Wear a waterproof coat.")
        elif is_cold and not is_raining:
            print("Wear a warm coat.")
        elif not is_cold and is_raining:
            print("Carry an umbrella.")
        else:  
            print("Wear light clothing.") 
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
weather_advice()

