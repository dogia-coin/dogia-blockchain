from setuptools import setup

dependencies = [
    "blspy==1.0.2",  # Signature library
    "dogiavdf==1.0.2",  # timelord and vdf verification
    "dogiabip158==1.0",  # bip158-style wallet filters
    "dogiapos==1.0.3",  # proof of space
    "clvm==0.9.7",
    "clvm_rs==0.1.8",
    "clvm_tools==0.4.3",
    "aiohttp==3.7.4",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==3.1.7",  # Binary data management library
    "colorlog==5.0.1",  # Adds color to logs
    "concurrent-log-handler==0.9.19",  # Concurrently log and rotate logs
    "cryptography==3.4.7",  # Python cryptography library for TLS - keyring conflict
    "keyring==23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
    "keyrings.cryptfile==1.3.4",  # Secure storage for keys on Linux (Will be replaced)
    #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  See https://github.com/frispete/keyrings.cryptfile/issues/15
    "PyYAML==5.4.1",  # Used for config file format
    "setproctitle==1.2.2",  # Gives the dogia processes readable names
    "sortedcontainers==2.3.0",  # For maintaining sorted mempools
    "websockets==8.1.0",  # For use in wallet RPC and electron UI
    "click==7.1.2",  # For the CLI
    "dnspython==2.1.0",  # Query DNS seeds
]

upnp_dependencies = [
    "miniupnpc==2.2.2",  # Allows users to open ports on their router
]

dev_dependencies = [
    "pytest",
    "pytest-asyncio",
    "flake8",
    "mypy",
    "black",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
]

kwargs = dict(
    name="dogia-blockchain",
    author="Mariano Sorgente",
    author_email="mariano@dogia.net",
    description="Dogia blockchain full node, farmer, timelord, and wallet.",
    url="https://dogia.net/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="dogia blockchain node",
    install_requires=dependencies,
    setup_requires=["setuptools_scm"],
    extras_require=dict(
        uvloop=["uvloop"],
        dev=dev_dependencies,
        upnp=upnp_dependencies,
    ),
    packages=[
        "build_scripts",
        "dogia",
        "dogia.cmds",
        "dogia.clvm",
        "dogia.consensus",
        "dogia.daemon",
        "dogia.full_node",
        "dogia.timelord",
        "dogia.farmer",
        "dogia.harvester",
        "dogia.introducer",
        "dogia.plotting",
        "dogia.pools",
        "dogia.protocols",
        "dogia.rpc",
        "dogia.server",
        "dogia.simulator",
        "dogia.types.blockchain_format",
        "dogia.types",
        "dogia.util",
        "dogia.wallet",
        "dogia.wallet.puzzles",
        "dogia.wallet.rl_wallet",
        "dogia.wallet.cc_wallet",
        "dogia.wallet.did_wallet",
        "dogia.wallet.settings",
        "dogia.wallet.trading",
        "dogia.wallet.util",
        "dogia.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "dogia = dogia.cmds.dogia:main",
            "dogia_wallet = dogia.server.start_wallet:main",
            "dogia_full_node = dogia.server.start_full_node:main",
            "dogia_harvester = dogia.server.start_harvester:main",
            "dogia_farmer = dogia.server.start_farmer:main",
            "dogia_introducer = dogia.server.start_introducer:main",
            "dogia_timelord = dogia.server.start_timelord:main",
            "dogia_timelord_launcher = dogia.timelord.timelord_launcher:main",
            "dogia_full_node_simulator = dogia.simulator.start_simulator:main",
        ]
    },
    package_data={
        "dogia": ["pyinstaller.spec"],
        "dogia.wallet.puzzles": ["*.clvm", "*.clvm.hex"],
        "dogia.util": ["initial-*.yaml", "english.txt"],
        "dogia.ssl": ["dogia_ca.crt", "dogia_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    use_scm_version={"fallback_version": "unknown-no-.git-directory"},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**kwargs)
