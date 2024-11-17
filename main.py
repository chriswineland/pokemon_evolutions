from domain.pokemon import Pokemon
from domain.helper_scripts.evolve_pokemon_with_data import evolve_pokemon_with_data
import json


machop_data: json
with open("json/base_pokemon_data/machop.json") as json_file:
    machop_data = json.load(json_file)
pokemon_1: Pokemon = Pokemon(json_data=machop_data)

machoke_evolution_data: json
with open("json/evolution_data/machoke.json") as json_file:
    machoke_evolution_data = json.load(json_file)
evolve_pokemon_with_data(pokemon_1, machoke_evolution_data)

machamp_evolution_data: json
with open("json/evolution_data/machamp.json") as json_file:
    machamp_evolution_data = json.load(json_file)
evolve_pokemon_with_data(pokemon_1, machamp_evolution_data)

bellsprout_data: json
with open("json/base_pokemon_data/bellsprout.json") as json_file:
    bellsprout_data = json.load(json_file)
pokemon_2: Pokemon = Pokemon(json_data=bellsprout_data)

print()