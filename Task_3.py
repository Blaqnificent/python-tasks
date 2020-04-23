"""Number Guessing Game.
   Usage:
        python guessinggame.py
"""
import random

def loop_var(usr_choice):
    """Determines the game difficulty level parameters.
        Args:
            usr_choice: The game difficulty level collected from the user.
        Returns:
            guess_count: The number of guesses a user has
            rand_num: A randomly generated integer within a range determined by usr_choice.  
    """
    if (usr_choice == 1):
        guess_count = 6
        rand_num = random.randint(1, 10)
    elif (usr_choice == 2):
        guess_count = 4
        rand_num = random.randint(1, 20)
    elif (usr_choice == 3):
        guess_count = 3
        rand_num = random.randint(1,50)
    return (guess_count, rand_num)

#Introduction. Collects user's name and displays the game levels available.
print ("Hi! What's your name?  :")
usr_name = input ()
print (f"Welcome to the guessing game {usr_name}. Choose a level from the options below: \n")
levels = ["Easy: 6 guesses. Number between 1 and 10", "Medium: 4 Guesses. Number between 1 and 20", "Hard: 3 Guesses. Number between 1 and 50"]
level_count = 0
for level in levels:
    level_count += 1
    print(f"{level_count} = {level}")

#Ensures that the user enters only 1,2 or 3 as the game difficulty level choice. 
choice_loop = True
while choice_loop:
    choice_options = [1,2,3]
    try:    
        usr_choice = int(input("\nEnter either 1, 2 or 3: "))
        if not usr_choice in choice_options:
            print("Wrong Selection. Please enter either '1', '2', or '3'")
        else:
            choice_loop = False
    except ValueError:
        print("Error. You should enter only whole numbers.")

guess_count, rand_num = loop_var(usr_choice) #Difficulty level parameters based on user's choice. 
# Main Guessing Program. 
game_status = True
while game_status:
    while (guess_count > 0): #Determines the number of 
            try: 
                usr_guess = int(input("Please enter your guess here: "))
                if usr_guess == rand_num:
                    print (f"You are right! Your guess is {rand_num}")
                    game_status = False
                    break
                else:
                    print ("You are wrong.")
                    guess_count -= 1
                    print (f"You've got {guess_count} guess(es) left.")
                    if guess_count == 0:
                        print("You have no more guesses left. Game Over!")
                        game_status = False
            except ValueError: #Ensures the user enters only integers. 
                print ("Error. Please enter a whole number.")