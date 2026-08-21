import random
print("Welcome to hangman!")

words = ["hacker", "is", "another", "programmer"]


display = ""
# print(guess)
counter = 0
# game_over = False
while True:
    secret_word = random.choice(words)
    guess = input("Enter the letter you guessed: ").lower()

    for i in secret_word:
        if i == guess:
            display += "_"

        else:
            display += i
    print("The word was: ", display)
    

    if "_" in display:
        print("You won!")
        break
    elif "_" not in display:
        counter +=1
        # print("You lost")
        # break

    if counter >=4:
        print("You lost")
        break
    display = ""


