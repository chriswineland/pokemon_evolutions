from __future__ import annotations
from enum import Enum

class PokemonCondition(str, Enum):
    ASLEEP = "asleep"
    BURNED = "burned"
    CONFUSED = "confused"
    PARALYZED = "paralyzed"
    POISONED = "poisoned"

    @staticmethod
    def create_from_value(value: str) -> PokemonCondition | None:
        match value:
            case PokemonCondition.ASLEEP.value:
                return PokemonCondition.ASLEEP
            case PokemonCondition.BURNED.value:
                return PokemonCondition.BURNED
            case PokemonCondition.CONFUSED.value:
                return PokemonCondition.CONFUSED
            case PokemonCondition.PARALYZED.value:
                return PokemonCondition.PARALYZED
            case PokemonCondition.POISONED.value:
                return PokemonCondition.POISONED
            case _:
                return None
