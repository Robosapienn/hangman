import random
import string
from words import words


def get_word(wordlist):
    word = random.choice(wordlist)
    while '-' in word or ' ' in word:
        word = random.choice(wordlist)

    return word


def hangman():
    word = get_word(words).upper()
    word_letters = set(word)
    used_letters = set()
    alphabet = set(string.ascii_uppercase)
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print('You have used these letters:', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('The current word is:', ' '.join(word_list))
        player_letter = input('Guess a letter:').upper()
        if player_letter in alphabet - used_letters:
            used_letters.add(player_letter)
            if player_letter in word_letters:
                word_letters.remove(player_letter)
            else:
                lives -= 1
                print(f"That letter is not in the word. You have {lives} lives left.")
        elif player_letter in used_letters:
            print('That character is already used. Type something else.')
        else:
            print('Invalid character.')

    if lives == 0:
        print(f"You have been hanged, the word was '{word}'.")
    else:
        print("Congratulations! You guessed the word correctly.")


hangman()
