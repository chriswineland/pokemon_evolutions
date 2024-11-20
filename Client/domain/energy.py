from __future__ import annotations
from enum import Enum


class EnergyType(str, Enum):
    FAIRY = 'fairy'
    FIGHTING = 'fighting'
    FIRE = 'fire'
    GRASS = 'grass'
    LIGHTNING = 'lightning'
    PSYCHIC = 'psychic'
    WATER = 'water'
    DARKNESS = 'darkness'
    DRAGON = 'dragon'
    METAL = 'metle'
    BASIC = 'basic'

    @staticmethod
    def create_from_value(value: str) -> EnergyType | None:
        match value:
            case EnergyType.FAIRY.value:
                return EnergyType.FAIRY
            case EnergyType.FIGHTING.value:
                return EnergyType.FIGHTING
            case EnergyType.FIRE.value:
                return EnergyType.FIRE
            case EnergyType.GRASS.value:
                return EnergyType.GRASS
            case EnergyType.LIGHTNING.value:
                return EnergyType.LIGHTNING
            case EnergyType.PSYCHIC.value:
                return EnergyType.PSYCHIC
            case EnergyType.WATER.value:
                return EnergyType.WATER
            case EnergyType.DARKNESS.value:
                return EnergyType.DARKNESS
            case EnergyType.DRAGON.value:
                return EnergyType.DRAGON
            case EnergyType.METAL.value:
                return EnergyType.METAL
            case EnergyType.BASIC.value:
                return EnergyType.BASIC
            case _:
                return None
            

class Energy:
    energy_type: EnergyType
    
    def __init__(self, value: str):
        self.energy_type = EnergyType.create_from_value(value)

    @staticmethod
    def json_key() -> str:
        return "energy_type"
