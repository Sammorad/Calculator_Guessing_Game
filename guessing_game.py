import pyinputplus as pyin
import random as rn 
n = rn.randint(0,15)
guess = pyin.inputInt(prompt := "make a guess: ")
life_count = 3
guess_list = []
guess = int(guess)
guess_count = 0
while (guess_count < 5) and (guess != n) and life_count > 0:
        
    if (guess > n) and (guess in guess_list):
        print("guess is too high")
    elif (guess > n) and (guess not in guess_list):
        life_count -= 1
        print("guess is too high and you loss a live")
        print(f"Your Live count is {life_count}")
    elif (guess < n) and (guess in guess_list):
        print("guess is too low")
    elif guess < n and guess not in guess_list:
        life_count -= 1
        print("guess is too low and you loss a live")
        print(f"Your Live count is {life_count}")
    elif guess == n:
        print("you are correct")
        break
    guess_count += 1
        
    guess_list.append(guess)
    guess = pyin.inputInt(prompt:= "make a guess: ")
print(f"the correct number is {n}")
        
     
     