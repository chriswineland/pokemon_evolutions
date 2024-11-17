import json
from domain.pokemon  import Pokemon


__ID_KEY: str = "id"
__NAME_KEY: str = "name"
__EVOLVED_FROM_ID_KEY: str = "evolves_from_id"

def evolve_pokemon_with_data(pokemon: Pokemon, data: json) -> bool:
    if not __is_valid_evolution(pokemon, data):
        return False
    __replace_evolution_values(pokemon, data)
    __update_evolution_values(pokemon, data)
    __upgrade_active_abilities(pokemon, data)
    __add_new_abilities(pokemon, data)
    return True

def  __is_valid_evolution(pokemon: Pokemon, data: json) -> bool:
    #could do validation of the json data but for this exersize we can assume its good
    return pokemon.id == data[__EVOLVED_FROM_ID_KEY]

def __replace_evolution_values(pokemon: Pokemon, data: json):
    pass

def __update_evolution_values(pokemon: Pokemon, data: json):
    pass

def __upgrade_active_abilities(pokemon: Pokemon, data: json):
    pass

def __add_new_abilities(pokemon: Pokemon, data: json):
    pass