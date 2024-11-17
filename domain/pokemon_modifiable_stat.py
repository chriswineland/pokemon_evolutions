from __future__ import annotations
from enum import Enum

class PokemonModifiableStat(str, Enum):
    MAX_HP = "max_hp"
    DEFENCE = "defence"
    SPECIAL_DEFENCE = "special_defence"
    ATTACK_MODIFIER = "attack_modifier"

    @staticmethod
    def create_from_value(value: str) -> PokemonModifiableStat | None:
        match value:
            case PokemonModifiableStat.MAX_HP.value:
                return PokemonModifiableStat.MAX_HP
            case PokemonModifiableStat.DEFENCE.value:
                return PokemonModifiableStat.DEFENCE
            case PokemonModifiableStat.SPECIAL_DEFENCE.value:
                return PokemonModifiableStat.SPECIAL_DEFENCE
            case PokemonModifiableStat.ATTACK_MODIFIER.value:
                return PokemonModifiableStat.ATTACK_MODIFIER
            case _:
                return None