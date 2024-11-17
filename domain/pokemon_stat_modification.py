import json
from domain.delegate_protocols.delegator import Delegator
from domain.delegate_protocols.pokemon_stat_modification_protocol import PokemonStatModificationProtocol
from domain.pokemon_modifiable_stat import PokemonModifiableStat

class PokemonStatModification:
    delegates: list[PokemonStatModificationProtocol]
    name: str
    stat:  PokemonModifiableStat
    amount: int

    
