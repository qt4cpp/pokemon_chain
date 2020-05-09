from pokemon_dict import PokemonDict
from random import randint
from anytree import Node, RenderTree


dictionary = PokemonDict()


def chain(first_pokemon, last_pokemon):
    lucky_feeling(first_pokemon, last_pokemon)


def lucky_feeling(first_pokemon, last_pokemon):
    chain_hist = [first_pokemon]
    candidate_list = dictionary.search(first_pokemon.last_letter())
    while True:
        if not candidate_list:
            break
        next_item = candidate_list.pop(randint(0, len(candidate_list)-1))
        chain_hist.append(next_item)
        if next_item.last_letter() == last_pokemon.first_letter():
            chain_hist.append(last_pokemon)
            break
        elif next_item.last_letter() == 'ン':
            break
        candidate_list = dictionary.search(next_item.last_letter())

    for i in chain_hist:
        print(i)


