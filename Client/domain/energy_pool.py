from __future__ import annotations
import json
from Client.domain.energy import Energy


class EnergyPoolElement:
    type: Energy
    amount: int

    def __init__(self, energy_type: Energy, energy_amount: int):
        self.type = energy_type
        self.amount = energy_amount


class EnergyPool:
    pool: list[EnergyPoolElement]

    #JSON Keys
    AMOUNT_KEY: str = "amount"

    def __init__(self, json_data: json = None, energy_pool_data: EnergyPool = None):
        self.pool = []
        if json_data is not None:
            self.populate_with_json_data(json_data)
        elif energy_pool_data is not None:
            self.populate_with_energy_pool_data(energy_pool_data)

    def populate_with_json_data(self, json_data: json):
        for pool_element in json_data:
            self.pool.append(EnergyPoolElement(pool_element[Energy.json_key()], pool_element[self.AMOUNT_KEY]))

    def populate_with_energy_pool_data(self, energy_pool_data: EnergyPool):
        pass
