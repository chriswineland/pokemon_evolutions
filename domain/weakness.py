from __future__ import annotations
from domain.pokemon_types import PokemonType
import json


class WeaknessElement:
    type: PokemonType
    amount: int

    #JSON Keys
    AMOUNT_KEY: str = "amount"

    def __init__(self, json_data: json):
        self.type = PokemonType.create_from_value(json_data[PokemonType.json_key()])
        self.amount = json_data[self.AMOUNT_KEY]

class Weakness:

    weaknesses: list[WeaknessElement]

    def __init__(self, json_data: json = None, weakness_data: Weakness = None):
        self.weaknesses = []
        if json_data is not None:
            self.__populate_with_json_data__(json_data)
        elif weakness_data is not None:
            self.__populate_with_weakness_data__(weakness_data)

    def __populate_with_json_data__(self, json_data: json):
        for weakness in json_data:
            self.weaknesses.append(WeaknessElement(weakness))

    def __populate_with_weakness_data__(self, weakness_data: Weakness):
        pass