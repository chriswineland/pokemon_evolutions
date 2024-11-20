from __future__ import annotations
from Client.domain.pokemon_types import PokemonType


class GameLog:
    __instance = None

    @staticmethod
    def get_instance() -> GameLog:
        if GameLog.__instance is None:
            GameLog()
        return GameLog.__instance

    def __init__(self):
        if GameLog.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            GameLog.__instance = self

    def log_pokemon_creation(self, pokemon):
        print(pokemon.name + " was successfully created.")

    def log_evolution_event(self, pokemon):
        print(pokemon.name + " succesfuly evolved.")

    def log_damage_event(self, pokemon_taking_damage, amount: int, damage_type: PokemonType):
        print(pokemon_taking_damage.name + " is taking " + str(amount) + " " + damage_type.value + " damage.")