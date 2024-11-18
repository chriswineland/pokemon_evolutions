from __future__ import annotations
from enum import Enum


class PokemonDamageType(str, Enum):
    PHYSICAL = 'physical'
    SPECIAL = 'special'
    
    @staticmethod
    def create_from_value(value: str) -> PokemonDamageType | None:
        match value:
            case PokemonDamageType.PHYSICAL.value:
                return PokemonDamageType.PHYSICAL
            case PokemonDamageType.SPECIAL.value:
                return PokemonDamageType.SPECIAL
            case _:
                return None
            

class PokemonDamage:
    pokemon_damage_type: PokemonDamageType
    
    def __init__(self, value: str):
        self.pokemon_damage_type = PokemonDamageType.create_from_value(value)

    @staticmethod
    def json_key() -> str:
        return "pokemon_damage_type"
