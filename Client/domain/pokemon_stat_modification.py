import json
from Client.domain.delegate_protocols.delegator import Delegator
from Client.domain.delegate_protocols.pokemon_stat_modification_protocol import PokemonStatModificationProtocol
from Client.domain.pokemon_modifiable_stat import PokemonModifiableStat

class PokemonStatModification:
    delegates: list[PokemonStatModificationProtocol]
    name: str
    stat:  PokemonModifiableStat
    amount: int

    
