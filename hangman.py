import random
import banners

def read():
    with open('./files/pokemon.txt', 'r', encoding='utf-8')as f:
        pokemon = [line.rstrip() for line in f]
    random_pokemon(pokemon)


def random_pokemon(pokemon):
    selected_pokemon = random.choice(pokemon)
    void_pokemon = selected_pokemon

    for i, value in enumerate(selected_pokemon):
        void_pokemon = void_pokemon.replace(value, '_')
    print(' '.join(selected_pokemon), ' '.join(void_pokemon))

    input_letter = input('Type a letter: ')

    for i, value in enumerate(selected_pokemon):
        if value == input_letter:
            result = void_pokemon.replace(void_pokemon[i], input_letter)
    print(result)

    #void_pokemon = ['_' for item in selected_pokemon]
    #print(' '.join(void_pokemon))
    #input_letter = input('Type a letter: ')
    # scan_letter(input_letter, selected_pokemon, void_pokemon)


# def scan_letter(input_letter, selected_pokemon, void_pokemon):
#     for index, value in enumerate(selected_pokemon):
#         if input_letter == value:
#             void_pokemon = list(map(lambda input_letter: value == input_letter, void_pokemon))
#             print(void_pokemon)


def run():
    #print(banners.hello_banner)
    read()


if __name__ == '__main__':
    run()