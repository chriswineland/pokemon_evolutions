import json
from domain.abilities.ability import Ability


class SelfStatusAbility(Ability):
    
    #JSON Keys

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