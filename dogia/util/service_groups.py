from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "dogia_harvester dogia_timelord_launcher dogia_timelord dogia_farmer dogia_full_node dogia_wallet".split(),
    "node": "dogia_full_node".split(),
    "harvester": "dogia_harvester".split(),
    "farmer": "dogia_harvester dogia_farmer dogia_full_node dogia_wallet".split(),
    "farmer-no-wallet": "dogia_harvester dogia_farmer dogia_full_node".split(),
    "farmer-only": "dogia_farmer".split(),
    "timelord": "dogia_timelord_launcher dogia_timelord dogia_full_node".split(),
    "timelord-only": "dogia_timelord".split(),
    "timelord-launcher-only": "dogia_timelord_launcher".split(),
    "wallet": "dogia_wallet dogia_full_node".split(),
    "wallet-only": "dogia_wallet".split(),
    "introducer": "dogia_introducer".split(),
    "simulator": "dogia_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
