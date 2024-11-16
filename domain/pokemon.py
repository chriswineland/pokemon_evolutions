from __future__ import annotations
from domain.abilities.ability import Ability
from domain.abilities.ability_factory import create_ability_from_json
from domain.energy_pool import EnergyPool
from domain.pokemon_types import PokemonType
from domain.delegate_protocols.delegator import Delegator
from domain.delegate_protocols.pokemon_status_protocol import PokemonStatusProtocol
from domain.weakness import Weakness
import json

class Pokemon(Delegator):
    
    delegates: list[PokemonStatusProtocol]
    id: int
    name: str
    type: PokemonType
    current_exp: int
    exp_to_level: int
    max_hp: int
    current_hp: int
    shield: int
    defence: int
    special_defence: int
    posible_abilities: list[Ability]
    active_abilities: list[Ability]
    ability_slots: int
    weakness: Weakness
    evolves_to_id: int | None
    evolved_from_id: int | None
    energy_pool: EnergyPool

    #JSON Keys
    ID_KEY: str = "id"
    NAME_KEY: str = "name"
    TYPE_KEY: str = "type"
    EXP_TO_LEVEL_KEY: str = "exp_to_level"
    MAX_HP_KEY: str = "max_hp"
    DEFENCE_KEY: str = "defence"
    SPECIAL_DEFENCE_KEY: str = "special_defence"
    POSIBLE_ABILITIES_KEY: str = "new_abilities"
    ABILITY_SLOTS_KEY: str = "ability_slots"
    WEAKNESS_KEY: str = "weakness"
    EVOLVES_TO_ID_KEY: str = "evolves_to_id"
    EVOLVED_FROM_ID_KEY: str = "evolved_from_id"

    def __init__(self, json_data: json = None, pokemon_data: Pokemon = None):
        if json_data is not None:
            self.populate_with_json_data(json_data)
        elif pokemon_data is not None:
            self.populate_with_pokemon_data(pokemon_data)

    def populate_with_json_data(self, json_data: json):
        self.id = json_data[self.ID_KEY]
        self.name = json_data[self.NAME_KEY]
        self.type = PokemonType.create_from_value(json_data[PokemonType.json_key()])
        self.current_exp = 0
        self.exp_to_level = json_data[self.EXP_TO_LEVEL_KEY]
        self.max_hp = json_data[self.MAX_HP_KEY]
        self.current_hp = 0
        self.shield = 0
        self.defence = json_data[self.DEFENCE_KEY]
        self.special_defence = json_data[self.SPECIAL_DEFENCE_KEY]
        self.evolves_to_id = json_data[self.EVOLVES_TO_ID_KEY]
        self.evolved_from_id = json_data[self.EVOLVED_FROM_ID_KEY]
        self.ability_slots = json_data[self.ABILITY_SLOTS_KEY]
        self.posible_abilities = []
        for ability_data in json_data[self.POSIBLE_ABILITIES_KEY]:
            parced_ability = create_ability_from_json(ability_data)
            if parced_ability is not None:
                self.posible_abilities.append(parced_ability)
        self.weakness = Weakness(json_data=json_data[self.WEAKNESS_KEY])
        self.energy_pool = EnergyPool()
            
    def populate_with_pokemon_data(self, pokemon_data: Pokemon):
        pass

    def evolve(evolution_data: json):
        pass
