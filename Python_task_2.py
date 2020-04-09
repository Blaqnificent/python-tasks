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
    usr_password = str(user_deets[0][:2]) + str(user_deets[1][:2]) + rand_char #Converts and then Concatenates the first two letters of the first and last name to the randomly generated character sequence above. 
    return usr_password

program_status = True
while program_status:
    user_deets_entry = user_deets()
    rand_pass = random_password_gen(user_deets_entry)
    print()
    print("Your randomly genearted password is " + rand_pass + ", would you like to keep it?")
    usr_choice = input ("Enter either 'yes' to keep it,  or 'no' to choose your own: ")
    usr_choice = usr_choice.lower()
    
    while True:
        if usr_choice == 'yes':
            user_deets_entry.append(rand_pass)