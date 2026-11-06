#Imports the random module
import random


while True:
    #No of Lives
    lives=6

    #Open File and put the words into array
    file=open("words.txt","r")
    words=file.read().splitlines()
    secret_word=random.choice(words).upper()

    #Hidden word with Underscores
    hidden_word=["_ "]*len(secret_word)
    print(secret_word)
    # Guess letters array as a set to store unique values
    guessed_letters = set()

    #stages
    stages=["Stage 1","Stage 2","Stage 3","Stage 4","Stage 5","Stage 6"]

    #While loop to iterate
    while lives>0:

        #User Input
        guess=input("Guess a letter: ").upper()

        #checking the validity
        if len(guess)!=1 or not guess.isalpha():
            print("Invalid Input! Enter one Letter!")
            continue

        if guess in guessed_letters:
            print("You already guessed this letter")
            continue

        else:
            guessed_letters.add(guess)

            if guess in secret_word:
                print("Correct Guess!")
            else:
                print("Wrong Guess!")
                lives-=1

        #for loop to reveal hidden word letter by letter
        for index,letter in enumerate(secret_word):
            if letter == guess:
                hidden_word[index]=letter
        print(hidden_word)

        if lives==0:
            print("You lose!")
            print("The word was: "+secret_word)

        print(stages[6-lives])


        if hidden_word==list(secret_word):
            print("Congratulations! You guessed the word!")


    #Play again
    play_again=input("Do you want to play again (y/n)?").upper()
    if play_again == "Y":
        print("Starting a new game...")
        continue
    else:
        print("Thanks for playing!")
        break