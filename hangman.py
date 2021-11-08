import random
import os
import banners


# Paso 1 -> Devuelve un pokemon random convertido en una lista sin separaciones y una lista con 
# Los espacios correspondientes a las letras del pokemon
def get_random_pokemon():
    with open('./files/pokemon.txt', 'r', encoding='utf-8')as f:
        pokemon = [line.lower().rstrip() for line in f]
        pokemon = list(random.choice(pokemon))
        secret_pokemon = ['_' for letter in pokemon]
    return pokemon, secret_pokemon


#Paso 1.1 -> Print and clean
def clean_and_print(secret_pokemon):
    os.system('clear')
    print(secret_pokemon)


#Paso 2 -> El usuario introduce una letra, manejamos errores (en su momento)
def request_letter():
    letter = input('Guess a letter 👉 ')
    return letter.lower()


#Paso 3 Ciclo de comprobaciones
def check_letter(pokemon, secret_pokemon, letter):
    if letter in pokemon:
        confirm_letter(pokemon, secret_pokemon, letter)
    else:
        decline_letter(pokemon, secret_pokemon, letter)


#Paso 3.1 -> si la letra está en la palabra, reemplazamos el espacio vacío
def confirm_letter(pokemon, secret_pokemon, letter):
    for index, value in enumerate(pokemon):
        if letter == value:
            secret_pokemon[index] == letter
    clean_and_print(secret_pokemon)

#Paso 3.2 -> si no lo está, imprimimos el muñeco por partes
def decline_letter():
    pass


def run():
    print(banners.hello_banner)
    pokemon, secret_pokemon = get_random_pokemon() #Paso 1
    print(' '.join(pokemon))
    print(' '.join(secret_pokemon))
    letter = request_letter() #Paso 2
    check_letter(pokemon, secret_pokemon, letter) #Paso 3



if __name__ == '__main__':
    run()