from Client.domain.pokemon import Pokemon
from Client.domain.abilities.direct_damage_ability import DirectDamageAbility
from Client.domain.helper_scripts.deal_damage import deal_damage

def execute_ability(activating_pokemon: Pokemon, ability_id: int, targets: list[Pokemon]):
    ability_to_execute: DirectDamageAbility = activating_pokemon.get_ability_by_id(ability_id)
    attack_modified_damage_total = ability_to_execute.damage + activating_pokemon.attack_modifier
    deal_damage(attack_modified_damage_total, ability_to_execute.damage_type, ability_to_execute.type, targets)
