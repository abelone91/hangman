# Hangman the game

import random

from stages import stages, logo, game_over_logo, you_won

from words import word_list

# display logo and ask player for name

print(logo)

player_name = input("Welcome to the HANGMAN game, enter your name here: ")

print(f'let\'s get started {player_name}')

# Generate random word

random_word = random.choice(word_list)
#
print(random_word)  # for debugging

# Find out length of word and replace alphabets with underscore

len_rand_word = len(random_word)

game_over = False
lives = 6

displayed_word_underscore = ""

for i in range(0, len_rand_word):
    i = "_"

    displayed_word_underscore = displayed_word_underscore + i

print(displayed_word_underscore)

# Ask the player to start guessing

while game_over == False:

    while lives > 0:

        player_guess = input(f"What's your guess {player_name}? ").lower()

        # Guess is word and correct
        if player_guess == random_word:
            print(you_won)
            lives = 0
            game_over = True

        # check if char and in generated random word, replace underscore with correct guess

        elif (len(player_guess) == 1) and (player_guess in random_word):
            # check if guess is already in displayed word
            if (len(player_guess) == 1) and (player_guess in displayed_word_underscore):
                print(stages[lives])
                print(f'you\'ve already guessed the character {player_guess}, remaining tries {lives}')
            # identify char postion in random_word generated and log postions to a list
            else:
                coordinates = []
                for char_pos in range(len_rand_word):
                    if random_word[char_pos] == player_guess:
                        coordinates.append(char_pos)
                # print(coordinates) #for debugging
                # change the displayed string with underscores to player_guess @ positions from coordinates list

                for i in coordinates:
                    displayed_word_underscore = displayed_word_underscore[
                                                :i] + player_guess + displayed_word_underscore[i + 1:]
                print(displayed_word_underscore)

                # if player guessed all the characters before lives = 0, display you won

                if displayed_word_underscore == random_word:
                    print(f'The correct guess is indeed: {displayed_word_underscore}')
                    print(you_won)
                    lives = 0
                    game_over = True
                # quit if out of attempts

                else:
                    if lives == 0:
                        print('you\'re out of attempts')
                        print(stages[0])
                        print(f'The correct word is: {random_word}')
                        print(game_over_logo)
                    else:
                        print(f'good guess. Character does exist in the word!, remaining tries {lives}')
                        print(stages[lives])
        # subtract life, if incorrect guess or out of attempts
        else:
            lives = lives - 1

            if lives == 0:
                game_over = True
                print(stages[0])
                print(f'The correct word is: {random_word}')
                print(game_over_logo)
            else:
                print(f"Character not in word! your remaining tries {lives} Try again")
                print(stages[lives])




