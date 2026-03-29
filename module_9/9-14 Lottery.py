import random 

# Creates a list containing 10 numbers and 5 letters, using strings
lottery_choices = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                 'A', 'B', 'C', 'D', 'E']

numbers_only = lottery_choices[:10]  # First 10 items
letters_only = lottery_choices[10:]  # Remaining 5 items

winning_numbers = random.sample(numbers_only, 4)
winning_letter = random.choice(letters_only)

lottery_ticket = "".join(winning_numbers) + winning_letter

print("The Impossible Lottery Game")
print("Pick 4 #'s and a letter from A-E (e.g., 1234A)")
user_guess = input("Enter your 5-character lottery number: ")

if user_guess == lottery_ticket:
    print(f"How did you guess?! {user_guess} is the winning ticket! You won!")
else:
    print(f"Sorry, you lose.The winning ticket was: {lottery_ticket}")