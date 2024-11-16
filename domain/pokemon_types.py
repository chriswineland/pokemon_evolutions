from __future__ import annotations
from enum import Enum
import json


class PokemonType(str, Enum):
    NORMAL = 'normal'
    FIGHTING = 'fighting'
    FLYING = 'flying'
    POISON = 'poison'
    GROUND = 'ground'
    ROCK = 'rock'
    BUG = 'bug'
    GHOST = 'ghost'
    STEEL = 'steel'
    STELLAR = 'stellar'
    FIRE = 'fire'
    WATER = 'water'
    GRASS = 'grass'
    ELECTRIC = 'electric'
    PSYCHIC = 'psychic'
    ICE = 'ice'
    DRAGON = 'dragon'
    DARK = 'dark'
    FAIRY = 'fairy'

    @staticmethod
    def create_from_value(value: str) -> PokemonType | None:
        match value:
            case PokemonType.NORMAL.value:
                return PokemonType.NORMAL
            case PokemonType.FIGHTING.value:
                return PokemonType.FIGHTING
            case PokemonType.FLYING.value:
                return PokemonType.FLYING
            case PokemonType.POISON.value:
                return PokemonType.POISON
            case PokemonType.GROUND.value:
                return PokemonType.GROUND
            case PokemonType.ROCK.value:
                return PokemonType.ROCK
            case PokemonType.BUG.value:
                return PokemonType.BUG
            case PokemonType.GHOST.value:
                return PokemonType.GHOST
            case PokemonType.STEEL.value:
                return PokemonType.STEEL
            case PokemonType.STELLAR.value:
                return PokemonType.STELLAR
            case PokemonType.FIRE.value:
                return PokemonType.FIRE
            case PokemonType.WATER.value:
                return PokemonType.WATER
            case PokemonType.GRASS.value:
                return PokemonType.GRASS
            case PokemonType.ELECTRIC.value:
                return PokemonType.ELECTRIC
            case PokemonType.PSYCHIC.value:
                return PokemonType.PSYCHIC
            case PokemonType.ICE.value:
                return PokemonType.ICE
            case PokemonType.DRAGON.value:
                return PokemonType.DRAGON
            case PokemonType.DARK.value:
                return PokemonType.DARK
            case PokemonType.FAIRY.value:
                return PokemonType.FAIRY
            case _:
                return None
            
    @staticmethod
    def json_key() -> str:
        return 'pokemon_type'
    
    @staticmethod
    def parce_from_json(json_data: json) -> PokemonType | None:
        return PokemonType.create_from_value(json_data[PokemonType.json_key()])
