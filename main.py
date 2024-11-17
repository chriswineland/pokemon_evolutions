from domain.pokemon import Pokemon
from domain.helper_scripts.evolve_pokemon_with_data import evolve_pokemon_with_data
import json


def print_json_data(json_data: json):
    print(json.dumps(json_data, indent=2))


machop_data: json
with open("json/base_pokemon/machop.json") as json_file:
    machop_data = json.load(json_file)
print("machop data:")
print_json_data(machop_data)
pokemon: Pokemon = Pokemon(json_data=machop_data)
print(pokemon.name)

machoke_evolution_data: json
with open("json/evolved_pokemon/machoke.json") as json_file:
    machoke_evolution_data = json.load(json_file)
print("machoke evolution data:")
print_json_data(machoke_evolution_data)
evolve_pokemon_with_data(pokemon, machoke_evolution_data)
print(pokemon.name)
