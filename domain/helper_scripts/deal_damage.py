from domain.pokemon_damage_type import PokemonDamageType
from domain.pokemon_types import PokemonType
from domain.weakness import WeaknessElement
from domain.pokemon import Pokemon
from domain.game_log import GameLog


def deal_damage(amount: int, damage_type: PokemonDamageType, ability_type: PokemonType, targets: list[Pokemon]):
    for target in targets:
        damage_type_modification: int = __calculate_damage_type_modification(target, damage_type)
        ability_weekness_modification: int = __calculate_ability_weakness_modification(target, ability_type)
        net_damage: int = amount  + damage_type_modification + ability_weekness_modification
        remaining_damage: int = 0
        if net_damage <= target.shield:
            target.shield -= net_damage
        elif target.shield > 0:
            remaining_damage = net_damage - target.shield
            target.shield = 0
        if remaining_damage > 0:
            target.current_hp -= remaining_damage
        GameLog.get_instance().log_damage_event(target, net_damage, ability_type)
            

def __calculate_damage_type_modification(target: Pokemon, damage_type: PokemonDamageType) -> int:
    reduction_amount: int = 0
    match damage_type:
        case PokemonDamageType.PHYSICAL:
            reduction_amount = target.defense
        case PokemonDamageType.SPECIAL:
            reduction_amount = target.special_defense
    #this is an adative value so we need to inverse the reductive amount for the calculation
    return reduction_amount * -1

def __calculate_ability_weakness_modification(target: Pokemon, ability_type: PokemonType) -> int:
    calculated_weakness_amount: int = 0
    for weakness_element in target.weakness.weaknesses:
        if weakness_element.type == ability_type:
            calculated_weakness_amount += weakness_element.amount
    return calculated_weakness_amount