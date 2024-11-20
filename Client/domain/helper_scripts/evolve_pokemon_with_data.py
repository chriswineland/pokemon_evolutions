import json
from Client.domain.helper_scripts.safe_get import safe_get
from Client.domain.pokemon_types import PokemonType
from Client.domain.pokemon import Pokemon
from Client.domain.abilities.ability import Ability
from Client.domain.abilities.ability_factory import create_ability_from_json
from Client.domain.game_log import GameLog


#validity keys
__EVOLVED_FROM_ID_KEY: str = "evolved_from_id"
#update key
__CURRENT_HP_KEY: str = "current_hp"
__SHIELD_KEY: str = "shield"
#ability keys
__ABILITY_UPGRADES_KEY: str = "ability_upgrades"
__NEW_ABILITIES_KEY: str = "new_abilities"

def evolve_pokemon_with_data(pokemon: Pokemon, data: json) -> bool:
    if not __is_valid_evolution(pokemon, data):
        return False
    __replace_evolution_values(pokemon, data)
    __update_evolution_values(pokemon, data)
    __upgrade_active_abilities(pokemon, data)
    __add_new_abilities(pokemon, data)
    GameLog.get_instance().log_evolution_event(pokemon)
    return True

def  __is_valid_evolution(pokemon: Pokemon, data: json) -> bool:
    #could do validation of the json data but for this exersize we can assume its good
    return pokemon.id == data[__EVOLVED_FROM_ID_KEY]

def __replace_evolution_values(pokemon: Pokemon, data: json):
    pokemon.name = data[pokemon.NAME_KEY]
    pokemon.id = data[pokemon.ID_KEY]
    if updated_type_value := safe_get(data, PokemonType.json_key()) is not None:
        pokemon.type = PokemonType.create_from_value(updated_type_value)
    if updated_ability_slots := safe_get(data, pokemon.ABILITY_SLOTS_KEY) is not None:
        pokemon.ability_slots = updated_ability_slots
    
def __update_evolution_values(pokemon: Pokemon, data: json):
    if safe_get(data, pokemon.MAX_HP_KEY) is not None:
        pokemon.max_hp += data[pokemon.MAX_HP_KEY]
    if safe_get(data, __CURRENT_HP_KEY) is not None:
        pokemon.current_hp += data[__CURRENT_HP_KEY]
    pokemon.current_hp = min(pokemon.current_hp, pokemon.max_hp)
    if safe_get(data, __SHIELD_KEY) is not None:
        pokemon.shield += data[__SHIELD_KEY]
    pokemon.shield = max(0, pokemon.shield)
    if safe_get(data, pokemon.DEFENSE_KEY) is not None:
        pokemon.defense += data[pokemon.DEFENSE_KEY]
    if safe_get(data, pokemon.SPECIAL_DEFENSE_KEY) is not None:
        pokemon.special_defense += data[pokemon.SPECIAL_DEFENSE_KEY]

def __upgrade_active_abilities(pokemon: Pokemon, data: json):
    #get a list of upgraded ability information
    ability_upgrades_data = data[__ABILITY_UPGRADES_KEY]
    ability_upgrades: list[Ability] = []
    for ability_data in ability_upgrades_data:
        ability_upgrades.append(create_ability_from_json(ability_data))
    #go though the list and update any matching abilities by id currently on the pokemon
    for upgraded_ability in ability_upgrades:
        for active_ability in pokemon.active_abilities:
            if active_ability.id == upgraded_ability.id:
                active_ability.update_ability_with_values(upgraded_ability)

def __add_new_abilities(pokemon: Pokemon, data: json):
    new_abilities_data = data[__NEW_ABILITIES_KEY]
    for new_ability_data in new_abilities_data:
        #because all posible abilities are active, we can add them in both places
        pokemon.active_abilities.append(create_ability_from_json(new_ability_data))
        pokemon.posible_abilities.append(create_ability_from_json(new_ability_data))