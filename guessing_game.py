import pyinputplus as pyin
import random as rn 
n = rn.randint(0,15) # generating random numbers for the guessing game system 
"""
We will need to set a count for the life 
a list to insert the guess for checks 
and a count for the guess made by the perticipant 
"""
life_count = 3
guess_list = []
guess_count = 0
while (guess_count < 5) and life_count > 0:  
    """This loop keeps the game running as long 
    as the life count is higher than zero and 
    participants made less than 5 guesses""" 
    guess = int(pyin.inputInt(prompt := "make a guess: ") )
    if (guess > n) and (guess in guess_list):
        print("guess is too high")
    elif (guess > n) and (guess not in guess_list):
        life_count -= 1
        print(f"guess is too high and your life count is reduced to {life_count}")
    elif (guess < n) and (guess in guess_list):
        print("guess is too low")
    elif (guess < n) and (guess not in guess_list):
        life_count -= 1
        print(f"guess is too low and your life count is reduced to {life_count}")
    elif guess == n:
        print("you are correct")
        break
    guess_count += 1
    guess_list.append(guess)
    
print(f"the correct number is {n}") #important we let participants know our selected number.
        
     
     