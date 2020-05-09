import re
from pokemon import Pokemon

path = 'data/pokedata'


class PokemonDict():

    def __init__(self):
        self.data_begin_with = {}
        with open(path) as f:
            for line in f:
                # matched = re.match(r"([\d\*]{3})\s+(\w+)", line)
                matched = re.match(r"([\d]{3})\s+(\w+)", line)
                if matched is None:
                    continue
                pokemon = Pokemon(matched.group(1), matched.group(2))
                self.add(pokemon)

    def add(self, pokemon):
        """pokemon class のインスタンスを database に追加する"""

        first_letter = pokemon.first_letter()
        if first_letter in self.data_begin_with:
            poke_list = self.data_begin_with[first_letter]
            poke_list.append(pokemon)
            self.data_begin_with[first_letter] = poke_list
        else:
            new_list = [pokemon]
            self.data_begin_with[first_letter] = new_list

    def search(self, first_letter):
        """ポケモンを最初の名前から"""

        return self.data_begin_with[first_letter]

    def search_no(self, number):
        """ポケモンNo.から該当する名前を返す"""
        for l in self.data_begin_with.values():
            for p in l:
                if p.number() == number:
                    return p
        return None

    def search_begin_with(self, first_letter):
        """first_letter で始まるポケモンのlist を返す"""
        return self.data_begin_with[first_letter]

    def search_name(self, name):
        """name が名前のポケモンを返す。
        いない場合は、 None をかえす
        """
        l = self.data_begin_with[name[0]]
        for p in l:
            if p.name == name:
                return p
        return None
