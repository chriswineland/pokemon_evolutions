from Client.domain.pokemon_modifiable_stat import PokemonModifiableStat


class PokemonStatModificationProtocol():
    def pokemonStatModificationDidChange(self, stat: PokemonModifiableStat, amount: int):
        pass
