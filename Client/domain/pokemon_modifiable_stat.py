from __future__ import annotations
from enum import Enum

class PokemonModifiableStat(str, Enum):
    MAX_HP = "max_hp"
    DEFENSE = "defense"
    SPECIAL_DEFENSE = "special_defense"
    ATTACK_MODIFIER = "attack_modifier"

    @staticmethod
    def create_from_value(value: str) -> PokemonModifiableStat | None:
        match value:
            case PokemonModifiableStat.MAX_HP.value:
                return PokemonModifiableStat.MAX_HP
            case PokemonModifiableStat.DEFENSE.value:
                return PokemonModifiableStat.DEFENSE
            case PokemonModifiableStat.SPECIAL_DEFENSE.value:
                return PokemonModifiableStat.SPECIAL_DEFENSE
            case PokemonModifiableStat.ATTACK_MODIFIER.value:
                return PokemonModifiableStat.ATTACK_MODIFIER
            case _:
                return None