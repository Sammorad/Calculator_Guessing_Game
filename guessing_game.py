import pyinputplus as pyin
import random as rn 
n = rn.randint(0,15) # generating random numbers for the guessing game system 
"""
We will need to set a count for the life 
a list to insert the guess for checks 
and a count for the guess made by the perticipant 
"""
guess_count = 0
life_count = 3
guess_list = []
while True: 
    guess = int(pyin.inputInt(prompt := "make a guess: ") )
    if guess_count > 5 or life_count == 0:
        print(f"game over. The correct number is {n}")
        break
    elif (guess > n) and (guess in guess_list):
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
    
        
     
     