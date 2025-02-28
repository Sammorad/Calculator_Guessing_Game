import pyinputplus as pyin
def guessing_game(n):
    guess = pyin.inputInt(prompt := "make a guess: ")
    life_count = 7
    guess_list = []
    guess = int(guess)
    guess_count = 0
    while (guess_count < 10) and (guess != n) and life_count > 0:
        
        if (guess > n) and (guess in guess_list):
            print("guess is too high")
        elif (guess > n) and (guess not in guess_list):
            life_count -= 1
            print("guess is too low and you loss a live")
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
        
        
        

guessing_game(10)