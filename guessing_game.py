def guessing_game(n):
    guess = input("make a guess: ")
    guess = int(guess)
    guess_count = 0
    while (guess_count < 10) and (guess != n) :
        if guess > n:
            print("Your guess is higher")
        elif guess < n:
            print("your guess is lower")
        elif guess == n:
            print("you are correct")
            break
        guess_count += 1
        guess = int(input("make a guess: "))
        
        

guessing_game(10)