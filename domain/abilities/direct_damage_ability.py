import json
from domain.abilities.ability import Ability
from domain.helper_scripts.safe_get import safe_get


class DirectDamageAbility(Ability):
    number_of_targets: int
    damage: int

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

    def populate_with_ability_data(self, ability_data: Ability):
        super().populate_with_ability_data(ability_data)
        pass
