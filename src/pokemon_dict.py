import re
from pokemon import Pokemon

path = 'data/pokedata'


class PokemonDict():

    def __init__(self):
        self.data = {}
        with open(path) as f:
            for line in f:
                # matched = re.match(r"([\d\*]{3})\s+(\w+)", line)
                matched = re.match(r"([\d]{3})\s+(\w+)", line)
                if matched is None:
                    continue
                pokemon = Pokemon(matched.group(1), matched.group(2))
                self.add(pokemon)

    def add(self, pokemon):
        first_letter = pokemon.first_letter()
        if first_letter in self.data:
            poke_list = self.data[first_letter]
            poke_list.append(pokemon)
            self.data[first_letter] = poke_list
        else:
            new_list = [pokemon]
            self.data[first_letter] = new_list

    def search(self, first_letter):
        return self.data[first_letter]

    def search_no(self, number):
        for l in self.data.values():
            for p in l:
                if p.number() == number:
                    return p
        return None

    def search_first_letter(self, first_letter):
        return self.data[first_letter]

    def search_name(self, name):
        l = self.data[name[0]]
        for p in l:
            if p.name == name:
                return p
        return None
