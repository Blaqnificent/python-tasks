# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 19:39:29 2020

@author: Bayo
"""

#Importing the necessary modules we need
import random
import string

#Getting the user details
def user_deets():
    first_name = input("Please enter your first name here: ")
    last_name = input("Please enter your last name here: ")
    user_email = input("Please enter your email address here: ")
    user_info = [first_name, last_name, user_email]
    return user_info

#Random password generator
def random_password_gen(user_deets_entry):
    rand_char = "".join([random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for char in range (5)]) #Generates five random characters in a list, and converts nto a string
    usr_password = str(user_deets_entry[0][:2]) + str(user_deets_entry[1][:2]) + rand_char #Converts and then Concatenates the first two letters of the first and last name to the randomly generated character sequence above. 
    return usr_password

#Start of main program. 

container = []
program_status = True
while program_status:
    user_deets_entry = user_deets()
    rand_pass = random_password_gen(user_deets_entry)
    print()
    print("Your randomly genearted password is " + rand_pass + ", would you like to keep it?") #Generates a random password from the user's first and last name
    usr_choice = input ("Enter either 'yes' to keep it,  or 'no' to choose your own: ")
    usr_choice = usr_choice.lower() #Ensures uniformity of user's input choice. Always lower case
    
    password_loop = True
    while password_loop:
        if usr_choice == 'yes':
            user_deets_entry.append(rand_pass) #Adds the generated password to the other user's details 
            container.append(user_deets_entry) #Adds the user's details to a container
            password_loop = False
        
        else:
            print ("Enter a password with at least 7 characters below: ")
            usr_choice = input()

            while len(usr_choice) < 7: #Keeps asking the user to enter a password till the length is 7 characters or longer
                print ("Your password is less than 7 characters. Choose a longer password: ")
                usr_choice =input()
                
            if len(usr_choice) >= 7: #If paasword is longer than 7, add to the other user's details
                user_deets_entry.append(usr_choice)
                container.append(user_deets_entry)
                password_loop = False #Breaks out of the password check loop

    new_usr_choice = input ("Would you like to enter a new user? Enter 'yes' or 'no': ")
    new_usr_choice = new_usr_choice.lower() #Ensures's user's choice is always lowercase. 

    if new_usr_choice == 'no':
        program_status = False
        for item in container: #Prints out all items in container, as long as we no longer collect any more details. 
            print (item)

    else:
        program_status = True

##END