from dataclasses import dataclass
from typing import List

from dogia.consensus.cost_calculator import NPCResult
from dogia.types.blockchain_format.coin import Coin
from dogia.types.blockchain_format.program import SerializedProgram
from dogia.types.blockchain_format.sized_bytes import bytes32
from dogia.types.spend_bundle import SpendBundle
from dogia.util.ints import uint64
from dogia.util.streamable import Streamable, streamable


@dataclass(frozen=True)
@streamable
class MempoolItem(Streamable):
    spend_bundle: SpendBundle
    fee: uint64
    npc_result: NPCResult
    cost: uint64
    spend_bundle_name: bytes32
    additions: List[Coin]
    removals: List[Coin]
    program: SerializedProgram

    def __lt__(self, other):
        return self.fee_per_cost < other.fee_per_cost

    @property
    def fee_per_cost(self) -> float:
        return int(self.fee) / int(self.cost)

    @property
    def name(self) -> bytes32:
        return self.spend_bundle_name
