import random

# prepare a txt file
with open("hangman_words.txt") as hangman_words:
    list_of_words = []
    for line in hangman_words:
        word = hangman_words.readline()
        list_of_words.append(word.strip("	•	").strip("\n"))
# create a dictionary of all words from the txt file
dictionary_words = {}
for i in range(len(list_of_words)):
    dictionary_words[i] = list_of_words[i]
def play_game(): 
    # choose a random word from dictionary
    rand_num = random.randint(0, len(dictionary_words) - 1)
    guessed_word = dictionary_words[rand_num]
    # create "_ _ _" form of the guessed word 
    length_of_guessed_word = len(guessed_word)
    result = '_' * length_of_guessed_word
    # amount of wrong guesses a player can take
    wrong_guesses = 6
    print(f"You have {wrong_guesses} wrong guesses left")
    # show which letters have already been guessed
    already_guessed = []
    # show how long the guessed word is
    print(f"Length of guessed word is {length_of_guessed_word}")
    print("If you want to leave the game before the end, type 'exit'")
    # game is being played until the word is guessed or player runs out of attempts or types exit
    while wrong_guesses > 0 and result != guessed_word:
        print(f"Letters that has already been tried: {already_guessed}")
        your_letter = input("* Guess a letter: ")
        # case when a letter is in the word and haven't been guessed yet
        if your_letter in guessed_word and your_letter not in already_guessed:
            for i in range(length_of_guessed_word):
                # find all indeces of a letter in the word
                list_of_indeces = []
                if guessed_word[i] == your_letter:
                    list_of_indeces.append(i)
                # change all "_" to letters in the result
                for num in list_of_indeces:
                    result = result[:num] + your_letter + result[num+1:]
            # show the result
            print(f"{your_letter} is in the word!")
            print(result)
        # case when a letter has already been tried
        elif your_letter in already_guessed:
            print("You have already tried this letter! Try another one.")
        # let user leave the game before the game ends
        elif your_letter == "exit":
            break
        # case when a letter is not in the word
        else:
            print(result)
            # take away one attempt
            wrong_guesses -= 1
            already_guessed.append(your_letter)
            print(f"{your_letter} is not in the word :(")
            print(f"You have {wrong_guesses} guesses left!")
    if wrong_guesses == 0:
        print("You failed! Try another word")
        print(f"The guessed word was {guessed_word}")
    elif "_" not in result:
        print(f"You won! The word is {result}")
    # if user types exit
    else:
        print("Oops!")
    # ask if player wants to play another game
    play_another_game()
def play_another_game():
        another_game = input("Do you want to play another game? y/n ")
        if another_game == "y":
            play_game()
        elif another_game == "n":
            print("Alright! See you later.")
        else:
            print("I don't understand. Please tell me y(es) or n(o)")
            play_another_game()
play_game()
