import random
import os
import banners


def get_random_pokemon():
    with open('./files/pokemon.txt', 'r', encoding='utf-8')as f:
        pokemon = [line.upper().rstrip() for line in f]
        POKEMON = list(random.choice(pokemon))
        secret_pokemon = ['_' for letter in POKEMON]
    return POKEMON, secret_pokemon

def clear_and_print(POKEMON, secret_pokemon, attemps):
    os.system('clear')
    print(banners.HANGMANPICS[attemps])
    #print(' '.join(POKEMON))
    print(' '.join(secret_pokemon))


def game(POKEMON, secret_pokemon, attemps):
    while True:
        letter = input('Guess a letter to find the pokemon 👉').upper()
        assert len(letter) == 1 and letter.isalpha(), 'You only can type a letter'
        if letter in POKEMON:
            for i, value in enumerate(POKEMON):
                if letter == value:
                    secret_pokemon[i] = letter
        else:
            attemps = attemps + 1
        clear_and_print(POKEMON, secret_pokemon, attemps)
        if secret_pokemon == POKEMON:
            print(banners.WON)
            print('The pokemon was ' + str(' '.join(secret_pokemon)))
            break
        if attemps == 6:
            print(banners.LOSE)
            print('The pokemon was ' + str(' '.join(POKEMON)))
            break

def run():
    print(banners.hello_banner)
    input('Press any button to start to play 💥 Or press ctrl + C to exit')
    POKEMON, secret_pokemon = get_random_pokemon() #Firts step -> Read, choice and create a list with the pokemon
    attemps = 0 # User has only 6 attemps, count start in 0
    clear_and_print(POKEMON, secret_pokemon, attemps) # Second step -> clear the console and print the void list
    game(POKEMON, secret_pokemon, attemps)
        
        
if __name__ == '__main__':
    run()