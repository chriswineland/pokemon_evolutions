from __future__ import annotations
from Client.domain.helper_scripts.safe_get import safe_get
from Client.domain.abilities.ability import Ability
from Client.domain.abilities.ability_factory import create_ability_from_json
from Client.domain.energy_pool import EnergyPool
from Client.domain.pokemon_types import PokemonType
from Client.domain.delegate_protocols.delegator import Delegator
from Client.domain.delegate_protocols.pokemon_status_protocol import PokemonStatusProtocol
from Client.domain.delegate_protocols.pokemon_stat_modification_protocol import PokemonStatModificationProtocol
from Client.domain.pokemon_condition import PokemonCondition
from Client.domain.pokemon_stat_modification import PokemonStatModification
from Client.domain.pokemon_modifiable_stat import PokemonModifiableStat
from Client.domain.weakness import Weakness
from Client.domain.game_log import GameLog
import json

class Pokemon(Delegator, PokemonStatModificationProtocol):
    delegates: list[PokemonStatusProtocol]
    id: int
    name: str
    type: PokemonType
    max_hp: int
    current_hp: int
    shield: int
    defense: int
    special_defense: int
    attack_modifier: int
    posible_abilities: list[Ability]
    active_abilities: list[Ability]
    conditions: list[PokemonCondition]
    stat_modifications: list[PokemonStatModification]
    ability_slots: int
    weakness: Weakness
    energy_pool: EnergyPool

    #JSON Keys
    ID_KEY: str = "id"
    NAME_KEY: str = "name"
    MAX_HP_KEY: str = "max_hp"
    DEFENSE_KEY: str = "defense"
    SPECIAL_DEFENSE_KEY: str = "special_defense"
    POSIBLE_ABILITIES_KEY: str = "new_abilities"
    ABILITY_SLOTS_KEY: str = "ability_slots"
    WEAKNESS_KEY: str = "weakness"

    def __init__(self, json_data: json = None, pokemon_data: Pokemon = None):
        if json_data is not None:
            self.populate_with_json_data(json_data)
        elif pokemon_data is not None:
            self.populate_with_pokemon_data(pokemon_data)
        GameLog.get_instance().log_pokemon_creation(self)

    def populate_with_json_data(self, json_data: json):
        self.id = safe_get(json_data, self.ID_KEY)
        self.name = safe_get(json_data,self.NAME_KEY)
        self.type = PokemonType.create_from_value(safe_get(json_data, PokemonType.json_key()))
        self.max_hp = safe_get(json_data, self.MAX_HP_KEY)
        self.current_hp = self.max_hp
        self.shield = 0
        self.defense = safe_get(json_data, self.DEFENSE_KEY)
        self.special_defense = safe_get(json_data, self.SPECIAL_DEFENSE_KEY)
        self.attack_modifier = 0
        self.ability_slots = safe_get(json_data, self.ABILITY_SLOTS_KEY)
        self.posible_abilities = []
        for ability_data in safe_get(json_data, self.POSIBLE_ABILITIES_KEY):
            parced_ability = create_ability_from_json(ability_data)
            if parced_ability is not None:
                self.posible_abilities.append(parced_ability)
        #for this mock project all posible abilities are active
        self.active_abilities = self.posible_abilities.copy()
        self.weakness = Weakness(json_data=safe_get(json_data, self.WEAKNESS_KEY))
        self.energy_pool = EnergyPool()
            
    def populate_with_pokemon_data(self, pokemon_data: Pokemon):
        pass

    def get_ability_by_id(self, ability_id: int) -> Ability | None:
        for ability in self.active_abilities:
            if ability.id == ability_id:
                return ability
        return None

    #PokemonStatModificationProtocol
    def pokemonStatModificationDidChange(self, stat: PokemonModifiableStat, amount: int):
        super().pokemonStatModificationDidChange(stat, amount)
        match stat:
            case PokemonModifiableStat.MAX_HP:
                self.max_hp += amount
                #make sure current hp is at or below new threshold
                self.current_hp = min(self.max_hp, self.current_hp)
            case PokemonModifiableStat.DEFENSE:
                self.defense += amount
            case PokemonModifiableStat.SPECIAL_DEFENSE:
                self.special_defense += amount
            case PokemonModifiableStat.ATTACK_MODIFIER:
                self.attack_modifier += amount
