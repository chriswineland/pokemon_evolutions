import json
from Client.domain.abilities.ability import Ability
from Client.domain.helper_scripts.safe_get import safe_get


class SelfStatusAbility(Ability):
    stat_modifications: list
    condition_modifications: list

    #JSON Keys
    STAT_MODIFICATIONS_KEY: str = "stat_modifications"
    CONDITION_MODIFICATION_KEY: str = "condition_modifications"

    def __init__(self, json_data: json = None, ability_data: Ability = None):
        super().__init__(json_data=json_data, ability_data=ability_data)
        if json_data is not None:
            self.populate_with_json_data(json_data)
        elif ability_data is not None:
            self.populate_with_ability_data(ability_data)

    def populate_with_json_data(self, json_data: json):
        super().populate_with_json_data(json_data)
        pass

    def populate_with_ability_data(self, ability_data: Ability):
        super().populate_with_ability_data(ability_data)
        pass