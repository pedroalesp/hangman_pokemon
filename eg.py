import random
import os


def run():

    PREV = ['''
+---+
|   |
    |
    |
    |
    |
=========''', 
'''
+---+
|   |
O   |
    |
    |
    |
=========''', 
'''
+---+
|   |
O   |
|   |
    |
    |
=========''', 
'''
+---+
|   |
O   |
/|   |
    |
    |
=========''', 
'''
+---+
|   |
O   |
/|\  |
    |
    |
=========''', 
'''
+---+
|   |
O   |
/|\  |
/    |
    |
=========''', 
'''
+---+
|   |
O   |
/|\  |
/ \  |
    |
========='''
]

    BASE = [
        "MONTEVIDEO",
        "CANELONES",
        "SAN JOSE",
        "MALDONADO",
        "COLONIA",
        "LAVALLEJA",
        "ROCHA",
        "FLORES",
        "TREINTA Y TRES",
        "DURAZNO",
        "SORIANO",
        "RIO NEGRO",
        "PAYSANDU",
        "SALTO",
        "ARTIGAS",
        "RIVERA",
        "TACUAREMBO",
        "FLORIDA"
        ]

    word = random.choice(BASE)
    spaces = ["_"] * len(word)
    attemps = 6

    while True:
        os.system("clear")
        for character in spaces:
            print(character, end=" ")
        print(PREV[attemps])
        letter = input("Dame una letra del departamento: ").upper()

        found = False
        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found = True

        if not found:
            attemps -= 1

        if "_" not in spaces:
            os.system("clear")
            print(F"Ganaste era {word}")
            break
            input()

        if attemps == 0:
            os.system("clear")
            print(F"Perdiste era {word}")
            break
            input()

if __name__ == '__main__':
    run()

   #_____________________________________________________________________
   # 
   
import os
import random


def read_words():
    words = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        words = [line.strip('\n') for line in f]
    return words


def transform_word(word):
    vowels_dict = {
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u'
    }
    for key, value in vowels_dict.items():
        word = str(word).replace(key, value)
    return word.upper()


def run():
    try:
        words = read_words()
        word_guess = transform_word(random.choice(words))
        guessed = "-" * len(word_guess)
        lineas = "-" * len(word_guess)
        LIFES = 5

        while guessed != word_guess:
            os.system("cls")
            print("Bienvenido al Juego del Ahorcado - Hangman Game")
            print("¡Adivina la palabra!")
            print("Vidas:", LIFES)
            print(guessed)

            if LIFES == 0:
                break

            letra = input("Ingresa una letra: ").upper()
            if letra.isnumeric():
                raise ValueError("Debe ingresar únicamente letras")

            if letra in word_guess:
                lineas = list(lineas)
                for index, element in enumerate(word_guess):
                    if letra == element:
                        lineas[index] = letra
                guessed = ''.join(lineas)
                print(guessed)
            else:
                print(guessed)
                LIFES -= 1
                continue
            
        if LIFES != 0:
            os.system("cls")
            print("¡Ganaste! La palabra era", word_guess)
        else:
            os.system("cls")
            print("¡Game Over! Inténtalo de nuevo")
    except ValueError as ve:
        print(ve)


if __name__=='__main__':
    run()  