from __future__ import annotations
from Client.domain.pokemon_types import PokemonType
from Client.domain.energy_pool import EnergyPool
from Client.domain.helper_scripts.safe_get import safe_get
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
        self.id = safe_get(json_data, self.ID_KEY)
        self.name = safe_get(json_data, self.NAME_KEY)
        self.description = safe_get(json_data, self.DESCRIPTION_KEY)
        self.type = PokemonType.create_from_value(safe_get(json_data, PokemonType.json_key()))
        self.cost = EnergyPool(json_data=safe_get(json_data, self.COST_KEY))

    def populate_with_ability_data(self, ability_data: Ability):
        pass

    def update_ability_with_values(self, update_ability: Ability):
        if update_ability.name is not None:
            self.name = update_ability.name
        if update_ability.description is not None:
            self.description = update_ability.description
        if update_ability.type is not None:
            self.type = update_ability.type
        if update_ability.cost is not None:
            self.cost = update_ability.cost
