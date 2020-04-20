import re
from pokemon import Pokemon
from pokemon_dict import PokemonDict
from chain import chain


path = './data/pokedata'

d = PokemonDict()
print(d.search('ア')[0])
print(d.search('ゲ')[0])
print(d.search_no(1))
# for p in d.data:
#     print(p)
chain(d.search_name('ピカチュウ'), d.search_name('ミュウ'))
