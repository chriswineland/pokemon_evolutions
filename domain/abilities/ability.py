from __future__ import annotations
from domain.pokemon_types import PokemonType
from domain.energy_pool import EnergyPool
import json


class Ability:
    id: int
    name: str
    description: str
    type: PokemonType
    cost: EnergyPool

    #JSON Keys
    ID_KEY: str = "id"
    NAME_KEY: str = "name"
    DESCRIPTION_KEY: str = "description"
    TYPE_KEY: str = "type"
    COST_KEY: str = "cost"

    def __init__(self, json_data: json = None, ability_data: Ability = None):
        if json_data is not None:
            self.populate_with_json_data(json_data)
        elif ability_data is not None:
            self.populate_with_ability_data(ability_data)

    def populate_with_json_data(self, json_data: json):
        self.id = json_data[self.ID_KEY]
        self.name = json_data[self.NAME_KEY]
        self.description = json_data[self.DESCRIPTION_KEY]
        self.type = PokemonType.parce_from_json(json_data)
        self.cost = EnergyPool(json_data=json_data[self.COST_KEY])

    def populate_with_ability_data(self, ability_data: Ability):
        pass