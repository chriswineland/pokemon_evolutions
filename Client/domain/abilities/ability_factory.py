from __future__ import annotations
import json
from enum import Enum
from Client.domain.abilities.ability import Ability
from Client.domain.abilities.direct_damage_ability import DirectDamageAbility
from Client.domain.abilities.self_status_ability import SelfStatusAbility


class AbilitySubTypes(str, Enum):
    DIRECT_DAMAGE = "direct_damage"
    SELF_STATUS = "self_status"

    @staticmethod
    def create_from_value(value: str) -> AbilitySubTypes | None:
        match value:
            case AbilitySubTypes.DIRECT_DAMAGE.value:
                return AbilitySubTypes.DIRECT_DAMAGE
            case AbilitySubTypes.SELF_STATUS.value:
                return AbilitySubTypes.SELF_STATUS
            case _: 
                return None


def create_ability_from_json(json_data: json) -> Ability | None:
    ABILITY_SUB_TYPE_KEY: str = "ability_sub_type"
    ability_sub_type = AbilitySubTypes.create_from_value(json_data[ABILITY_SUB_TYPE_KEY])
    match ability_sub_type:
        case AbilitySubTypes.DIRECT_DAMAGE:
            return DirectDamageAbility(json_data=json_data)
        case AbilitySubTypes.SELF_STATUS:
            return SelfStatusAbility(json_data=json_data)
        case _:
            return None
