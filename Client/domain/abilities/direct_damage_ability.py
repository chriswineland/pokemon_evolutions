from __future__ import annotations
import json
from Client.domain.abilities.ability import Ability
from Client.domain.pokemon_damage_type import PokemonDamageType
from Client.domain.helper_scripts.safe_get import safe_get


class DirectDamageAbility(Ability):
    number_of_targets: int
    damage: int
    damage_type: PokemonDamageType

    #JSON Keys
    NUMBER_OF_TARGETS_KEY: str = "number_of_targets"
    DAMAGE_KEY: str = "damage"

    def __init__(self, json_data: json = None, ability_data: Ability = None):
        super().__init__(json_data=json_data, ability_data=ability_data)
        if json_data is not None:
            self.populate_with_json_data(json_data)
        elif ability_data is not None:
            self.populate_with_ability_data(ability_data)

    def populate_with_json_data(self, json_data: json):
        super().populate_with_json_data(json_data)
        self.number_of_targets = safe_get(json_data, self.NUMBER_OF_TARGETS_KEY)
        self.damage = safe_get(json_data, self.DAMAGE_KEY)
        self.damage_type = PokemonDamageType.create_from_value(safe_get(json_data, PokemonDamageType.json_key()))

    def populate_with_ability_data(self, ability_data: Ability):
        super().populate_with_ability_data(ability_data)
    
    def update_ability_with_values(self, update_ability: DirectDamageAbility):
        super().update_ability_with_values(update_ability)
        if update_ability.number_of_targets is not None:
            self.number_of_targets = update_ability.number_of_targets
        if update_ability.damage is not None:
            self.damage = update_ability.damage
