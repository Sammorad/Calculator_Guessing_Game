import random as rn 
def get_user_guess():
    guess = int(input("Enter your guess: "))
    return guess

def play_game():
    """the main guessing game,
    It takes input and test the guessing game"""
    live_count = 3
    guessing_list = []
    no_of_guesses  = 0
    number = rn.randint(1,15)
    print("Welcome to your Guessing game\n")
    print(f"You have {live_count} lives")
    while live_count > 0:
        guess = get_user_guess()
        no_of_guesses += 1
        if guess == number:
            print(f"your guess is correct")
            break

        elif guess > number and guess not in guessing_list:
            print("Your guess is too high")
            guessing_list.append(guess)
            live_count -= 1
        elif guess > number and guess in guessing_list:
            print("Your guess is too high")

        elif guess < number and guess not in guessing_list :
            print("your guess is too low")
            guessing_list.append(guess)
            live_count -= 1

        elif guess < number and guess in guessing_list:
            print("your guess is too low ")
    else:
        print(f"Game over, correct number is {number}")
def main():
    """This loop will ensure the game 
    continues in an interactive manner """
    
    while True:
        play_game()
        play_again = input("Will you play another game? (yes/no)").strip().lower()
        if play_again == "no":
            print("Its great having you play the game, goodbye")
            break
        elif play_again == "yes":
            continue

main()






    